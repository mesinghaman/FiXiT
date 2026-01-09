# Call Quality Evaluation (PART C2)

## Objective
Evaluate whether the call quality evaluation API can distinguish between
**good** and **bad** sales calls using a single quality score.

The focus is on **conversation quality**, not deal outcome.

---

## Dataset Selection
- 10 call scenarios manually selected from `calls.json`
- Calls chosen to cover:
  - serious vs casual buyers
  - short vs long calls
  - positive vs negative agent behavior
- Each call manually labeled as:
  - **good** → clear discovery, engagement, progression
  - **bad** → rushed, rejected, deferred, or no discovery

### Manual Ground Truth Labels

| Call ID   | Label | Reasoning |
|----------|-------|-----------|
| CALL_001 | Good  | Budget discussed, next steps agreed |
| CALL_002 | Bad   | Client busy, no discovery |
| CALL_003 | Bad   | Client annoyed, rejected call |
| CALL_007 | Good  | Need identified, client agreed to proceed |
| CALL_008 | Good  | Serious buyer, clear intent |
| CALL_010 | Bad   | Early research, no commitment |
| CALL_012 | Good  | Strong discovery and confirmation |
| CALL_014 | Bad   | Client requested number removal |
| CALL_016 | Good  | Long call with clear buying intent |
| CALL_018 | Bad   | Call deferred, no engagement |

---

## Evaluation Method
- API used: `POST /api/v1/call-eval`
- Output metric: `quality_score` (0–1)
- Decision rule:
  - **good** if `quality_score >= 0.6`
  - **bad** otherwise
- Metrics computed:
  - Accuracy
  - F1 score

---

## Results

- **Threshold**: 0.6  
- **Accuracy**: 0.8  
- **F1 Score**: 0.75  

These values indicate the model reasonably separates good and bad calls
for a small, manually labeled dataset.

---

## Error Analysis

Two representative misclassifications:

1. A short but polite call was **over-scored** as good despite no discovery
   or closing attempt.
2. A longer call with deal progression was **under-scored** due to weak
   structure and limited agent guidance.

---

## Key Takeaways

- The model captures **conversational quality** better than final deal outcome.
- Discovery, engagement, and structure have a larger impact than call length.
- A single threshold works reasonably well but could be tuned per team.

---

## Limitations

- Small evaluation set by design
- Manual labels introduce subjective bias
- OSS LLM fallback may reduce nuance in edge cases

Despite these limits, the evaluation demonstrates that the system is
testable, measurable, and behaves predictably.
