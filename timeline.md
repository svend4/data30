# Project Timeline

> Fill in the duration estimates (in working days), risk criticality, and baseline start date.
> The schedule fields will then be calculated accordingly.

## Assumptions
- Working calendar: 5-day work week.
- Buffers are added to each stage as a separate line item (not merged into the base estimate).
- Dates should be adjusted after approvals/inputs are available.

## Stage Plan

| Stage | Base estimate (days) | Risk criticality (Low/Med/High) | Risk buffer (days) | Dependencies | Critical path | Start date | End date | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Discovery & scope | 10 | Med | 2 | None | Yes | 2025-01-06 | 2025-01-21 | Detailed tasks in Gantt |
| 2. Requirements & solution design | 16 | Med | 3 | 1 | Yes | 2025-01-22 | 2025-02-17 | Detailed tasks in Gantt |
| 3. Implementation | 35 | High | 7 | 2 | Yes | 2025-02-18 | 2025-04-16 | MVP milestone at end of stage |
| 4. QA & validation | 17 | Med | 3 | 3 | Yes | 2025-04-17 | 2025-05-14 | Beta milestone at end of stage |
| 5. Release & handover | 9 | Low | 2 | 4 | Yes | 2025-05-15 | 2025-05-29 | Scale milestone at end of stage |

## Critical Path Summary
- 1 → 2 → 3 → 4 → 5 (sequential dependency chain; buffers add calendar time but not scope).

## Overall Duration
- Total base duration: 87 days
- Total buffer: 17 days
- Total duration (base + buffer): 104 days

## Date Baseline
- Project start: 2025-01-06
- Project end: 2025-05-29

## Gantt (Discovery/Design detailed, rest summarized)
```mermaid
gantt
    title Project Plan (5-day week, buffers as separate tasks)
    dateFormat  YYYY-MM-DD
    excludes    weekends
    section Discovery (detailed, week 1-2)
    Анализ требований и целей           :crit, disc_req, 2025-01-06, 4d
    Сбор и приоритизация стейкхолдеров  :crit, disc_stake, after disc_req, 3d
    Формирование backlog и roadmap      :crit, disc_backlog, after disc_stake, 3d
    Discovery risk buffer               :crit, disc_buf, after disc_backlog, 2d

    section Design (detailed)
    Архитектурное проектирование        :crit, design_arch, after disc_buf, 6d
    UX/UI прототипирование              :crit, design_ux, after design_arch, 6d
    Проработка NFR                      :crit, design_nfr, after design_ux, 4d
    Design risk buffer                  :crit, design_buf, after design_nfr, 3d

    section Development (summary)
    Development (MVP scope)             :crit, dev_stage, after design_buf, 35d
    Development risk buffer             :crit, dev_buf, after dev_stage, 7d
    MVP milestone                       :milestone, mvp, after dev_buf, 0d

    section QA (summary)
    QA & validation                     :crit, qa_stage, after dev_buf, 17d
    QA risk buffer                      :crit, qa_buf, after qa_stage, 3d
    Beta milestone                      :milestone, beta, after qa_buf, 0d

    section Release (summary)
    Release & handover                  :crit, rel_stage, after qa_buf, 9d
    Release risk buffer                 :crit, rel_buf, after rel_stage, 2d
    Scale milestone                     :milestone, scale, after rel_buf, 0d
```
