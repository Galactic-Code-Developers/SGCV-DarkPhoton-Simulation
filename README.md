# SGCV Dark Photon Simulation Toolkit

A simulation framework for modeling exotic Higgs decay events involving superluminal dark photons, based on the Superluminal Graviton Condensate Vacuum (SGCV) model. This tool is designed to assess Time-of-Flight (ToF) anomalies and spatial origin displacements in high-energy collider environments, such as ATLAS or SHiP.

---

## 📘 Overview

This project implements a theoretical particle simulation to test predictions from the SGCV framework:

```
H → γ_DP → γ
```

Where:
- $\gamma_{	ext{DP}}$ : a transient dark photon traveling at $v > c$,
- which converts into a Standard Model photon inside the detector,
- producing measurable $\Delta t$ and $\Delta x$ anomalies.

---

## 🛠 Features

- GEANT4-compatible Monte Carlo event modeling
- Adjustable dark photon velocities and path segments
- High-precision ToF tracking and vertex displacement analysis
- Configurable detector smearing and resolution parameters
- Google Colab compatibility for rapid execution and visualization

---

## 📁 Repository Structure

```
SGCV-Simulation/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── SGCV-DarkPhoton-Simulator/
│   ├── simulate_tof_anomalies.py         # Main simulation engine
│   └── SGCV_DarkPhoton_Colab.ipynb       # Google Colab version
│   └── src/
│       ├── __init__.py
│       ├── sgcv_simulation.py         <-- Core GEANT4-based simulation code
│       ├── detector_geometry.gdml     <-- Simplified geometry for ATLAS/SHiP
│       ├── event_generator.py         <-- Higgs → γγ + dark photon MC generation
│       └── plot_utils.py              <-- Helper functions to visualize Δt, Δx
├──  data/
│       └── example_results.csv        <-- Example Δt, Δx outputs
├──  docs/
│    └── SGCV_Simulation_Manual.pdf <-- Short user manual + figure explanations
│    └──  figures/
│         ├── tof_anomaly_example.png   # Pending Reseale
│         ├── graviton_arc_diagram.png  # Pending Reseale
│         └── bullet_analogy.png        # Pending Reseale
├── SGCV-HiggsDecay-Simulator/
├── CMakeLists.txt
├── README.md
│   └── src/
│       ├── DetectorConstruction.cc
│       ├── PrimaryGeneratorAction.cc
│       ├── PhysicsList.cc
│       ├── EventAction.cc
│       ├── RunAction.cc
│       ├── SteppingAction.cc
│       ├── SGCVPhysicsExtension.cc  // Custom superluminal DP handling
├────── include/
│       ├── DetectorConstruction.hh
│       ├── PrimaryGeneratorAction.hh
│       ├── PhysicsList.hh
│       ├── EventAction.hh
│       ├── RunAction.hh
│       ├── SteppingAction.hh
│       ├── SGCVPhysicsExtension.hh
├────── macros/
│       └── run.mac
└────── data/
        └── output.root
```

---

## 🚀 Quick Start

### 🔧 Local Python Setup

Install required packages:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python simulate_tof_anomalies.py
```

### 🧪 Google Colab

Launch the ready-to-run notebook:

[🔗 SGCV_DarkPhoton_Colab.ipynb](./SGCV_DarkPhoton_Colab.ipynb) 'Pending Update'

Includes:
- Preloaded parameters for SGCV validation
- Visualization of $\Delta t$ histograms and scatter plots

---

## 📊 Output Examples

The simulation produces:
- Histograms of time anomalies ($\Delta t$)
- Scatter plots of photon origin displacements ($\Delta x$)
- Statistical comparison to Standard Model baselines

All plots can be saved as PNG/PDF for use in research figures or papers.

---

## 🧠 Theory Background

This simulator is based on the paper:

**"Investigating Superluminal Dark Photons and Their Influence on Higgs Boson Decay Through Time-of-Flight Anomalies
"**  
- DOI: 10.13140/RG.2.2.35920.52488
- *Antonios Valamontes, 2025*

**"Experiment for the detection of superluminal propagating dark photons at CERN and their correlation with gravitons and the Higgs Boson H→γγ decay event
"**  
- DOI: 10.13140/RG.2.2.35357.83688
- *Emmanouil N. Markoulakis and Antonios Valamontes, 2025*


It models how displaced vacuum gravitons (in the SGCV model) produce dark photon intermediaries that travel superluminally, leading to detectable collider anomalies.

---

## 🤝 Acknowledgments

- No formal collaboration with ATLAS/SHiP exists at this time.
- The authors welcome scientific dialogue, replication, and code validation efforts.

---

## 📬 Contact

- Antonios Valamontes — [avalamontes@kapodistrian.edu.gr](mailto:avalamontes@kapodistrian.edu.gr)
- John Karantonis — [jkarantonis@kapodistrian.edu.gr](mailto:jkarantonis@kapodistrian.edu.gr)
---

## 📄 License

This project is licensed under the terms of the MIT License.  
See [LICENSE](./LICENSE) for full details.
