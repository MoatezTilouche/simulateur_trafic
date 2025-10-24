class ReseauRoutier:
    """Représente l'ensemble des routes composant le réseau.

    Fournit des méthodes pour ajouter des routes, récupérer une route par nom
    et obtenir un état synthétique du réseau.
    """

    def __init__(self):
        """Initialise un réseau vide (sans routes)."""
        self.routes = {}

    def ajouter_route(self, route):
        """Ajoute une instance `Route` au réseau.

        Args:
            route (Route): instance à ajouter.
        """
        self.routes[route.nom] = route

    def get_route(self, nom):
        """Retourne la route nommée `nom` ou None si elle n'existe pas."""
        return self.routes.get(nom)

    def etat_reseau(self):
        """Retourne un dictionnaire résumant la position des véhicules par route.

        Format:
            { nom_route: [(vehicule_id, position_approchee), ...], ... }
        """
        etat = {}
        for nom, route in self.routes.items():
            etat[nom] = [(v.id, round(v.position, 2)) for v in route.vehicules]
        return etat
