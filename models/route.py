class Route:
    """Représente une route du réseau.

    Attributs principaux:
        nom (str): nom de la route
        longueur (float): longueur en mètres
        limite_vitesse (float): limite de vitesse
        vehicules (list): véhicules présents sur la route
    """

    def __init__(self, nom, longueur, limite_vitesse):
        """Crée une nouvelle route.

        Args:
            nom (str): nom de la route.
            longueur (float): longueur de la route en mètres.
            limite_vitesse (float): vitesse maximale autorisée.
        """
        self.nom = nom
        self.longueur = longueur
        self.limite_vitesse = limite_vitesse
        self.vehicules = []

    def ajouter_vehicule(self, vehicule):
        """Ajoute un véhicule à la route."""
        self.vehicules.append(vehicule)

    def mettre_a_jour_vehicules(self, delta_t):
        """Met à jour la position de chaque véhicule pour un pas `delta_t`."""
        for v in self.vehicules:
            v.avancer(delta_t)
