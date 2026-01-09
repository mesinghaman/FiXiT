from fastapi import FastAPI

from src.api.lead_priority import router as lead_router
from src.api.call_eval import router as call_router

app = FastAPI(title="FiXiT")

@app.get("/")
def root():
    return {"message": "FiXiT API is running"}

app.include_router(lead_router)
app.include_router(call_router)
