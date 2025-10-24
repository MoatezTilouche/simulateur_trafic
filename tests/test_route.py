from models.route import Route
from models.vehicule import Vehicule


def test_ajout_de_vehicule():
	"""L'ajout d'un véhicule à une route doit l'inscrire dans la liste."""
	route = Route("R_test", longueur=500, limite_vitesse=30)
	v = Vehicule("V1", route, position=0, vitesse=5)
	assert len(route.vehicules) == 0
	route.ajouter_vehicule(v)
	assert len(route.vehicules) == 1
	assert route.vehicules[0] is v


def test_mise_a_jour_avance_vehicules():
	"""La mise à jour de la route doit appeler `avancer` sur chaque véhicule."""
	route = Route("R_update", longueur=200, limite_vitesse=20)
	v1 = Vehicule("V1", route, position=0, vitesse=10)
	v2 = Vehicule("V2", route, position=50, vitesse=2)
	route.ajouter_vehicule(v1)
	route.ajouter_vehicule(v2)

	route.mettre_a_jour_vehicules(delta_t=3)

	# v1: 0 + 10*3 = 30
	assert v1.position == 30
	# v2: 50 + 2*3 = 56
	assert v2.position == 56

