import pytest

from models.reseau import ReseauRoutier
from models.route import Route
from models.vehicule import Vehicule


@pytest.fixture
def route_simple():
	"""Fixture qui crée une route simple pour les tests."""
	return Route("A1", longueur=1000, limite_vitesse=30)


@pytest.fixture
def vehicule_exemple(route_simple):
	"""Fixture qui crée un véhicule placé sur `route_simple`."""
	return Vehicule("V1", route=route_simple, position=0, vitesse=10)


@pytest.fixture
def reseau_simple(route_simple, vehicule_exemple):
	"""Fixture qui crée un réseau contenant la route et le véhicule d'exemple."""
	reseau = ReseauRoutier()
	reseau.ajouter_route(route_simple)
	route_simple.ajouter_vehicule(vehicule_exemple)
	return reseau