class FeuRouge:
    """Classe simple représentant un feu tricolore cyclique.

    Le feu a trois états: 'rouge' -> 'vert' -> 'orange' -> 'rouge' ...
    Le paramètre `cycle` définit la durée (en secondes) de chaque état.
    """

    def __init__(self, cycle=5):
        # durée (en secondes) de chaque état
        self.cycle = float(cycle)
        # ordre des états
        self._etats = ['rouge', 'vert', 'orange']
        # index de l'état courant
        self._index = 0
        # compteur de temps dans l'état courant
        self._t = 0.0

    @property
    def etat(self):
        """Retourne l'état courant: 'rouge', 'vert' ou 'orange'."""
        return self._etats[self._index]

    def avancer_temps(self, dt):
        """Fait avancer le temps du feu de `dt` secondes et change d'état si nécessaire."""
        if dt <= 0:
            return
        self._t += float(dt)
        # tant que le compteur dépasse la durée de l'état, avancer l'état
        while self._t >= self.cycle:
            self._t -= self.cycle
            self._index = (self._index + 1) % len(self._etats)
