"""
Script de test pour vérifier que tous les modules fonctionnent
"""
import sys
import os

# Configurer l'encodage UTF-8 pour Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test des imports de modules"""
    print("🔍 Test des imports...")

    try:
        from modules.ping_monitor import PingMonitor
        print("  ✓ PingMonitor")
    except Exception as e:
        print(f"  ✗ PingMonitor: {e}")
        return False

    try:
        from modules.bandwidth_monitor import BandwidthMonitor
        print("  ✓ BandwidthMonitor")
    except Exception as e:
        print(f"  ✗ BandwidthMonitor: {e}")
        return False

    try:
        from modules.display import Display
        print("  ✓ Display")
    except Exception as e:
        print(f"  ✗ Display: {e}")
        return False

    try:
        from modules.graph_generator import GraphGenerator
        print("  ✓ GraphGenerator")
    except Exception as e:
        print(f"  ✗ GraphGenerator: {e}")
        return False

    return True


def test_dependencies():
    """Test des dépendances"""
    print("\n🔍 Test des dépendances...")

    dependencies = [
        'colorama',
        'psutil',
        'ping3',
        'matplotlib',
    ]

    all_ok = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"  ✓ {dep}")
        except ImportError:
            print(f"  ✗ {dep} - NON INSTALLÉ")
            all_ok = False

    return all_ok


def test_ping():
    """Test du module ping"""
    print("\n🔍 Test du module ping...")

    try:
        from modules.ping_monitor import PingMonitor

        monitor = PingMonitor()
        results = monitor.measure_all()

        for server, ping in results.items():
            if ping is not None:
                print(f"  ✓ {server}: {ping:.2f} ms")
            else:
                print(f"  ⚠ {server}: TIMEOUT")

        return True
    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False


def test_bandwidth():
    """Test du module bandwidth"""
    print("\n🔍 Test du module bandwidth...")

    try:
        from modules.bandwidth_monitor import BandwidthMonitor
        import time

        monitor = BandwidthMonitor()

        # Première mesure (initialisation)
        monitor.measure_bandwidth()
        time.sleep(1)

        # Deuxième mesure (réelle)
        results = monitor.measure_bandwidth()

        print(f"  ✓ Upload: {results['upload']:.2f} Mbps")
        print(f"  ✓ Download: {results['download']:.2f} Mbps")

        return True
    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False


def test_display():
    """Test du module display"""
    print("\n🔍 Test du module display...")

    try:
        from modules.display import Display

        display = Display()
        display.clear_screen()
        display.show_logo()

        print("  ✓ Affichage du logo")

        # Test de formatage
        ping_formatted = display.format_ping_color(15.5)
        print(f"  ✓ Format ping: {ping_formatted}")

        bandwidth_formatted = display.format_bandwidth_color(50.2, 'download')
        print(f"  ✓ Format bandwidth: {bandwidth_formatted}")

        return True
    except Exception as e:
        print(f"  ✗ Erreur: {e}")
        return False


def main():
    """Exécute tous les tests"""
    print("=" * 60)
    print("  TEST DES MODULES NETWORK MONITOR")
    print("=" * 60 + "\n")

    tests = [
        ("Dépendances", test_dependencies),
        ("Imports", test_imports),
        ("Display", test_display),
        ("Ping", test_ping),
        ("Bandwidth", test_bandwidth),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Erreur lors du test {name}: {e}")
            results.append((name, False))

    # Résumé
    print("\n" + "=" * 60)
    print("  RÉSUMÉ DES TESTS")
    print("=" * 60)

    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status} - {name}")

    total = len(results)
    passed = sum(1 for _, r in results if r)

    print("\n" + "=" * 60)
    print(f"  Résultat: {passed}/{total} tests réussis")
    print("=" * 60 + "\n")

    if passed == total:
        print("✅ Tous les tests sont passés! L'application est prête.")
        return 0
    else:
        print("⚠️  Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
