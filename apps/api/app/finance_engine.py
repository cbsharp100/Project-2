import numpy as np

def simulate_investment(
    start_age=25,
    end_age=65,
    monthly_contribution=500,
    mean_return=0.07,
    volatility=0.15,
    simulations=5000
):
    years = end_age - start_age
    months = years * 12

    results = []

    for _ in range(simulations):
        value = 0
        for m in range(months):
            monthly_return = np.random.normal(mean_return/12, volatility/np.sqrt(12))
            value = (value + monthly_contribution) * (1 + monthly_return)
        results.append(value)

    arr = np.array(results)

    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "p10": float(np.percentile(arr, 10)),
        "p90": float(np.percentile(arr, 90)),
        "std": float(np.std(arr))
    }

