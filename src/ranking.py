from __future__ import annotations

from dataclasses import dataclass
from math import log1p
from typing import Any, Dict, Iterable, List, Mapping

RANKING_VERSION = "ranking_v1"

REQUIRED_FIELDS = (
    "quality_score_avg",
    "utility_score_avg",
    "verified_review_ratio",
    "verified_review_count",
    "novelty_score",
    "spam_risk_score",
    "last_review_months",
    "maturity_level",
)

MATURITY_SCORES = {
    "prototype": 0.3,
    "stable": 0.7,
    "recommended": 1.0,
}

DEFAULT_SCENARIO = "default"

SCENARIO_CONFIGS: Dict[str, "RankingConfig"] = {
    DEFAULT_SCENARIO: None,
    "automation_reports": None,
    "modeling": None,
    "data_analysis": None,
}


@dataclass(frozen=True)
class RankingConfig:
    version: str
    quality_weight: float
    utility_weight: float
    maturity_weight: float
    verified_ratio_weight: float
    verified_count_weight: float
    novelty_weight: float
    recency_weight: float
    spam_penalty_weight: float
    min_verified_reviews: int = 3

    def recency_multiplier(self, last_review_months: int) -> float:
        if last_review_months > 12:
            return 0.7
        return 1.0


def _build_configs() -> None:
    SCENARIO_CONFIGS[DEFAULT_SCENARIO] = RankingConfig(
        version=RANKING_VERSION,
        quality_weight=0.4,
        utility_weight=0.4,
        maturity_weight=0.1,
        verified_ratio_weight=0.05,
        verified_count_weight=0.03,
        novelty_weight=0.02,
        recency_weight=0.1,
        spam_penalty_weight=0.2,
    )
    SCENARIO_CONFIGS["automation_reports"] = RankingConfig(
        version=RANKING_VERSION,
        quality_weight=0.35,
        utility_weight=0.45,
        maturity_weight=0.1,
        verified_ratio_weight=0.05,
        verified_count_weight=0.03,
        novelty_weight=0.02,
        recency_weight=0.1,
        spam_penalty_weight=0.2,
    )
    SCENARIO_CONFIGS["modeling"] = RankingConfig(
        version=RANKING_VERSION,
        quality_weight=0.45,
        utility_weight=0.35,
        maturity_weight=0.1,
        verified_ratio_weight=0.05,
        verified_count_weight=0.03,
        novelty_weight=0.02,
        recency_weight=0.1,
        spam_penalty_weight=0.2,
    )
    SCENARIO_CONFIGS["data_analysis"] = RankingConfig(
        version=RANKING_VERSION,
        quality_weight=0.4,
        utility_weight=0.4,
        maturity_weight=0.1,
        verified_ratio_weight=0.05,
        verified_count_weight=0.03,
        novelty_weight=0.02,
        recency_weight=0.1,
        spam_penalty_weight=0.2,
    )


_build_configs()


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _normalize_count(value: int, max_count: int = 50) -> float:
    if value <= 0:
        return 0.0
    return _clamp(log1p(value) / log1p(max_count), 0.0, 1.0)


def _extract_metrics(item: Mapping[str, Any], scenario: str) -> Mapping[str, Any]:
    scenario_metrics = item.get("scenario_metrics", {})
    if scenario in scenario_metrics:
        return scenario_metrics[scenario]
    return item


def validate_items(items: Iterable[Mapping[str, Any]], scenario: str) -> None:
    missing_fields: List[str] = []
    for item in items:
        metrics = _extract_metrics(item, scenario)
        for field in REQUIRED_FIELDS:
            if field not in metrics:
                missing_fields.append(field)
    if missing_fields:
        missing_list = ", ".join(sorted(set(missing_fields)))
        raise ValueError(f"Missing required ranking fields: {missing_list}")


def _get_config(scenario: str) -> RankingConfig:
    if not SCENARIO_CONFIGS:
        _build_configs()
    if scenario in SCENARIO_CONFIGS and SCENARIO_CONFIGS[scenario] is not None:
        return SCENARIO_CONFIGS[scenario]
    return SCENARIO_CONFIGS[DEFAULT_SCENARIO]


def score_item(metrics: Mapping[str, Any], config: RankingConfig) -> float:
    quality_score = _clamp(float(metrics["quality_score_avg"]), 1.0, 5.0) / 5.0
    utility_score = _clamp(float(metrics["utility_score_avg"]), 1.0, 5.0) / 5.0
    verified_ratio = _clamp(float(metrics["verified_review_ratio"]), 0.0, 1.0)
    verified_count = int(metrics["verified_review_count"])
    novelty_score = _clamp(float(metrics["novelty_score"]), 0.0, 1.0)
    spam_risk = _clamp(float(metrics["spam_risk_score"]), 0.0, 1.0)
    last_review_months = int(metrics["last_review_months"])
    maturity_level = str(metrics["maturity_level"]).lower()
    maturity_score = MATURITY_SCORES.get(maturity_level, 0.0)

    if verified_count < config.min_verified_reviews:
        return 0.0

    base_score = (
        config.quality_weight * quality_score
        + config.utility_weight * utility_score
        + config.maturity_weight * maturity_score
        + config.verified_ratio_weight * verified_ratio
        + config.verified_count_weight * _normalize_count(verified_count)
        + config.novelty_weight * novelty_score
    )

    recency_multiplier = config.recency_multiplier(last_review_months)
    recency_factor = (1 - config.recency_weight) + config.recency_weight * recency_multiplier
    adjusted_score = base_score * recency_factor
    penalty = config.spam_penalty_weight * spam_risk

    return adjusted_score - penalty


def rank_search_results(
    items: Iterable[Mapping[str, Any]],
    scenario: str,
    version: str = RANKING_VERSION,
) -> List[Dict[str, Any]]:
    if version != RANKING_VERSION:
        raise ValueError(f"Unsupported ranking version: {version}")

    items_list = list(items)
    validate_items(items_list, scenario)
    config = _get_config(scenario)

    ranked: List[Dict[str, Any]] = []
    for item in items_list:
        metrics = _extract_metrics(item, scenario)
        score = score_item(metrics, config)
        ranked_item = dict(item)
        ranked_item["rank_score"] = round(score, 6)
        ranked_item["ranking_version"] = config.version
        ranked.append(ranked_item)

    ranked.sort(key=lambda entry: entry["rank_score"], reverse=True)
    return ranked
