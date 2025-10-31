"""
Script de démonstration de la gestion des exceptions.

Ce script montre comment les exceptions personnalisées sont levées
et capturées dans différentes situations d'erreur.
"""

from models.vehicule import Vehicule
from models.route import Route
from models.reseau import ReseauRoutier
from core.simulateur import Simulateur
from core.analyseur import Analyseur

from exceptions import *


def demo_vitesse_negative():
    """Démonstration: Vitesse négative."""
    print("\n" + "="*60)
    print("📍 DEMO 1: Vitesse négative")
    print("="*60)
    
    try:
        route = Route("Route_Test", longueur=1000, limite_vitesse=50)
        vehicule = Vehicule("V_negatif", route, position=0, vitesse=-15)
        print("✅ Véhicule créé (ne devrait pas arriver ici)")
        
    except VitesseNegativeException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Vitesse invalide: {e.vitesse} m/s")
        print(f"   Véhicule: {e.vehicule_id}")
        print("✅ Exception gérée correctement")


def demo_position_invalide():
    """Démonstration: Position hors limites."""
    print("\n" + "="*60)
    print("📍 DEMO 2: Position invalide")
    print("="*60)
    
    try:
        route = Route("Route_Test", longueur=1000, limite_vitesse=50)
        vehicule = Vehicule("V_hors_limite", route, position=1500, vitesse=20)
        print("✅ Véhicule créé (ne devrait pas arriver ici)")
        
    except PositionInvalideException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Position: {e.position} m")
        print(f"   Position max: {e.position_max} m")
        print("✅ Exception gérée correctement")


def demo_longueur_route_invalide():
    """Démonstration: Longueur de route invalide."""
    print("\n" + "="*60)
    print("📍 DEMO 3: Longueur de route nulle")
    print("="*60)
    
    try:
        route = Route("Route_Nulle", longueur=0, limite_vitesse=50)
        print("✅ Route créée (ne devrait pas arriver ici)")
        
    except LongueurRouteInvalideException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Longueur invalide: {e.longueur} m")
        print(f"   Route: {e.route_id}")
        print("✅ Exception gérée correctement")


def demo_route_pleine():
    """Démonstration: Route pleine."""
    print("\n" + "="*60)
    print("📍 DEMO 4: Route pleine (capacité atteinte)")
    print("="*60)
    
    try:
        route = Route("Route_Petite", longueur=1000, limite_vitesse=50, capacite_max=2)
        print(f"   Capacité de la route: {route.capacite_max} véhicules")
        
        # Ajouter 2 véhicules
        v1 = Vehicule("V1", route, 0, 10)
        v2 = Vehicule("V2", route, 500, 15)
        route.ajouter_vehicule(v1)
        route.ajouter_vehicule(v2)
        print(f"   Véhicules ajoutés: {len(route.vehicules)}/{route.capacite_max}")
        
        # Tenter d'ajouter un 3ème véhicule
        v3 = Vehicule("V3", route, 300, 12)
        route.ajouter_vehicule(v3)
        print("✅ Véhicule ajouté (ne devrait pas arriver ici)")
        
    except RoutePleineException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Route: {e.route_id}")
        print(f"   Capacité max: {e.capacite_max}")
        print("✅ Exception gérée correctement")


def demo_vehicule_deja_present():
    """Démonstration: Véhicule déjà présent."""
    print("\n" + "="*60)
    print("📍 DEMO 5: Véhicule déjà présent sur la route")
    print("="*60)
    
    try:
        route = Route("Route_Test", longueur=1000, limite_vitesse=50)
        vehicule = Vehicule("V_double", route, 0, 10)
        
        route.ajouter_vehicule(vehicule)
        print(f"   Véhicule {vehicule.id} ajouté une première fois")
        
        # Tenter d'ajouter le même véhicule
        route.ajouter_vehicule(vehicule)
        print("✅ Véhicule ajouté (ne devrait pas arriver ici)")
        
    except VehiculeDejaPresent as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Véhicule: {e.vehicule_id}")
        print(f"   Route: {e.route_id}")
        print("✅ Exception gérée correctement")


def demo_route_inexistante():
    """Démonstration: Route inexistante."""
    print("\n" + "="*60)
    print("📍 DEMO 6: Accès à une route inexistante")
    print("="*60)
    
    try:
        reseau = ReseauRoutier()
        route1 = Route("R1", 1000, 50)
        route2 = Route("R2", 1500, 60)
        reseau.ajouter_route(route1)
        reseau.ajouter_route(route2)
        
        print(f"   Routes disponibles: {list(reseau.routes.keys())}")
        print(f"   Tentative d'accès à 'R999'...")
        
        route = reseau.get_route("R999")
        print("✅ Route trouvée (ne devrait pas arriver ici)")
        
    except RouteInexistanteException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Route recherchée: {e.route_id}")
        print(f"   Routes disponibles: {e.routes_disponibles}")
        print("✅ Exception gérée correctement")


def demo_fichier_config_inexistant():
    """Démonstration: Fichier de configuration inexistant."""
    print("\n" + "="*60)
    print("📍 DEMO 7: Fichier de configuration inexistant")
    print("="*60)
    
    try:
        print(f"   Tentative de chargement: 'config_inexistant.json'")
        sim = Simulateur("config_inexistant.json")
        print("✅ Simulateur créé (ne devrait pas arriver ici)")
        
    except FichierConfigurationException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Fichier: {e.fichier}")
        print(f"   Raison: {e.raison}")
        print("✅ Exception gérée correctement")


def demo_iterations_invalides():
    """Démonstration: Nombre d'itérations invalide."""
    print("\n" + "="*60)
    print("📍 DEMO 8: Nombre d'itérations invalide")
    print("="*60)
    
    try:
        sim = Simulateur("data/config_reseau.json")
        print("   Tentative de lancer avec -5 itérations...")
        sim.lancer_simulation(n_tours=-5, delta_t=1.0)
        print("✅ Simulation lancée (ne devrait pas arriver ici)")
        
    except IterationsInvalidesException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Itérations invalides: {e.iterations}")
        print("✅ Exception gérée correctement")


def demo_reseau_vide():
    """Démonstration: Analyse d'un réseau vide."""
    print("\n" + "="*60)
    print("📍 DEMO 9: Analyse d'un réseau vide")
    print("="*60)
    
    try:
        analyseur = Analyseur()
        reseau = ReseauRoutier()  # Réseau vide
        
        print("   Tentative d'analyse d'un réseau sans routes...")
        stats = analyseur.analyser(reseau)
        print("✅ Analyse réussie (ne devrait pas arriver ici)")
        
    except DonneesMaquantesException as e:
        print(f"❌ Exception capturée: {type(e).__name__}")
        print(f"   Code: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Données manquantes: {e.donnees_manquantes}")
        print("✅ Exception gérée correctement")


def demo_capture_globale():
    """Démonstration: Capture avec SimulateurException (exception de base)."""
    print("\n" + "="*60)
    print("📍 DEMO 10: Capture globale avec SimulateurException")
    print("="*60)
    
    erreurs_capturees = 0
    
    # Test multiple exceptions
    tests = [
        lambda: Vehicule("V1", Route("R1", 1000, 50), 0, -10),  # VitesseNegativeException
        lambda: Route("R_zero", longueur=0, limite_vitesse=50),   # LongueurRouteInvalideException
        lambda: Simulateur("inexistant.json"),                    # FichierConfigurationException
    ]
    
    for i, test in enumerate(tests, 1):
        try:
            test()
        except SimulateurException as e:
            erreurs_capturees += 1
            print(f"   Test {i}: {type(e).__name__} [{e.code}] capturée")
    
    print(f"\n✅ {erreurs_capturees}/3 exceptions capturées avec SimulateurException")
    print("   Toutes les exceptions personnalisées héritent de SimulateurException")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚨 DÉMONSTRATION DES EXCEPTIONS PERSONNALISÉES")
    print("="*60)
    print("\nCe script montre comment les exceptions sont levées et gérées")
    print("dans différentes situations d'erreur du simulateur de trafic.")
    
    # Exécuter toutes les démos
    demo_vitesse_negative()
    demo_position_invalide()
    demo_longueur_route_invalide()
    demo_route_pleine()
    demo_vehicule_deja_present()
    demo_route_inexistante()
    demo_fichier_config_inexistant()
    demo_iterations_invalides()
    demo_reseau_vide()
    demo_capture_globale()
    
    print("\n" + "="*60)
    print("✨ DÉMONSTRATION TERMINÉE")
    print("="*60)
    print("\nToutes les exceptions ont été levées et gérées correctement!")
    print("Les messages d'erreur sont clairs et informatifs.")
    print("\n💡 Consultez exceptions/README.md pour plus d'informations.\n")
