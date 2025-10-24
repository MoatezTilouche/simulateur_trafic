"""Script d'exécution du simulateur.

Exécuter ce fichier pour lancer une simulation à partir de
`data/config_reseau.json`.
"""

from core.simulateur import Simulateur


if __name__ == "__main__":
    simu = Simulateur("data/config_reseau.json")
    simu.lancer_simulation(n_tours=10, delta_t=10)
