from models.feu_rouge import FeuRouge


def test_cycle_du_feu():
    """Le feu doit parcourir les états rouge -> vert -> orange -> rouge en étapes."""
    feu = FeuRouge(cycle=1)
    assert feu.etat == 'rouge'
    feu.avancer_temps(1)
    assert feu.etat == 'vert'
    feu.avancer_temps(1)
    assert feu.etat == 'orange'
    feu.avancer_temps(1)
    assert feu.etat == 'rouge'
