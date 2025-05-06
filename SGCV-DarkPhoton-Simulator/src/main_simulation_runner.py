from sgcv_simulation import SGCVSimulation
from alp_simulation import ALPSimulation
from km_simulation import KMSimulation
from plot_utils import compare_models_histograms, plot_scatter_dt_dx

import matplotlib.pyplot as plt

def run_all_simulations(n_events=10000, seed=42):
    # Initialize models
    sgcv = SGCVSimulation(n_events=n_events, seed=seed)
    alp = ALPSimulation(n_events=n_events, seed=seed)
    km = KMSimulation(n_events=n_events, seed=seed)

    # Generate Δx, Δt for each model
    dx_sgcv, dt_sgcv = sgcv.generate_events()
    dx_alp, dt_alp = alp.generate_events()
    dx_km, dt_km = km.generate_events()

    # Combine results into dictionary for plotting
    all_data = {
        "SGCV": {"Δx": dx_sgcv, "Δt": dt_sgcv},
        "ALP": {"Δx": dx_alp, "Δt": dt_alp},
        "KM": {"Δx": dx_km, "Δt": dt_km}
    }

    # Plot histograms
    compare_models_histograms(all_data)

    # Optional: Scatter plot of Δt vs Δx for qualitative view
    plt.figure(figsize=(16, 4))
    for i, model in enumerate(all_data, 1):
        plt.subplot(1, 3, i)
        plot_scatter_dt_dx(all_data[model]['Δx'], all_data[model]['Δt'], label=model)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_all_simulations()
