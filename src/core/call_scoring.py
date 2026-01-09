import time
import logging

from src.schemas.call import CallEvalIn, CallEvalOut
from src.llm.call_model import analyze_call

log = logging.getLogger(__name__)


def run_call_eval(data: CallEvalIn) -> CallEvalOut:
    started = time.time()
    size = len(data.transcript)

    try:
        result = analyze_call(data.transcript)
    except Exception as exc:
        log.error("call_eval_failed", exc_info=exc)
        raise

    took = round(time.time() - started, 3)

    log.info(
        "call_eval_done",
        extra={"latency": took, "chars": size},
    )

    return CallEvalOut(
        quality_score=result["quality_score"],
        labels=result["labels"],
        summary=result["summary"],
        next_actions=result["next_actions"],
        model_metadata={
            "model_name": result["model"],
            "latency": took,
        },
    )
