import unittest
import sys
import os

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.route import Route
from models.vehicule import Vehicule


class TestRoute(unittest.TestCase):
    """Tests unitaires pour la classe Route."""

    def test_ajout_de_vehicule(self):
        """L'ajout d'un véhicule à une route doit l'inscrire dans la liste."""
        route = Route("R_test", longueur=500, limite_vitesse=30)
        v = Vehicule("V1", route, position=0, vitesse=5)
        self.assertEqual(len(route.vehicules), 0)
        route.ajouter_vehicule(v)
        self.assertEqual(len(route.vehicules), 1)
        self.assertIs(route.vehicules[0], v)

    def test_mise_a_jour_avance_vehicules(self):
        """La mise à jour de la route doit appeler `avancer` sur chaque véhicule."""
        route = Route("R_update", longueur=200, limite_vitesse=20)
        v1 = Vehicule("V1", route, position=0, vitesse=10)
        v2 = Vehicule("V2", route, position=50, vitesse=2)
        route.ajouter_vehicule(v1)
        route.ajouter_vehicule(v2)

        route.mettre_a_jour_vehicules(delta_t=3)

        # v1: 0 + 10*3 = 30
        self.assertEqual(v1.position, 30)
        # v2: 50 + 2*3 = 56
        self.assertEqual(v2.position, 56)


if __name__ == '__main__':
    unittest.main()
