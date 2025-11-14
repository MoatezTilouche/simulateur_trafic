from exceptions import (
    LongueurRouteInvalideException,
    RoutePleineException,
    VehiculeDejaPresent
)


class Route:
    """Représente une route du réseau.

    Attributs principaux:
        nom (str): nom de la route
        longueur (float): longueur en mètres
        limite_vitesse (float): limite de vitesse
        vehicules (list): véhicules présents sur la route
    """

    def __init__(self, nom, longueur, limite_vitesse, capacite_max=100):
        """Crée une nouvelle route.

        Args:
            nom (str): nom de la route.
            longueur (float): longueur de la route en mètres.
            limite_vitesse (float): vitesse maximale autorisée.
            capacite_max (int): capacité maximale de véhicules (défaut: 100).
            
        Raises:
            LongueurRouteInvalideException: Si la longueur est <= 0.
            ValueError: Si la limite de vitesse est négative.
        """
        # Validation de la longueur
        if longueur <= 0:
            raise LongueurRouteInvalideException(longueur, nom)
        
        # Validation de la limite de vitesse
        if limite_vitesse < 0:
            raise ValueError(f"La limite de vitesse doit être >= 0 pour la route '{nom}'")
        
        self.nom = nom
        self.longueur = longueur
        self.limite_vitesse = limite_vitesse
        self.capacite_max = capacite_max
        self.vehicules = []
        # support pour un feu de circulation (objet FeuRouge et position)
        self.feu_rouge = None
        self.position_feu = None

    def ajouter_vehicule(self, vehicule):
        """Ajoute un véhicule à la route.
        
        Args:
            vehicule (Vehicule): Le véhicule à ajouter.
            
        Raises:
            RoutePleineException: Si la route a atteint sa capacité maximale.
            VehiculeDejaPresent: Si le véhicule est déjà sur cette route.
        """
        # Vérifier si la route est pleine
        if len(self.vehicules) >= self.capacite_max:
            raise RoutePleineException(self.nom, self.capacite_max)
        
        # Vérifier si le véhicule est déjà présent
        for v in self.vehicules:
            if v.id == vehicule.id:
                raise VehiculeDejaPresent(str(vehicule.id), self.nom)
        
        # Ajouter le véhicule
        self.vehicules.append(vehicule)

    def ajouter_feu_rouge(self, feu, position=None):
        """Ajoute un feu rouge à la route à la position donnée.

        Args:
            feu: instance de FeuRouge
            position (float): position en mètres le long de la route (par défaut milieu)
        """
        if position is None:
            position = self.longueur / 2.0
        # clamp
        if position < 0:
            position = 0.0
        if position > self.longueur:
            position = self.longueur
        self.feu_rouge = feu
        self.position_feu = position

    def mettre_a_jour_vehicules(self, delta_t):
        """Met à jour la position de chaque véhicule pour un pas `delta_t`.
        
        Args:
            delta_t (float): Intervalle de temps en secondes.
        """
        try:
            # Mettre à jour le feu s'il existe
            if self.feu_rouge is not None:
                try:
                    self.feu_rouge.avancer_temps(delta_t)
                except Exception:
                    pass

            for v in self.vehicules:
                # si un feu est présent et rouge, empêcher de traverser la position
                if self.feu_rouge is not None and self.feu_rouge.etat == 'rouge' and self.position_feu is not None:
                    prochaine_position = v.position + v.vitesse * delta_t
                    if v.position < self.position_feu and prochaine_position >= self.position_feu:
                        # arrêt : placer juste avant le feu et mettre la vitesse à 0
                        v.position = max(0.0, self.position_feu - 1.0)
                        v.vitesse = 0.0
                        continue

                v.avancer(delta_t)
        except Exception as e:
            # Log l'erreur mais continue avec les autres véhicules
            print(f"Erreur lors de la mise à jour du véhicule {v.id} sur la route {self.nom}: {e}")
            raise
