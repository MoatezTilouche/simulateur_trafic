class Vehicule:
    """Représente un véhicule dans la simulation.

    Attributs:
        id (str): identifiant unique du véhicule
        route (Route): route sur laquelle il circule
        position (float): position actuelle en mètres
        vitesse (float): vitesse actuelle en mètres/seconde
    """

    def __init__(self, identifiant, route, position=0.0, vitesse=0.0):
        """Initialise un véhicule.

        Args:
            identifiant: identifiant unique (str ou int).
            route: instance de `Route` où le véhicule est placé.
            position (float): position initiale (m).
            vitesse (float): vitesse initiale (m/s).
        """
        self.id = identifiant
        self.route = route
        self.position = position
        self.vitesse = vitesse

    def avancer(self, delta_t):
        """Fait avancer le véhicule en fonction de sa vitesse pendant `delta_t`.

        La position est bornée par la longueur de la route.
        """
        self.position += self.vitesse * delta_t
        if self.position > self.route.longueur:
            self.position = self.route.longueur

    def changer_de_route(self, nouvelle_route):
        """Change la route du véhicule et réinitialise sa position à 0."""
        self.route = nouvelle_route
        self.position = 0
