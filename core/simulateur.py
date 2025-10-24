from models import ReseauRoutier, Route, Vehicule
from core.analyseur import Analyseur
from io_pkg import Affichage, Export
import json
import csv

class Simulateur:
    """Simulateur principal.

    Gère le réseau routier, l'avancement du temps, l'analyse et l'export des
    résultats. Charge une configuration JSON décrivant les routes et
    véhicules.
    """

    def __init__(self, fichier_config):
        """Initialise le simulateur à partir d'un fichier de configuration.

        Args:
            fichier_config (str): chemin vers un fichier JSON contenant
                les routes et véhicules à instancier.
        """
        self.reseau = ReseauRoutier()
        self.temps = 0
        self.analyseur = Analyseur()
        self.affichage = Affichage()
        self.exporteur = Export()
        self.historique = []

        # Charger configuration
        with open(fichier_config, "r") as f:
            config = json.load(f)

        for r in config["routes"]:
            route = Route(r["nom"], r["longueur"], r["limite_vitesse"])
            self.reseau.ajouter_route(route)

        for v in config["vehicules"]:
            route = self.reseau.get_route(v["route"])
            vehicule = Vehicule(v["id"], route, v["position"], v["vitesse"])
            route.ajouter_vehicule(vehicule)

    def lancer_simulation(self, n_tours, delta_t):
        """Exécute la simulation pendant `n_tours` incréments de `delta_t`.

        À chaque tour:
        - avance le temps
        - met à jour les véhicules sur chaque route
        - calcule des statistiques via l'analyseur
        - affiche l'état
        - enregistre un snapshot des positions dans l'historique

        Args:
            n_tours (int): nombre de pas de simulation à exécuter.
            delta_t (float): durée (en secondes) d'un pas de simulation.
        """
        for _ in range(n_tours):
            self.temps += delta_t
            for route in self.reseau.routes.values():
                route.mettre_a_jour_vehicules(delta_t)

            stats = self.analyseur.analyser(self.reseau)
            self.affichage.afficher_etat(self.temps, self.reseau, stats)

            snapshot = {"temps": self.temps, "positions": {}}
            for route in self.reseau.routes.values():
                for v in route.vehicules:
                    snapshot["positions"][v.id] = v.position
            self.historique.append(snapshot)

        self.exporteur.exporter_resultats(stats, "data/resultats.json")

    def tracer_positions(self):
        """Exporte les positions des véhicules au format CSV.

        Le fichier produit contient une colonne 'temps' suivie d'une colonne par
        véhicule (identifiée par son id). Ce jeu de données peut ensuite être
        visualisé avec l'outil de votre choix.
        """
        # Export position time-series to CSV using the standard library so plotting
        # is optional and doesn't require matplotlib.
        if not self.historique:
            print("Aucun historique disponible pour tracer les positions.")
            return

        # Collect all vehicle ids and sorted time steps
        temps = [s["temps"] for s in self.historique]
        vehicules_ids = []
        seen = set()
        for s in self.historique:
            for vid in s["positions"].keys():
                if vid not in seen:
                    seen.add(vid)
                    vehicules_ids.append(vid)

        out_path = "data/positions.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Header: time + vehicle ids
            writer.writerow(["temps"] + list(vehicules_ids))
            for s in self.historique:
                row = [s["temps"]]
                for vid in vehicules_ids:
                    row.append(s["positions"].get(vid, ""))
                writer.writerow(row)

        print(f"Positions exportées vers {out_path} (CSV). Use your preferred plotting tool to visualize it.")
