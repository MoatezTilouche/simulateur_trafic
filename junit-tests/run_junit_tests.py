#!/usr/bin/env python
"""
Script pour exécuter tous les tests unittest et générer des rapports JUnit XML.

Usage:
    python junit-tests/run_junit_tests.py
"""

import unittest
import sys
import os

# Installer xmlrunner si nécessaire: pip install unittest-xml-reporting


def main():
    """Découvre et exécute tous les tests unittest dans ce dossier."""
    
    # Ajouter le répertoire parent au path
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    # Découvrir tous les tests dans le dossier junit-tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test_*_unittest.py')
    
    # Essayer d'utiliser xmlrunner si disponible pour générer des rapports JUnit XML
    try:
        import xmlrunner
        runner = xmlrunner.XMLTestRunner(output='junit-tests/xml-reports', verbosity=2)
        print("✓ Génération des rapports JUnit XML dans junit-tests/xml-reports/")
    except ImportError:
        print("⚠ xmlrunner non installé. Installation recommandée : pip install unittest-xml-reporting")
        print("→ Utilisation du runner unittest standard")
        runner = unittest.TextTestRunner(verbosity=2)
    
    # Exécuter les tests
    result = runner.run(suite)
    
    # Retourner le code de sortie approprié
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
