from models.reseau import ReseauRoutier
from models.route import Route
from models.vehicule import Vehicule


def test_ajout_de_routes_au_reseau():
    """L'ajout de routes au réseau doit les enregistrer dans `routes`."""
    reseau = ReseauRoutier()
    r1 = Route("R1", longueur=100, limite_vitesse=20)
    r2 = Route("R2", longueur=200, limite_vitesse=30)

    reseau.ajouter_route(r1)
    reseau.ajouter_route(r2)

    assert "R1" in reseau.routes
    assert "R2" in reseau.routes
    assert reseau.get_route("R1") is r1
    assert reseau.get_route("R2") is r2


def test_mise_a_jour_de_lensemble_des_routes():
    """La mise à jour de l'ensemble des routes avance les véhicules présents."""
    reseau = ReseauRoutier()
    r1 = Route("R1", longueur=1000, limite_vitesse=50)
    r2 = Route("R2", longueur=500, limite_vitesse=30)

    v1 = Vehicule("V1", r1, position=0, vitesse=10)
    v2 = Vehicule("V2", r2, position=100, vitesse=5)

    r1.ajouter_vehicule(v1)
    r2.ajouter_vehicule(v2)

    reseau.ajouter_route(r1)
    reseau.ajouter_route(r2)

    # Update all routes in the network (simulate what the simulator does)
    for route in reseau.routes.values():
        route.mettre_a_jour_vehicules(delta_t=2)

    assert v1.position == 20  # 0 + 10*2
    assert v2.position == 110  # 100 + 5*2
