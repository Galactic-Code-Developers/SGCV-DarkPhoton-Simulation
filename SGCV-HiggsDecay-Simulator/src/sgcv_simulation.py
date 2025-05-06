# sgcv_simulation.py

"""
SGCV GEANT4-based Simulation Core

This module sets up a GEANT4-based simulation environment to model
superluminal dark photon (γ_DP) production and propagation under
the Superluminal Graviton Condensate Vacuum (SGCV) hypothesis.

Authors: Valamontes, John Karantonis (2025)
Version: 1.0.0
"""

import numpy as np

# If using g4py (GEANT4 Python bindings), import required GEANT4 modules
try:
    import Geant4 as g4
except ImportError:
    raise ImportError("GEANT4 Python bindings not found. Install g4py or pygeant4.")

# === Constants ===
LIGHT_SPEED = 299792458  # [m/s]
SGCV_SUPERLUMINAL_FACTOR = 1.05  # 5% faster than light in vacuum

# === Core simulation classes ===

class SGCVDetectorConstruction(g4.G4VUserDetectorConstruction):
    def __init__(self):
        super().__init__()

    def Construct(self):
        # Define world volume (vacuum box)
        world_solid = g4.G4Box("World", 1*m, 1*m, 1*m)
        world_logic = g4.G4LogicalVolume(world_solid, g4.G4Material.GetMaterial("G4_Galactic"), "World")
        world_phys = g4.G4PVPlacement(None, g4.G4ThreeVector(), world_logic, "World", None, False, 0)
        return world_phys


class SGCVPrimaryGenerator(g4.G4VUserPrimaryGeneratorAction):
    def __init__(self):
        super().__init__()
        self.particleGun = g4.G4ParticleGun(1)
        particle = g4.G4ParticleTable.GetParticleTable().FindParticle("gamma")
        self.particleGun.SetParticleDefinition(particle)
        self.particleGun.SetParticleMomentumDirection(g4.G4ThreeVector(0., 0., 1.))
        self.particleGun.SetParticleEnergy(1.0 * g4.GeV)

    def GeneratePrimaries(self, event):
        self.particleGun.GeneratePrimaryVertex(event)


class SGCVRunAction(g4.G4UserRunAction):
    def BeginOfRunAction(self, run):
        print("[SGCV Simulation] Begin Run")

    def EndOfRunAction(self, run):
        print("[SGCV Simulation] End Run")


def simulate_sgcv_event(num_events=1000, superluminal=True):
    """
    Run SGCV-based simulation with optional superluminal propagation.

    Args:
        num_events (int): Number of events to simulate.
        superluminal (bool): If True, apply SGCV superluminal propagation.

    Returns:
        list of (Δx, Δt) tuples per event.
    """
    delta_x_dt_data = []

    for _ in range(num_events):
        path_length = np.random.normal(loc=1.0, scale=0.01)  # meters
        velocity = SGCV_SUPERLUMINAL_FACTOR * LIGHT_SPEED if superluminal else LIGHT_SPEED
        delta_t = path_length / velocity
        delta_x_dt_data.append((path_length, delta_t))

    return delta_x_dt_data
