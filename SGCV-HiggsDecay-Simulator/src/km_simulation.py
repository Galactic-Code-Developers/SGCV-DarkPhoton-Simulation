import numpy as np

class KMSimulation:
    """
    Simulation class for Kaluza–Klein (KK) graviton events in extra-dimensional models.
    """
    def __init__(self, n_events=10000, compact_radius=1e-18, kk_mode=1, seed=None):
        """
        Initialize KK simulation.

        Parameters:
        - n_events: Number of events
        - compact_radius: Compactification radius [m]
        - kk_mode: Index of KK excitation
        - seed: Optional RNG seed
        """
        self.n_events = n_events
        self.compact_radius = compact_radius
        self.kk_mode = kk_mode
        self.rng = np.random.default_rng(seed)

    def generate_events(self):
        """
        Generate mock Δt and Δx data for KK model.

        Returns:
        - delta_x: Position deviations [mm]
        - delta_t: Time deviations [ns]
        """
        # KK graviton mass estimate
        m_kk = self.kk_mode / self.compact_radius  # in natural units (GeV/c^2 if radius in 1/GeV)

        # Assume subluminal propagation due to extra-dimensional detours
        beta = 0.999  # Slightly slower than c
        gamma = 1. / np.sqrt(1 - beta**2)

        # Simulated propagation delays
        propagation_time = self.rng.exponential(scale=1e-9, size=self.n_events)  # ~1 ns
        delta_x = beta * 3e11 * propagation_time * 1e-3  # [mm]
        delta_t = propagation_time * 1e9  # [ns]

        # Detector timing + geometry noise
        delta_x += self.rng.normal(0, 1.5, size=self.n_events)
        delta_t += self.rng.normal(0, 0.1, size=self.n_events)

        return delta_x, delta_t
