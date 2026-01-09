import sys
import unittest

sys.path.append("src")

from ranking import RANKING_VERSION, rank_search_results


class RankingTests(unittest.TestCase):
    def test_rank_search_results_uses_scenario_metrics(self):
        items = [
            {
                "id": "tool-a",
                "scenario_metrics": {
                    "data_analysis": {
                        "quality_score_avg": 4.6,
                        "utility_score_avg": 4.5,
                        "verified_review_ratio": 0.9,
                        "verified_review_count": 20,
                        "novelty_score": 0.3,
                        "spam_risk_score": 0.1,
                        "last_review_months": 3,
                        "maturity_level": "stable",
                    },
                    "automation_reports": {
                        "quality_score_avg": 3.2,
                        "utility_score_avg": 3.0,
                        "verified_review_ratio": 0.4,
                        "verified_review_count": 5,
                        "novelty_score": 0.7,
                        "spam_risk_score": 0.2,
                        "last_review_months": 2,
                        "maturity_level": "prototype",
                    },
                },
            },
            {
                "id": "tool-b",
                "scenario_metrics": {
                    "data_analysis": {
                        "quality_score_avg": 4.1,
                        "utility_score_avg": 4.2,
                        "verified_review_ratio": 0.8,
                        "verified_review_count": 12,
                        "novelty_score": 0.5,
                        "spam_risk_score": 0.05,
                        "last_review_months": 2,
                        "maturity_level": "recommended",
                    }
                },
            },
        ]

        ranked = rank_search_results(items, scenario="data_analysis")
        self.assertEqual(ranked[0]["id"], "tool-a")
        self.assertEqual(ranked[0]["ranking_version"], RANKING_VERSION)

    def test_recency_penalty_applies(self):
        items = [
            {
                "id": "newer",
                "quality_score_avg": 4.0,
                "utility_score_avg": 4.0,
                "verified_review_ratio": 0.8,
                "verified_review_count": 10,
                "novelty_score": 0.4,
                "spam_risk_score": 0.1,
                "last_review_months": 2,
                "maturity_level": "stable",
            },
            {
                "id": "older",
                "quality_score_avg": 4.0,
                "utility_score_avg": 4.0,
                "verified_review_ratio": 0.8,
                "verified_review_count": 10,
                "novelty_score": 0.4,
                "spam_risk_score": 0.1,
                "last_review_months": 14,
                "maturity_level": "stable",
            },
        ]

        ranked = rank_search_results(items, scenario="default")
        self.assertEqual(ranked[0]["id"], "newer")
        self.assertGreater(ranked[0]["rank_score"], ranked[1]["rank_score"])

    def test_missing_fields_validation(self):
        items = [
            {
                "id": "broken",
                "quality_score_avg": 4.0,
                "utility_score_avg": 4.0,
            }
        ]

        with self.assertRaises(ValueError):
            rank_search_results(items, scenario="default")

    def test_min_verified_review_threshold(self):
        items = [
            {
                "id": "low-verified",
                "quality_score_avg": 5.0,
                "utility_score_avg": 5.0,
                "verified_review_ratio": 1.0,
                "verified_review_count": 1,
                "novelty_score": 1.0,
                "spam_risk_score": 0.0,
                "last_review_months": 1,
                "maturity_level": "recommended",
            }
        ]

        ranked = rank_search_results(items, scenario="default")
        self.assertEqual(ranked[0]["rank_score"], 0.0)


if __name__ == "__main__":
    unittest.main()
