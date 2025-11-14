from models.route import Route
from models.vehicule import Vehicule
from models.feu_rouge import FeuRouge


def test_arret_au_feu_rouge():
    """Vérifie qu'un véhicule s'arrête devant un feu rouge et que sa vitesse devient 0."""
    route = Route("R_test_feu", longueur=100, limite_vitesse=50)
    feu = FeuRouge(cycle=10)
    # position du feu à 50m
    route.ajouter_feu_rouge(feu, position=50)

    # véhicule proche du feu, qui dépasserait le feu en 1s
    v = Vehicule("V1", route, position=48, vitesse=5)
    route.ajouter_vehicule(v)

    # le feu est rouge par défaut -> le véhicule doit s'arrêter avant la position 50
    route.mettre_a_jour_vehicules(delta_t=1)

    assert v.position < 50
    # on attend que la position soit juste avant le feu (50 - 1 selon implémentation)
    assert v.position == 49 or v.position == 49.0
    assert v.vitesse == 0.0


def test_ajouter_feu_rouge_default_position():
    route = Route("R_default", longueur=120, limite_vitesse=50)
    from models.feu_rouge import FeuRouge

    feu = FeuRouge(cycle=10)
    route.ajouter_feu_rouge(feu)
    assert route.position_feu == 60


def test_vehicule_traverse_sur_feu_vert():
    route = Route("R_green", longueur=100, limite_vitesse=50)
    from models.feu_rouge import FeuRouge

    feu = FeuRouge(cycle=10)
    # advance to green state
    feu.avancer_temps(10)
    route.ajouter_feu_rouge(feu, position=50)

    v = Vehicule("Vpass", route, position=48, vitesse=5)
    route.ajouter_vehicule(v)

    route.mettre_a_jour_vehicules(delta_t=1)
    # should have passed the light (position >= 50)
    assert v.position >= 50
