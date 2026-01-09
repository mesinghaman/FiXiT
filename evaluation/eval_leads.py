import csv
from typing import List

import numpy as np

from src.core.lead_scoring import score_lead
from src.schemas.lead import LeadIn


BUCKET_MAP = {"cold": 0, "warm": 1, "hot": 2}


def load_leads(path: str) -> List[LeadIn]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(
                LeadIn(
                    lead_id=r["lead_id"],
                    source=r["source"],
                    budget=float(r["budget"]),
                    city=r["city"],
                    property_type=r["property_type"],
                    last_activity_minutes_ago=int(
                        r["last_activity_minutes_ago"]
                    ),
                    past_interactions=int(r["past_interactions"]),
                    notes=r["notes"],
                    status=r["status"],
                )
            )
    return rows


def precision_recall_hot(pred: List[str], truth: List[str]) -> tuple[float, float]:
    tp = sum(p == "hot" and t == "hot" for p, t in zip(pred, truth))
    fp = sum(p == "hot" and t != "hot" for p, t in zip(pred, truth))
    fn = sum(p != "hot" and t == "hot" for p, t in zip(pred, truth))

    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return round(precision, 3), round(recall, 3)


def run_eval() -> None:
    leads = load_leads("data/leads_eval_20.csv")

    preds = []
    scores = []
    truth = []

    for l in leads:
        out = score_lead(l)
        preds.append(out.priority_bucket)
        scores.append(out.priority_score)
        truth.append(l.status)  

    precision, recall = precision_recall_hot(preds, truth)

    bucket_nums = [BUCKET_MAP[b] for b in preds]
    corr = float(np.corrcoef(scores, bucket_nums)[0, 1])

    print("precision_hot:", precision)
    print("recall_hot:", recall)
    print("score_bucket_correlation:", round(corr, 3))


if __name__ == "__main__":
    run_eval()
