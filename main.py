"""Script d'exécution du simulateur.

Exécuter ce fichier pour lancer une simulation à partir de
`data/config_reseau.json`.
"""

from core.simulateur import Simulateur
from exceptions import (
    SimulateurException,
    FichierConfigurationException,
    IterationsInvalidesException
)


if __name__ == "__main__":
    try:
        print("=" * 60)
        print("🚦 SIMULATEUR DE TRAFIC ROUTIER")
        print("=" * 60)
        print()
        
        # Initialisation du simulateur
        print("📂 Chargement de la configuration...")
        simu = Simulateur("data/config_reseau.json")
        print("✅ Configuration chargée avec succès\n")
        
        # Lancement de la simulation
        print("▶️  Démarrage de la simulation...")
        print("-" * 60)
        simu.lancer_simulation(n_tours=10, delta_t=1.0)
        print("-" * 60)
        print("✅ Simulation terminée avec succès\n")
        
        # Export des positions
        print("📊 Export des positions en CSV...")
        simu.tracer_positions()
        
        print()
        print("=" * 60)
        print("✨ Simulation complète !")
        print("=" * 60)
        
    except FichierConfigurationException as e:
        print(f"\n❌ ERREUR DE CONFIGURATION [{e.code}]")
        print(f"   Fichier: {e.fichier}")
        print(f"   Raison: {e.raison}")
        print("\n💡 Vérifiez que le fichier de configuration existe et est valide.")
        exit(1)
        
    except IterationsInvalidesException as e:
        print(f"\n❌ ERREUR DE PARAMÈTRES [{e.code}]")
        print(f"   Nombre d'itérations invalide: {e.iterations}")
        print("\n💡 Le nombre d'itérations doit être un entier > 0.")
        exit(1)
        
    except SimulateurException as e:
        print(f"\n❌ ERREUR DU SIMULATEUR [{e.code}]")
        print(f"   {e.message}")
        exit(1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Simulation interrompue par l'utilisateur.")
        print("   Les données partielles ont été sauvegardées.")
        exit(0)
        
    except Exception as e:
        print(f"\n❌ ERREUR INATTENDUE: {type(e).__name__}")
        print(f"   {str(e)}")
        print("\n💡 Contactez le support technique si le problème persiste.")
        import traceback
        traceback.print_exc()
        exit(1)

