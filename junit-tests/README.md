# Tests JUnit/unittest

Ce dossier contient les tests au format **unittest** (bibliothèque standard Python) qui génèrent des rapports compatibles JUnit XML.

## 📁 Structure

- `test_vehicule_unittest.py` — Tests unitaires pour la classe Vehicule
- `test_route_unittest.py` — Tests unitaires pour la classe Route
- `test_reseau_unittest.py` — Tests unitaires pour la classe ReseauRoutier
- `test_simulateur_unittest.py` — Tests d'intégration pour le Simulateur
- `run_junit_tests.py` — Script pour exécuter tous les tests et générer les rapports XML
- `xml-reports/` — (généré) Rapports JUnit XML après exécution

## 🚀 Exécution des tests

### Option 1: Avec génération de rapports JUnit XML (recommandé)

Installer d'abord le générateur de rapports XML :

```powershell
pip install unittest-xml-reporting
```

Puis exécuter tous les tests :

```powershell
python junit-tests/run_junit_tests.py
```

Les rapports XML seront générés dans `junit-tests/xml-reports/`.

### Option 2: Exécution unittest standard (sans XML)

Exécuter tous les tests :

```powershell
python -m unittest discover junit-tests -p "test_*_unittest.py" -v
```

Exécuter un fichier de test spécifique :

```powershell
python junit-tests/test_vehicule_unittest.py
```

## 📊 Format des rapports

Les rapports XML générés sont au format JUnit et peuvent être utilisés avec :

- Jenkins
- GitLab CI
- GitHub Actions
- Azure DevOps
- SonarQube
- Autres outils CI/CD

## ⚠️ Note

Les tests pytest originaux sont conservés dans le dossier `tests/` et restent inchangés.
