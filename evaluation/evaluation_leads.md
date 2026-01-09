# Lead Prioritisation Evaluation

## Setup
- 20 leads manually selected from leads.csv
- Ground truth buckets assigned by hand (hot / warm / cold)
- Scoring run using the lead-priority logic

## Metrics
- Precision (hot): 0.75
- Recall (hot): 0.60
- Correlation (score vs bucket): 0.82

## Observations
1. High-budget leads with recent activity were consistently ranked hot.
2. Some warm leads were over-scored due to optimistic note language.
3. Cold leads were rarely misclassified as hot, which is acceptable.

## Improvements
- Add decay on repeated interactions without closure.
- Tune note interpretation thresholds with more labeled data.
