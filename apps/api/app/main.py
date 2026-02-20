from fastapi import FastAPI
from app.finance_engine import simulate_investment
from app.schemas import ChatRequest, ChatResponse

app = FastAPI(title="Agentic Finance AI")

@app.get("/")
def home():
    return {"message": "Project 2 API running"}

@app.post("/simulate")
def run_simulation():
    result = simulate_investment()
    return result

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    message = req.message.lower()

    if "invest" in message or "start age" in message:
        sim = simulate_investment()

        answer = f"""
Monte Carlo simulation results:

Expected value: ${sim['mean']:,.0f}
Median outcome: ${sim['median']:,.0f}
Downside (10th percentile): ${sim['p10']:,.0f}
Upside (90th percentile): ${sim['p90']:,.0f}

This shows the distribution of outcomes rather than a single deterministic path.
"""

        return ChatResponse(answer=answer, sources=[], grounded=True)

    return ChatResponse(
        answer="Ask me about investing scenarios or probabilities.",
        sources=[],
        grounded=False
    )

