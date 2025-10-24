# 🚦 **Simulateur de Trafic** — Traffic Simulator

Un petit simulateur de trafic écrit en Python.

## 🧩 **Dépendances**

- ✅ Aucune bibliothèque de tracé externe n'est requise. Le simulateur exporte les séries temporelles de positions en CSV (`data/positions.csv`).
- 🖼️ Si vous souhaitez visualiser les résultats, installez une bibliothèque de tracé (par ex. `matplotlib`) séparément.

## ▶️ **Exécution**

Lancer la simulation depuis la racine du projet :

```powershell
python main.py
```

## 📝 **Notes Importantes**

- 📦 Le package local `io` a été renommé en `io_pkg` pour éviter les conflits avec le module standard `io` de Python.
- ⚠️ Si vous rencontrez un `ImportError` lié à `io`, utilisez `from io_pkg import ...` au lieu de `from io import ...`.

## ℹ️ **Fichiers Utiles**

- `data/config_reseau.json` — configuration d'exemple (routes et véhicules)
- `data/resultats.json` — statistiques exportées après une simulation
- `data/positions.csv` — positions temporelles exportées par `Simulateur.tracer_positions()`

## 💡 **Astuce**

Pour exécuter les tests :

```powershell
python -m pytest -q
```

## 🏗️ **Architecture du Projet**

La structure réelle trouvée dans ce dépôt (raccourcie aux fichiers pertinents) est :

```
simulateur_trafic/
├─ .github/                     # workflows CI (optionnel)
├─ core/
│  ├─ __init__.py
│  ├─ analyseur.py
│  └─ simulateur.py
├─ data/
│  └─ config_reseau.json
├─ docs/
│  ├─ conf.py
│  ├─ index.rst
│  └─ modules.rst
├─ io_pkg/
│  ├─ __init__.py
│  ├─ affichage.py
│  └─ export.py
├─ main.py
├─ models/
│  ├─ __init__.py
│  ├─ reseau.py
│  ├─ route.py
│  └─ vehicule.py
├─ README.md
├─ requirements.txt
└─ tests/
   ├─ conftest.py
   ├─ test_vehicule.py
   ├─ test_route.py
   └─ test_reseau.py
```

## 🧭 **Flux de Données**

- Le `Simulateur` charge `data/config_reseau.json` au démarrage.
- Il instancie les `Route` et `Vehicule` dans `models`.
- À chaque pas de simulation, le `Simulateur` met à jour chaque `Route`, qui appelle `Vehicule.avancer(delta_t)`.
- Les `Analyseur` calcule des statistiques (nombre de véhicules, vitesses, moyenne).
- `io_pkg.Affichage` affiche l'état dans la console ; `io_pkg.Export` écrit `resultats.json`.
- Optionnel: `Simulateur.tracer_positions()` exporte `data/positions.csv` pour visualisation.

## 🔌 **Points d'Extension / Guide Développement**

- Ajouter des comportements de véhicules : modifier `models/vehicule.py` (accélération, freins, changement de vitesse).
- Ajouter des stratégies de routage : étendre `models/reseau.py` et `models/route.py`.
- Remplacer l'affichage : implémenter une nouvelle classe dans `io_pkg` (par ex. `affichage_gui.py`) et l'injecter dans `Simulateur`.
- Ajouter de nouveaux analyseurs : créer des modules dans `core/` et les appeler depuis `Simulateur`.

## 🧪 **Tests et CI**

### Tests pytest (dossier `tests/`)

Exécuter les tests avec pytest :

```powershell
python -m pytest -q
```

### **Tests unittest/JUnit** (dossier `junit-tests/`)

Le projet inclut également des tests au format **unittest** (bibliothèque standard Python) qui génèrent des rapports compatibles JUnit XML.

#### **Structure des tests JUnit**

- `test_vehicule_unittest.py` — Tests unitaires pour la classe Vehicule
- `test_route_unittest.py` — Tests unitaires pour la classe Route
- `test_reseau_unittest.py` — Tests unitaires pour la classe ReseauRoutier
- `test_simulateur_unittest.py` — Tests d'intégration pour le Simulateur
- `run_junit_tests.py` — Script pour exécuter tous les tests et générer les rapports XML
- `xml-reports/` — (généré) Rapports JUnit XML après exécution

#### **Exécution des tests JUnit**

**Option 1: Avec génération de rapports JUnit XML (recommandé)**

Installer d'abord le générateur de rapports XML :

```powershell
pip install unittest-xml-reporting
```

Puis exécuter tous les tests :

```powershell
python junit-tests/run_junit_tests.py
```

Les rapports XML seront générés dans `junit-tests/xml-reports/`.

**Option 2: Exécution unittest standard (sans XML)**

Exécuter tous les tests :

```powershell
python -m unittest discover junit-tests -p "test_*_unittest.py" -v
```

Exécuter un fichier de test spécifique :

```powershell
python junit-tests/test_vehicule_unittest.py
```

#### **Format des rapports JUnit**

Les rapports XML générés sont au format JUnit et peuvent être utilisés avec :

- Jenkins
- GitLab CI
- GitHub Actions
- Azure DevOps
- SonarQube
- Autres outils CI/CD

#### **Note importante**

Les tests pytest originaux sont conservés dans le dossier `tests/` et restent inchangés. Les deux formats de tests coexistent.

### **CI/CD**

Un workflow GitHub Actions (si présent) installe les dépendances, exécute les tests et construit la documentation Sphinx.

## 📚 **Génération de Documentation (Sphinx)**

1. Installer Sphinx :

```powershell
python -m pip install -U sphinx sphinx-rtd-theme
```

2. Construire la doc :

```powershell
python -m sphinx -b html docs docs/_build/html
```

Si la construction échoue car Sphinx ne peut pas importer des modules, vérifiez que vous exécutez la commande depuis la racine du projet et que toutes les dépendances d'import sont installées.

---

**Auteur :** Moatez Tilouche
