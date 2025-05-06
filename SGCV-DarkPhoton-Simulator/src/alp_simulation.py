import numpy as np

class ALPSimulation:
    """
    Simulation class for Axion-Like Particle (ALP) model events.
    """
    def __init__(self, n_events=10000, mass_alp=1e-3, coupling_alp=1e-4, seed=None):
        """
        Initialize the ALP simulation.

        Parameters:
        - n_events: Number of simulated events
        - mass_alp: ALP mass [GeV]
        - coupling_alp: ALP-photon coupling constant
        - seed: Optional random seed for reproducibility
        """
        self.n_events = n_events
        self.mass_alp = mass_alp
        self.coupling_alp = coupling_alp
        self.rng = np.random.default_rng(seed)

    def generate_events(self):
        """
        Generate mock Δt and Δx data based on ALP propagation and interaction.

        Returns:
        - delta_x: Position deviations [mm]
        - delta_t: Time deviations [ns]
        """
        # Assume Lorentz-boosted propagation and delayed decay
        beta = 0.9999  # close to c
        gamma = 1. / np.sqrt(1 - beta**2)

        # Simulate decay time and location in lab frame
        proper_lifetime = self.rng.exponential(scale=1e-10, size=self.n_events)  # ~100 ps
        lab_lifetime = proper_lifetime * gamma
        delta_x = beta * 3e11 * lab_lifetime * 1e-3  # [mm] (3e11 mm/s)
        delta_t = lab_lifetime * 1e9  # [ns]

        # Add detector resolution noise
        delta_x += self.rng.normal(0, 1.0, size=self.n_events)  # mm
        delta_t += self.rng.normal(0, 0.05, size=self.n_events)  # ns

        return delta_x, delta_t
