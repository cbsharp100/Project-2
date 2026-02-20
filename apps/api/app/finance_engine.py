import numpy as np

def simulate_investment(
    start_age: int = 25,
    end_age: int = 65,
    monthly_contribution: float = 500.0,
    mean_return: float = 0.07,
    volatility: float = 0.15,
    simulations: int = 5000,
    seed: int = 42,
):
    """
    Simple Monte Carlo model (monthly normal returns).
    We'll upgrade to historical bootstrap + regime switching next.
    """
    rng = np.random.default_rng(seed)

    years = end_age - start_age
    months = years * 12

    results = np.empty(simulations, dtype=float)

    for i in range(simulations):
        value = 0.0
        for _ in range(months):
            r = rng.normal(mean_return / 12.0, volatility / np.sqrt(12.0))
            value = (value + monthly_contribution) * (1.0 + r)
        results[i] = value

    return {
        "mean": float(results.mean()),
        "median": float(np.median(results)),
        "p10": float(np.percentile(results, 10)),
        "p90": float(np.percentile(results, 90)),
        "std": float(results.std()),
    }

