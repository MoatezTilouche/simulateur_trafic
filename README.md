# 🚦 Simulateur de Trafic Routier

[![PyPI version](https://badge.fury.io/py/simulateur-trafic-moatez.svg)](https://pypi.org/project/simulateur-trafic-moatez/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un simulateur de trafic routier complet écrit en Python avec gestion d'exceptions, tests unitaires, et documentation Sphinx. Publié sur PyPI pour installation facile.

## 📦 Installation

### Depuis PyPI (recommandé)

```bash
pip install simulateur-trafic-moatez
```

### Depuis les sources

```bash
git clone https://github.com/MoatezTilouche/simulateur_trafic.git
cd simulateur_trafic
pip install -e .
```

## 🚀 Utilisation Rapide

### En ligne de commande

```bash
# Après installation via pip
simulateur-trafic-moatez

# Ou via module Python
python -m simulateur_trafic
```

### Dans votre code Python

```python
import simulateur_trafic
from simulateur_trafic import Simulateur, Vehicule, Route

# Créer et lancer une simulation
sim = Simulateur("config_reseau.json")
sim.lancer_simulation(n_tours=100, delta_t=1.0)

print(f"Version: {simulateur_trafic.__version__}")
```

## 📁 Architecture du Projet

```
simulateur_trafic/
├─ core/                        # 🧠 Moteur de simulation
│  ├─ simulateur.py             #   Simulateur principal
│  └─ analyseur.py              #   Analyseur statistique
├─ models/                      # 🏗️ Modèles de données
│  ├─ vehicule.py               #   Classe Vehicule
│  ├─ route.py                  #   Classe Route
│  └─ reseau.py                 #   Réseau routier
├─ exceptions/                  # 🚨 Exceptions personnalisées
│  ├─ base_exceptions.py        #   Exception de base
│  ├─ vehicule_exceptions.py    #   Erreurs véhicule
│  ├─ route_exceptions.py       #   Erreurs route
│  ├─ simulateur_exceptions.py  #   Erreurs simulateur
│  └─ analyseur_exceptions.py   #   Erreurs analyseur
├─ io_pkg/                      # 📤 Entrées/Sorties
│  ├─ affichage.py              #   Affichage console
│  └─ export.py                 #   Export JSON/CSV
├─ data/                        # 📊 Données et configuration
│  ├─ config_reseau.json        #   Configuration réseau
│  ├─ resultats.json            #   Statistiques exportées
│  └─ positions.csv             #   Positions pour visualisation
├─ tests/                       # 🧪 Tests pytest
├─ junit-tests/                 # 🧪 Tests unittest/JUnit
└─ docs/                        # 📚 Documentation Sphinx
```

## 🧭 Flux de Données et Fonctionnement

1. **Configuration** : Le `Simulateur` charge `data/config_reseau.json` au démarrage
2. **Initialisation** : Instancie les `Route` et `Vehicule` selon la configuration
3. **Simulation** : À chaque pas, met à jour les positions via `Vehicule.avancer(delta_t)`
4. **Analyse** : `Analyseur` calcule statistiques (nombre véhicules, vitesses, moyenne)
5. **Affichage** : `io_pkg.Affichage` montre l'état en temps réel
6. **Export** : `io_pkg.Export` sauvegarde `resultats.json` et `positions.csv`

### Exemple de configuration (config_reseau.json)
```json
{
  "routes": [
    {"nom": "R1", "longueur": 1000, "limite_vitesse": 50, "capacite_max": 10},
    {"nom": "R2", "longueur": 800, "limite_vitesse": 60, "capacite_max": 8}
  ],
  "vehicules": [
    {"id": "V1", "route": "R1", "position": 0, "vitesse": 30},
    {"id": "V2", "route": "R2", "position": 100, "vitesse": 45}
  ]
}
```

## 🚨 Système d'Exceptions Personnalisées

Le simulateur dispose d'un système complet de gestion d'erreurs avec codes d'erreur spécifiques :

### Types d'exceptions disponibles

| Exception | Code | Description |
|-----------|------|-------------|
| `VitesseNegativeException` | VEH001 | Vitesse négative détectée |
| `PositionInvalideException` | VEH002 | Position hors limites |
| `RoutePleineException` | RTE001 | Capacité maximale atteinte |
| `VehiculeDejaPresent` | RTE002 | Véhicule déjà sur la route |
| `FichierConfigurationException` | SIM001 | Fichier config manquant/invalide |
| `DivisionParZeroException` | ANA001 | Division par zéro dans calculs |

### Utilisation des exceptions
```python
from exceptions import VitesseNegativeException, RoutePleineException

try:
    vehicule = Vehicule("V1", route, position=0, vitesse=-10)  # ❌ Erreur
except VitesseNegativeException as e:
    print(f"Erreur [{e.code}]: {e.message}")
    print(f"Vitesse invalide: {e.vitesse}")
```

## 🧪 Tests et Validation

Le projet dispose de **deux systèmes de tests complémentaires** :

### 🔬 Tests pytest (dossier `tests/`)

**Exécution :**
```bash
# Tous les tests
python -m pytest -v

# Tests avec couverture
python -m pytest --cov=simulateur_trafic

# Tests spécifiques
python -m pytest tests/test_exceptions.py -v
```

**Tests disponibles :**
- `test_vehicule.py` — Tests classe Vehicule
- `test_route.py` — Tests classe Route  
- `test_reseau.py` — Tests réseau routier
- `test_exceptions.py` — Tests gestion d'erreurs
- `test_simulateur.py` — Tests intégration

### 🏭 Tests JUnit/unittest (dossier `junit-tests/`)

**Génération de rapports XML :**
```bash
# Installer le générateur XML
pip install unittest-xml-reporting

# Exécuter avec rapports JUnit
python junit-tests/run_junit_tests.py
```

**Exécution standard :**
```bash
# Tous les tests unittest
python -m unittest discover junit-tests -p "test_*_unittest.py" -v

# Test spécifique
python junit-tests/test_vehicule_unittest.py
```

**Rapports générés :**
- Compatible avec Jenkins, GitLab CI, GitHub Actions
- Fichiers XML dans `junit-tests/xml-reports/`
- Métriques détaillées par classe et méthode

## 📚 Documentation Sphinx

**Génération de la documentation :**
```bash
# Installer Sphinx
pip install sphinx sphinx-rtd-theme

# Générer la documentation
python -m sphinx -b html docs docs/_build/html
```

**Contenu :**
- 📖 Documentation complète des APIs
- 🏗️ Architecture et design patterns
- 📊 Exemples d'utilisation
- 🚨 Guide des exceptions

## 🔌 Points d'Extension / Guide Développement

### Nouveaux comportements véhicules
```python
# Dans models/vehicule.py
class VehiculeAvance(Vehicule):
    def __init__(self, *args, acceleration=1.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.acceleration = acceleration
    
    def avancer(self, delta_t):
        # Logique d'accélération personnalisée
        super().avancer(delta_t)
```

### Stratégies de routage
```python
# Dans models/reseau.py
class ReseauIntelligent(ReseauRoutier):
    def optimiser_routes(self):
        # Algorithme d'optimisation du trafic
        pass
```

### Nouveaux affichages
```python
# Dans io_pkg/affichage_gui.py
class AffichageGUI(AffichageInterface):
    def afficher_etat(self, routes, stats):
        # Interface graphique avec tkinter/PyQt
        pass
```

## 📦 Informations PyPI

**Package publié :** [`simulateur-trafic-moatez`](https://pypi.org/project/simulateur-trafic-moatez/)

### Métadonnées
- **Version :** 1.0.0
- **Licence :** MIT
- **Python :** ≥3.8
- **Plateforme :** Toutes (Pure Python)
- **Taille :** ~60KB

### Installation et mise à jour
```bash
# Installation
pip install simulateur-trafic-moatez

# Mise à jour
pip install --upgrade simulateur-trafic-moatez

# Version spécifique
pip install simulateur-trafic-moatez==1.0.0
```

## 💡 Exemples d'Usage Avancé

### Simulation personnalisée
```python
from simulateur_trafic import Simulateur
from simulateur_trafic.models import Vehicule, Route

# Configuration custom
sim = Simulateur()
route = Route("Autoroute", longueur=5000, limite_vitesse=130)
vehicule = Vehicule("Voiture1", route, vitesse=90)

# Simulation avec callback
def callback_stats(stats):
    print(f"Vitesse moyenne: {stats['moyenne_vitesse']:.1f} km/h")

sim.lancer_simulation(
    n_tours=200, 
    delta_t=0.5,
    callback=callback_stats
)
```

### Export et visualisation
```python
import matplotlib.pyplot as plt
import pandas as pd

# Après simulation
sim.tracer_positions()  # Génère positions.csv

# Visualisation
df = pd.read_csv('data/positions.csv')
plt.plot(df['temps'], df['vitesse_moyenne'])
plt.title('Évolution de la vitesse moyenne')
plt.show()
```

## 🧩 Dépendances

- ✅ **Aucune dépendance externe** : Le simulateur fonctionne avec Python standard
- 📊 **Visualisation optionnelle** : Installez `matplotlib` séparément pour tracer les courbes
- 📋 **Tests** : `pytest` et `unittest-xml-reporting` pour les rapports JUnit

## 🎯 Roadmap / Fonctionnalités Futures

### Version 1.1.0 (Prévue)
- [ ] Interface graphique (tkinter)
- [ ] Algorithmes d'optimisation du trafic
- [ ] Support multi-threading
- [ ] Métriques avancées (pollution, consommation)

### Version 1.2.0 (Envisagée)  
- [ ] API REST pour contrôle distant
- [ ] Intégration bases de données
- [ ] Machine Learning pour prédictions
- [ ] Support feux de circulation

## 🤝 Contribution

### Comment contribuer
1. **Fork** le projet
2. **Créer** une branche feature (`git checkout -b feature/nouvelle-fonctionalite`)
3. **Commiter** vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. **Pousser** vers la branche (`git push origin feature/nouvelle-fonctionalite`)
5. **Ouvrir** une Pull Request

### Standards de code
- **PEP 8** pour le style Python
- **Type hints** pour la documentation
- **Docstrings** pour toutes les fonctions/classes
- **Tests unitaires** pour nouvelles fonctionnalités

## 📄 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**Moatez Tilouche**
- 📧 Email: moateztilouch@gmail.com
- 🐙 GitHub: [@MoatezTilouche](https://github.com/MoatezTilouche)
- 📦 PyPI: [simulateur-trafic-moatez](https://pypi.org/project/simulateur-trafic-moatez/)

## 🙏 Remerciements

- Équipe pédagogique ING3-INFO
- Communauté Python pour les outils formidables
- Contributeurs et testeurs

---

**⭐ N'hésitez pas à laisser une étoile si ce projet vous aide !**

*Dernière mise à jour : Novembre 2025*