class Analyseur:
    """Classe simple d'analyse du réseau.

    Fournit des méthodes pour calculer des statistiques basiques sur le réseau
    (nombre de véhicules, liste des vitesses et vitesse moyenne).
    """

    def analyser(self, reseau):
        """Analyse l'état du `reseau` et renvoie des statistiques.

        Args:
            reseau: instance de `ReseauRoutier` contenant les routes et véhicules.

        Returns:
            dict: clés: 'nb_vehicules', 'vitesses', 'moyenne_vitesse'.
        """
        stats = {"nb_vehicules": 0, "vitesses": [], "moyenne_vitesse": 0}

        for route in reseau.routes.values():
            for v in route.vehicules:
                stats["nb_vehicules"] += 1
                stats["vitesses"].append(v.vitesse)

        if stats["vitesses"]:
            stats["moyenne_vitesse"] = sum(stats["vitesses"]) / len(stats["vitesses"])

        return stats
