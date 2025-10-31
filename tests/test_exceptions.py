"""
Tests unitaires pour les exceptions personnalisées du simulateur.

Ce fichier teste que toutes les exceptions sont levées correctement
dans les différents cas d'erreur.
"""

import pytest
import sys
import os

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.vehicule import Vehicule
from models.route import Route
from models.reseau import ReseauRoutier
from core.simulateur import Simulateur
from core.analyseur import Analyseur

from exceptions import (
    VitesseNegativeException,
    PositionInvalideException,
    RoutePleineException,
    VehiculeDejaPresent,
    RouteInexistanteException,
    LongueurRouteInvalideException,
    FichierConfigurationException,
    IterationsInvalidesException,
    DivisionParZeroException,
    DonneesMaquantesException,
    RouteVideException
)


class TestVehiculeExceptions:
    """Tests des exceptions liées aux véhicules."""
    
    def test_vitesse_negative_leve_exception(self):
        """Teste qu'une vitesse négative lève VitesseNegativeException."""
        route = Route("R1", longueur=1000, limite_vitesse=50)
        
        with pytest.raises(VitesseNegativeException) as exc_info:
            Vehicule("V1", route, position=0, vitesse=-10)
        
        assert exc_info.value.vitesse == -10
        assert exc_info.value.vehicule_id == "V1"
        assert exc_info.value.code == "VEH001"
    
    def test_position_negative_leve_exception(self):
        """Teste qu'une position négative lève PositionInvalideException."""
        route = Route("R1", longueur=1000, limite_vitesse=50)
        
        with pytest.raises(PositionInvalideException) as exc_info:
            Vehicule("V1", route, position=-50, vitesse=10)
        
        assert exc_info.value.position == -50
        assert exc_info.value.code == "VEH002"
    
    def test_position_superieure_longueur_route_leve_exception(self):
        """Teste qu'une position > longueur route lève PositionInvalideException."""
        route = Route("R1", longueur=1000, limite_vitesse=50)
        
        with pytest.raises(PositionInvalideException) as exc_info:
            Vehicule("V1", route, position=1500, vitesse=10)
        
        assert exc_info.value.position == 1500
        assert exc_info.value.position_max == 1000


class TestRouteExceptions:
    """Tests des exceptions liées aux routes."""
    
    def test_longueur_nulle_leve_exception(self):
        """Teste qu'une longueur nulle lève LongueurRouteInvalideException."""
        with pytest.raises(LongueurRouteInvalideException) as exc_info:
            Route("R1", longueur=0, limite_vitesse=50)
        
        assert exc_info.value.longueur == 0
        assert exc_info.value.route_id == "R1"
        assert exc_info.value.code == "RTE004"
    
    def test_longueur_negative_leve_exception(self):
        """Teste qu'une longueur négative lève LongueurRouteInvalideException."""
        with pytest.raises(LongueurRouteInvalideException):
            Route("R1", longueur=-500, limite_vitesse=50)
    
    def test_route_pleine_leve_exception(self):
        """Teste qu'ajouter un véhicule à une route pleine lève RoutePleineException."""
        route = Route("R1", longueur=1000, limite_vitesse=50, capacite_max=2)
        
        # Ajouter 2 véhicules (capacité max)
        v1 = Vehicule("V1", route, 0, 10)
        v2 = Vehicule("V2", route, 100, 10)
        route.ajouter_vehicule(v1)
        route.ajouter_vehicule(v2)
        
        # Tenter d'ajouter un 3ème véhicule
        v3 = Vehicule("V3", route, 200, 10)
        with pytest.raises(RoutePleineException) as exc_info:
            route.ajouter_vehicule(v3)
        
        assert exc_info.value.route_id == "R1"
        assert exc_info.value.capacite_max == 2
        assert exc_info.value.code == "RTE001"
    
    def test_vehicule_deja_present_leve_exception(self):
        """Teste qu'ajouter deux fois le même véhicule lève VehiculeDejaPresent."""
        route = Route("R1", longueur=1000, limite_vitesse=50)
        vehicule = Vehicule("V1", route, 0, 10)
        
        route.ajouter_vehicule(vehicule)
        
        with pytest.raises(VehiculeDejaPresent) as exc_info:
            route.ajouter_vehicule(vehicule)
        
        assert exc_info.value.vehicule_id == "V1"
        assert exc_info.value.route_id == "R1"
        assert exc_info.value.code == "RTE002"


class TestReseauExceptions:
    """Tests des exceptions liées au réseau routier."""
    
    def test_route_inexistante_leve_exception(self):
        """Teste qu'accéder à une route inexistante lève RouteInexistanteException."""
        reseau = ReseauRoutier()
        route1 = Route("R1", 1000, 50)
        route2 = Route("R2", 1500, 60)
        reseau.ajouter_route(route1)
        reseau.ajouter_route(route2)
        
        with pytest.raises(RouteInexistanteException) as exc_info:
            reseau.get_route("R999")
        
        assert exc_info.value.route_id == "R999"
        assert "R1" in exc_info.value.routes_disponibles
        assert "R2" in exc_info.value.routes_disponibles
        assert exc_info.value.code == "RTE003"


class TestSimulateurExceptions:
    """Tests des exceptions liées au simulateur."""
    
    def test_fichier_config_inexistant_leve_exception(self):
        """Teste qu'un fichier de config inexistant lève FichierConfigurationException."""
        with pytest.raises(FichierConfigurationException) as exc_info:
            Simulateur("fichier_inexistant.json")
        
        assert exc_info.value.code == "SIM001"
        assert "fichier_inexistant.json" in str(exc_info.value)
    
    def test_iterations_negatives_leve_exception(self):
        """Teste qu'un nombre d'itérations négatif lève IterationsInvalidesException."""
        # Créer un simulateur avec une config valide
        sim = Simulateur("data/config_reseau.json")
        
        with pytest.raises(IterationsInvalidesException) as exc_info:
            sim.lancer_simulation(n_tours=-10, delta_t=1.0)
        
        assert exc_info.value.iterations == -10
        assert exc_info.value.code == "SIM002"
    
    def test_iterations_zero_leve_exception(self):
        """Teste qu'un nombre d'itérations nul lève IterationsInvalidesException."""
        sim = Simulateur("data/config_reseau.json")
        
        with pytest.raises(IterationsInvalidesException):
            sim.lancer_simulation(n_tours=0, delta_t=1.0)
    
    def test_delta_t_negatif_leve_exception(self):
        """Teste qu'un delta_t négatif lève ValueError."""
        sim = Simulateur("data/config_reseau.json")
        
        with pytest.raises(ValueError) as exc_info:
            sim.lancer_simulation(n_tours=10, delta_t=-1.0)
        
        assert "delta_t" in str(exc_info.value).lower()


class TestAnalyseurExceptions:
    """Tests des exceptions liées à l'analyseur."""
    
    def test_reseau_vide_leve_exception(self):
        """Teste qu'analyser un réseau vide lève DonneesMaquantesException."""
        analyseur = Analyseur()
        reseau = ReseauRoutier()  # Réseau sans routes
        
        with pytest.raises(DonneesMaquantesException) as exc_info:
            analyseur.analyser(reseau)
        
        assert exc_info.value.code == "ANA002"
    
    def test_reseau_none_leve_exception(self):
        """Teste qu'analyser None lève DonneesMaquantesException."""
        analyseur = Analyseur()
        
        with pytest.raises(DonneesMaquantesException):
            analyseur.analyser(None)


class TestMessagesExceptions:
    """Tests des messages d'erreur des exceptions."""
    
    def test_message_vitesse_negative_contient_info(self):
        """Teste que le message VitesseNegativeException contient les infos utiles."""
        route = Route("R1", 1000, 50)
        
        try:
            Vehicule("V1", route, 0, -15.5)
        except VitesseNegativeException as e:
            message = str(e)
            assert "V1" in message
            assert "-15.5" in message or "15.5" in message
            assert "VEH001" in str(e)
    
    def test_message_route_pleine_contient_capacite(self):
        """Teste que le message RoutePleineException contient la capacité."""
        route = Route("R1", 1000, 50, capacite_max=5)
        
        # Remplir la route
        for i in range(5):
            route.ajouter_vehicule(Vehicule(f"V{i}", route, i*100, 10))
        
        try:
            route.ajouter_vehicule(Vehicule("V_extra", route, 600, 10))
        except RoutePleineException as e:
            message = str(e)
            assert "5" in message
            assert "R1" in message


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
