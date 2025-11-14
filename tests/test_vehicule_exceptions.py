import pytest

from models.route import Route
from models.vehicule import Vehicule
from exceptions import VitesseNegativeException, PositionInvalideException


def test_init_vitesse_negative_raises():
    route = Route("R1", longueur=100, limite_vitesse=50)
    with pytest.raises(VitesseNegativeException):
        Vehicule("V_neg", route, position=0, vitesse=-5)


def test_init_position_negative_raises():
    route = Route("R1", longueur=100, limite_vitesse=50)
    with pytest.raises(PositionInvalideException):
        Vehicule("V_pos", route, position=-1, vitesse=5)


def test_avancer_avec_vitesse_negative_raises():
    route = Route("R1", longueur=100, limite_vitesse=50)
    v = Vehicule("V1", route, position=10, vitesse=5)
    v.vitesse = -3
    with pytest.raises(VitesseNegativeException):
        v.avancer(1)


def test_avancer_type_error_raises_position_invalide():
    route = Route("R1", longueur=100, limite_vitesse=50)
    v = Vehicule("V2", route, position=10, vitesse=5)
    # set a non-numeric speed to trigger an unexpected exception inside avancer
    v.vitesse = "fast"
    with pytest.raises(PositionInvalideException):
        v.avancer(1)
