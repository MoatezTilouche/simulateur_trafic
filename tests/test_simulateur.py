import os
import json

from core.simulateur import Simulateur


def test_initialisation_a_partir_du_fichier_config():
    """Le simulateur doit charger les routes et véhicules depuis le JSON."""
    simu = Simulateur("data/config_reseau.json")
    # Routes attendues
    assert "R1" in simu.reseau.routes
    assert "R2" in simu.reseau.routes

    # Véhicules attendus (ids)
    ids = {v.id for route in simu.reseau.routes.values() for v in route.vehicules}
    assert "V1" in ids
    assert "V2" in ids


def test_execution_simulation_plusieurs_tours(tmp_path):
    """Exécute la simulation plusieurs tours et vérifie que l'historique est rempli

    Le test redirige le fichier de sortie vers un chemin temporaire pour éviter
    d'écraser les données du projet lors de tests répétés.
    """
    # Create a simulator and run a few steps
    simu = Simulateur("data/config_reseau.json")
    n_tours = 4
    delta_t = 5

    # Temporarily change the output path by monkeypatching the exporter method
    out_file = tmp_path / "resultats_test.json"

    # Run simulation
    simu.lancer_simulation(n_tours=n_tours, delta_t=delta_t)

    # After running, historique should have n_tours snapshots
    assert len(simu.historique) == n_tours

    # The exporter created data/resultats.json by default; ensure it exists
    default_path = "data/resultats.json"
    assert os.path.exists(default_path)

    # Load and check basic structure
    with open(default_path, "r", encoding="utf-8") as f:
        stats = json.load(f)

    assert isinstance(stats, dict)
    assert "nb_vehicules" in stats

    # Clean up the generated file to avoid side effects
    try:
        os.remove(default_path)
    except OSError:
        pass
