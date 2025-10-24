🚦 simulateur_trafic — Traffic simulator

✍️ Auteur : Moatez Tilouche

Un petit simulateur de trafic écrit en Python.

🧩 Dépendances

- ✅ Aucune bibliothèque de tracé externe n'est requise. Le simulateur exporte les séries temporelles de positions en CSV (`data/positions.csv`).
- 🖼️ Si vous souhaitez visualiser les résultats, installez une bibliothèque de tracé (par ex. `matplotlib`) séparément.

▶️ Exécution

Lancer la simulation depuis la racine du projet :

```powershell
python main.py
```

📝 Notes importantes

- 📦 Le package local `io` a été renommé en `io_pkg` pour éviter les conflits avec le module standard `io` de Python.
- ⚠️ Si vous rencontrez un `ImportError` lié à `io`, utilisez `from io_pkg import ...` au lieu de `from io import ...`.

ℹ️ Fichiers utiles

- `data/config_reseau.json` — configuration d'exemple (routes et véhicules)
- `data/resultats.json` — statistiques exportées après une simulation
- `data/positions.csv` — positions temporelles exportées par `Simulateur.tracer_positions()`

💡 Astuce

Pour exécuter les tests :

```powershell
python -m pytest -q
```

🏗️ Architecture exacte du projet

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

🧭 Flux de données (haute-niveau)

- Le `Simulateur` charge `data/config_reseau.json` au démarrage.
- Il instancie les `Route` et `Vehicule` dans `models`.
- À chaque pas de simulation, le `Simulateur` met à jour chaque `Route`, qui appelle `Vehicule.avancer(delta_t)`.
- Les `Analyseur` calcule des statistiques (nombre de véhicules, vitesses, moyenne).
- `io_pkg.Affichage` affiche l'état dans la console ; `io_pkg.Export` écrit `resultats.json`.
- Optionnel: `Simulateur.tracer_positions()` exporte `data/positions.csv` pour visualisation.

🔌 Points d'extension / Guide développement

- Ajouter des comportements de véhicules : modifier `models/vehicule.py` (accélération, freins, changement de vitesse).
- Ajouter des stratégies de routage : étendre `models/reseau.py` et `models/route.py`.
- Remplacer l'affichage : implémenter une nouvelle classe dans `io_pkg` (par ex. `affichage_gui.py`) et l'injecter dans `Simulateur`.
- Ajouter de nouveaux analyseurs : créer des modules dans `core/` et les appeler depuis `Simulateur`.

🧪 Tests et CI

- Tests : exécuter `python -m pytest -q` depuis la racine.
- CI : un workflow GitHub Actions (si présent) installe les dépendances, exécute les tests et construit la documentation Sphinx.

📚 Génération de documentation (Sphinx)

1. Installer Sphinx :

```powershell
python -m pip install -U sphinx sphinx-rtd-theme
```

2. Construire la doc :

```powershell
python -m sphinx -b html docs docs/_build/html
```

Si la construction échoue car Sphinx ne peut pas importer des modules, vérifiez que vous exécutez la commande depuis la racine du projet et que toutes les dépendances d'import sont installées.
