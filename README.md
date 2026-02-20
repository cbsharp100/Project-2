# MGMT 690 Project 2 – Agentic Finance AI

## Overview

This project is an intelligent financial assistant that uses Monte Carlo simulation to evaluate long-term investment decisions.

The system accepts natural language questions (e.g., start age, monthly investment) and returns probabilistic outcomes such as expected wealth, downside risk, and upside potential.

## Features

* Chat-based UI (Next.js)
* FastAPI backend
* Monte Carlo investment simulation
* Scenario comparisons:

  * Starting age (25 vs 35)
  * Monthly contributions ($300 vs $500)
  * Goal targeting (reach $1M by retirement)
* Risk metrics:

  * mean
  * median
  * 10th percentile (downside)
  * 90th percentile (upside)
  * standard deviation

## Example Questions

* What happens if I start investing at 35 instead of 25?
* What if I invest $300/month instead of $500?
* How much do I need to invest at 25 to reach $1M by age 60?

## How to Run

### Backend

cd apps/api
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001

### Frontend

cd apps/web
npm install
npm run dev

Open:
http://localhost:3000

## Architecture

Frontend: Next.js
Backend: FastAPI
Modeling: Python Monte Carlo simulation

## Author

Charlie Sharp
