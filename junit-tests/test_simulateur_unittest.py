import unittest
import sys
import os
import json

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.simulateur import Simulateur


class TestSimulateur(unittest.TestCase):
    """Tests d'intégration pour la classe Simulateur."""

    def test_initialisation_a_partir_du_fichier_config(self):
        """Le simulateur doit charger les routes et véhicules depuis le JSON."""
        simu = Simulateur("data/config_reseau.json")
        # Routes attendues
        self.assertIn("R1", simu.reseau.routes)
        self.assertIn("R2", simu.reseau.routes)

        # Véhicules attendus (ids)
        ids = {v.id for route in simu.reseau.routes.values() for v in route.vehicules}
        self.assertIn("V1", ids)
        self.assertIn("V2", ids)

    def test_execution_simulation_plusieurs_tours(self):
        """Exécute la simulation plusieurs tours et vérifie que l'historique est rempli."""
        # Create a simulator and run a few steps
        simu = Simulateur("data/config_reseau.json")
        n_tours = 4
        delta_t = 5

        # Run simulation
        simu.lancer_simulation(n_tours=n_tours, delta_t=delta_t)

        # After running, historique should have n_tours snapshots
        self.assertEqual(len(simu.historique), n_tours)

        # The exporter created data/resultats.json by default; ensure it exists
        default_path = "data/resultats.json"
        self.assertTrue(os.path.exists(default_path))

        # Load and check basic structure
        with open(default_path, "r", encoding="utf-8") as f:
            stats = json.load(f)

        self.assertIsInstance(stats, dict)
        self.assertIn("nb_vehicules", stats)

        # Clean up the generated file to avoid side effects
        try:
            os.remove(default_path)
        except OSError:
            pass


if __name__ == '__main__':
    unittest.main()
