from src.schemas.lead import LeadIn, LeadOut
from src.llm.local_model import classify_note_intent


def score_lead(lead: LeadIn) -> LeadOut:
    score = 0.0
    reasons = []
 
    if lead.last_activity_minutes_ago < 30:
        score += 0.25
        reasons.append("recent activity")

    if lead.budget >= 7_500_000:
        score += 0.25
        reasons.append("high budget")

    if lead.past_interactions >= 3:
        score += 0.15
        reasons.append("multiple interactions")

    
    intent = classify_note_intent(lead.notes)

    if intent == "urgent":
        score += 0.25
        reasons.append("urgent intent from notes")
    elif intent == "soft":
        score += 0.10
        reasons.append("mild interest from notes")

    score = min(score, 1.0)

    if score >= 0.7:
        bucket = "hot"
    elif score >= 0.4:
        bucket = "warm"
    else:
        bucket = "cold"

    return LeadOut(
        lead_id=lead.lead_id,
        priority_score=round(score, 3),
        priority_bucket=bucket,
        reasons=reasons,
    )
