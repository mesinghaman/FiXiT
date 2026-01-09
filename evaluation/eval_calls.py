from typing import List, Tuple

from src.llm.call_model import analyze_call


def accuracy_f1(pred: List[int], truth: List[int]) -> Tuple[float, float]:
    tp = sum(p == 1 and t == 1 for p, t in zip(pred, truth))
    tn = sum(p == 0 and t == 0 for p, t in zip(pred, truth))
    fp = sum(p == 1 and t == 0 for p, t in zip(pred, truth))
    fn = sum(p == 0 and t == 1 for p, t in zip(pred, truth))

    acc = (tp + tn) / len(pred)
    f1 = (2 * tp) / (2 * tp + fp + fn) if (2 * tp + fp + fn) else 0.0
    return round(acc, 3), round(f1, 3)


def run_eval() -> None:
    calls = [
        ("CALL_001", "good", "Agent discussed budget and next steps clearly."),
        ("CALL_002", "bad", "Client busy, no discovery."),
        ("CALL_003", "bad", "Client irritated, rejected call."),
        ("CALL_007", "good", "Need identified and client agreed to proceed."),
        ("CALL_008", "good", "Serious buyer with clear budget."),
        ("CALL_010", "bad", "Early-stage research, no intent."),
        ("CALL_012", "good", "Strong discovery and confirmation."),
        ("CALL_014", "bad", "Client requested number removal."),
        ("CALL_016", "good", "Long call with clear buying intent."),
        ("CALL_018", "bad", "Call deferred, no engagement."),
    ]

    y_true: List[int] = []
    y_pred: List[int] = []

    threshold = 0.6

    for _, label, text in calls:
        out = analyze_call(text)
        y_true.append(1 if label == "good" else 0)
        y_pred.append(1 if out["quality_score"] >= threshold else 0)

    acc, f1 = accuracy_f1(y_pred, y_true)

    print("threshold:", threshold)
    print("accuracy:", acc)
    print("f1:", f1)


if __name__ == "__main__":
    run_eval()
