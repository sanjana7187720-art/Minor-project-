from fastapi import FastAPI
from main import run_risk_prioritization

app = FastAPI()

@app.get("/risk-prioritization")
def get_risk_prioritization():

    results = run_risk_prioritization()

    return {
        "feature": "Risk Based Prioritization",
        "results": results
    }