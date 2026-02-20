from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import ChatRequest, ChatResponse
from app.finance_engine import simulate_investment

app = FastAPI(title="MGMT 690 Project 2: Agentic Finance")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Project 2 API running"}

@app.post("/simulate")
def simulate():
    return simulate_investment()

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    q = req.message.lower()

    if any(k in q for k in ["invest", "retire", "start age", "401k", "ira", "million", "probability", "monte carlo"]):
        sim = simulate_investment()
        answer = (
            "Monte Carlo simulation results (stochastic outcomes):\n\n"
            f"- Expected final value: ${sim['mean']:,.0f}\n"
            f"- Median final value: ${sim['median']:,.0f}\n"
            f"- 10th percentile (downside): ${sim['p10']:,.0f}\n"
            f"- 90th percentile (upside): ${sim['p90']:,.0f}\n"
            f"- Std dev (dispersion): ${sim['std']:,.0f}\n\n"
            "This replaces a single deterministic path with a distribution of outcomes."
        )
        return ChatResponse(answer=answer, sources=[], grounded=True)

    return ChatResponse(
        answer="Ask about investing outcomes (start age, volatility, probability of reaching $1M).",
        sources=[],
        grounded=False,
    )


