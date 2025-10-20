"""
Démonstration rapide de l'application (10 secondes)
"""
import sys
import os
import time
import threading

# Configurer l'encodage UTF-8 pour Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from modules.ping_monitor import PingMonitor
from modules.bandwidth_monitor import BandwidthMonitor
from modules.display import Display


def demo():
    """Démonstration rapide (10 secondes)"""
    print("\n" + "=" * 70)
    print("  DÉMONSTRATION - Network Monitor (10 secondes)")
    print("=" * 70 + "\n")

    display = Display()
    ping_monitor = PingMonitor()
    bandwidth_monitor = BandwidthMonitor()

    # Afficher le logo
    display.show_logo()
    time.sleep(2)

    # 5 itérations de 2 secondes = 10 secondes
    for i in range(5):
        # Mesurer
        ping_data = ping_monitor.measure_all()
        bandwidth_data = bandwidth_monitor.measure_bandwidth()

        # Afficher
        elapsed = (i + 1) * 2
        display.show_monitoring_screen(ping_data, bandwidth_data, elapsed)

        time.sleep(2)

    # Afficher le résumé
    display.clear_screen()
    print("\n" + "=" * 70)
    print("  DÉMONSTRATION TERMINÉE")
    print("=" * 70 + "\n")

    # Statistiques
    ping_stats = {}
    for target in ping_monitor.TARGETS.keys():
        ping_stats[target] = ping_monitor.get_statistics(target)

    bandwidth_stats = bandwidth_monitor.get_statistics()

    display.show_statistics(ping_stats, bandwidth_stats, 10)

    print("\n" + "=" * 70)
    print("  Pour lancer la vraie application: python src/main.py")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\nDémonstration interrompue.")
    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()
