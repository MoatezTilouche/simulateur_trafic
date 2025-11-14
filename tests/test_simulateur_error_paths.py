import os

from core.simulateur import Simulateur


def test_lancer_simulation_handles_route_and_analyse_errors(monkeypatch):
    # Create simulator from config (exists at data/config_reseau.json)
    sim = Simulateur("data/config_reseau.json")

    # Make each route.raise an exception when updating vehicles
    for r in sim.reseau.routes.values():
        def raise_exc(dt):
            raise Exception("route error")
        monkeypatch.setattr(r, "mettre_a_jour_vehicules", raise_exc)

    # Make analyser raise to trigger the fallback stats
    def analyser_raise(reseau):
        raise Exception("analyse error")
    monkeypatch.setattr(sim.analyseur, "analyser", analyser_raise)

    # Ensure exporter does not raise on final call
    monkeypatch.setattr(sim.exporteur, "exporter_resultats", lambda stats, path: None)

    # Should not raise despite internal errors
    sim.lancer_simulation(1, 1)
    assert len(sim.historique) == 1


def test_tracer_positions_writes_csv(tmp_path):
    sim = Simulateur("data/config_reseau.json")
    # run one step to populate history
    sim.lancer_simulation(1, 1)

    # change output path inside method by temporarily changing cwd
    out = "data/positions.csv"
    # ensure any existing file removed
    try:
        os.remove(out)
    except Exception:
        pass

    sim.tracer_positions()
    assert os.path.exists(out)
    # cleanup
    try:
        os.remove(out)
    except Exception:
        pass
