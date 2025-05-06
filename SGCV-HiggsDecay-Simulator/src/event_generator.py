# event_generator.py
"""
Monte Carlo generator for Higgs → γγ and Higgs → γ + γ_DP decays.

Supports kinematic output for:
- Standard Model (SM): H → γγ
- SGCV (Superluminal Graviton Condensate Vacuum): H → γ + γ_DP

Author: Condor Simulation Project
"""

import numpy as np
import random

# Constants
HIGGS_MASS_GEV = 125.10
C_LIGHT = 299792458  # m/s

# Optional: set random seed for reproducibility
np.random.seed(42)


def generate_higgs_rest_frame_event(model="SM", dark_photon_mass=0.0):
    """
    Generate a Higgs decay event in its rest frame.
    - model: "SM" or "SGCV"
    - dark_photon_mass: non-zero mass for SGCV dark photon
    """
    if model == "SM":
        m1, m2 = 0.0, 0.0  # two photons
    elif model == "SGCV":
        m1, m2 = 0.0, dark_photon_mass  # photon and γ_DP
    else:
        raise ValueError("Unsupported model")

    E_H = HIGGS_MASS_GEV

    # Two-body decay kinematics
    E1 = (E_H**2 + m1**2 - m2**2) / (2 * E_H)
    E2 = (E_H**2 + m2**2 - m1**2) / (2 * E_H)

    p = np.sqrt(E1**2 - m1**2)

    # Random direction
    theta = np.arccos(2 * np.random.rand() - 1)
    phi = 2 * np.pi * np.random.rand()

    px = p * np.sin(theta) * np.cos(phi)
    py = p * np.sin(theta) * np.sin(phi)
    pz = p * np.cos(theta)

    # For photon 1 and photon 2 / γ_DP
    particle1 = {"E": E1, "px": px, "py": py, "pz": pz, "mass": m1}
    particle2 = {"E": E2, "px": -px, "py": -py, "pz": -pz, "mass": m2}

    return particle1, particle2


def generate_events(n_events=1000, model="SM", dark_photon_mass=0.0):
    """
    Generate a list of n_events with given decay model.
    """
    events = []
    for _ in range(n_events):
        p1, p2 = generate_higgs_rest_frame_event(model, dark_photon_mass)
        events.append((p1, p2))
    return events


def save_events_to_csv(events, filename):
    """
    Save event list to CSV file for later analysis or plotting.
    """
    import csv
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["E1", "px1", "py1", "pz1", "mass1", "E2", "px2", "py2", "pz2", "mass2"])
        for e1, e2 in events:
            row = [e1["E"], e1["px"], e1["py"], e1["pz"], e1["mass"],
                   e2["E"], e2["px"], e2["py"], e2["pz"], e2["mass"]]
            writer.writerow(row)


# Example usage (debug mode)
if __name__ == "__main__":
    n = 10
    model = "SGCV"
    mass_dp = 1.0  # GeV

    events = generate_events(n_events=n, model=model, dark_photon_mass=mass_dp)
    save_events_to_csv(events, f"events_{model}_{mass_dp:.1f}GeV.csv")
    print(f"[✓] {n} events generated and saved for model: {model}")
