from models.route import Route
from models.vehicule import Vehicule


def test_avancement_modifie_position():
    route = Route("R_test", longueur=1000, limite_vitesse=50)
    v = Vehicule("V_test", route, position=0.0, vitesse=10.0)
    v.avancer(5)  # 5s * 10 m/s = 50
    assert v.position == 50.0


def test_ne_depasse_pas_longueur_route():
    route = Route("R_short", longueur=100, limite_vitesse=20)
    v = Vehicule("V_edge", route, position=95.0, vitesse=10.0)
    v.avancer(1)  # would be 105 but should cap at 100
    assert v.position == 100.0


def test_changement_de_route_reset_position():
    route1 = Route("R1", longueur=500, limite_vitesse=30)
    route2 = Route("R2", longueur=800, limite_vitesse=40)
    v = Vehicule("V_move", route1, position=123.0, vitesse=5.0)
    v.changer_de_route(route2)
    assert v.route is route2
    assert v.position == 0
