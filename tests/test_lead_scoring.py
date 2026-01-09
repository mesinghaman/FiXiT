from src.core.lead_scoring import score_lead
from src.schemas.lead import LeadIn


def test_hot_lead_scores_high() -> None:
    lead = LeadIn(
        lead_id="L-test-1",
        source="website",
        budget=9_000_000,
        city="Mumbai",
        property_type="apartment",
        last_activity_minutes_ago=10,
        past_interactions=4,
        notes="Client wants to close this week, sounds urgent",
        status="contacted",
    )

    out = score_lead(lead)

    assert out.priority_bucket == "hot"
    assert out.priority_score >= 0.7
    assert "urgent intent from notes" in out.reasons


def test_cold_lead_scores_low() -> None:
    lead = LeadIn(
        lead_id="L-test-2",
        source="portal",
        budget=3_000_000,
        city="Pune",
        property_type="plot",
        last_activity_minutes_ago=500,
        past_interactions=0,
        notes="Just browsing, checking options",
        status="new",
    )

    out = score_lead(lead)

    assert out.priority_bucket == "cold"
    assert out.priority_score < 0.4
