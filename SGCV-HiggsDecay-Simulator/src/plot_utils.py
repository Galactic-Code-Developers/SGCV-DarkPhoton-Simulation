import numpy as np
import matplotlib.pyplot as plt

def plot_delta_x_vs_delta_t(delta_x, delta_t, label='Model', color='blue'):
    """Plot Δx vs Δt for a given model."""
    plt.figure(figsize=(8, 6))
    plt.scatter(delta_t, delta_x, label=label, alpha=0.6, edgecolors='k', color=color)
    plt.xlabel('Δt [ns]')
    plt.ylabel('Δx [mm]')
    plt.title('Δx vs Δt')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_histogram(data, bins=50, label='Model', xlabel='Value', color='blue'):
    """Generic histogram plotter."""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, alpha=0.7, label=label, color=color, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel('Counts')
    plt.title(f'{xlabel} Distribution')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def compare_models_histograms(data_dict, bins=50, xlabel='Δt [ns]'):
    """Compare histograms for multiple models."""
    plt.figure(figsize=(10, 6))
    for label, (data, color) in data_dict.items():
        plt.hist(data, bins=bins, alpha=0.5, label=label, color=color, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel('Counts')
    plt.title(f'Comparative Histogram: {xlabel}')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
