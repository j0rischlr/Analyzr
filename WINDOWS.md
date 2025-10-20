# Guide Windows - Network Monitor

## Installation et démarrage

### Méthode 1 : Script automatique (recommandé)

Double-cliquez sur `run.bat` ou lancez dans le terminal :

```cmd
run.bat
```

### Méthode 2 : Installation manuelle

1. **Installer les dépendances :**
```cmd
pip install -r requirements.txt
```

2. **Lancer l'application :**
```cmd
python src\main.py
```

### Méthode 3 : Démonstration rapide (10 secondes)

```cmd
python demo.py
```

## Problèmes courants et solutions

### ❌ Erreur : "ModuleNotFoundError: No module named 'ping3'"

**Solution :** Installez les dépendances
```cmd
pip install -r requirements.txt
```

### ❌ Erreur : "UnicodeEncodeError" ou caractères bizarres

**Solution :** Utilisez Windows Terminal ou PowerShell moderne

1. Téléchargez Windows Terminal depuis le Microsoft Store
2. Ou utilisez PowerShell 7+ : https://github.com/PowerShell/PowerShell

### ❌ Le run.bat ne fait rien

**Solutions possibles :**

1. **Python n'est pas dans le PATH**
   - Réinstallez Python en cochant "Add Python to PATH"
   - Ou ajoutez manuellement Python au PATH système

2. **Lancez depuis le terminal**
   ```cmd
   cd network_monitor
   python src\main.py
   ```

### ❌ Ping ne fonctionne pas / Timeout constant

**Cause :** Pare-feu ou antivirus bloque les requêtes ICMP

**Solutions :**

1. **Lancez en mode Administrateur**
   - Clic droit sur CMD/PowerShell → "Exécuter en tant qu'administrateur"
   - Puis lancez l'application

2. **Autorisez Python dans le pare-feu**
   - Windows Defender → Autoriser une application
   - Ajoutez python.exe

3. **Désactivez temporairement l'antivirus** (pour tester)

### ❌ Les graphiques ne s'affichent pas

**Solution :** Réinstallez matplotlib
```cmd
pip uninstall matplotlib
pip install matplotlib
```

### ❌ Bande passante toujours à 0

**Normal !** La bande passante mesure l'utilisation actuelle. Si vous ne téléchargez rien, elle sera proche de 0.

**Pour tester :**
1. Lancez l'application
2. Dans un autre terminal, lancez un téléchargement ou naviguez sur internet
3. Observez l'augmentation de la bande passante

## Commandes utiles

### Tester les modules
```cmd
python test_modules.py
```

### Démonstration rapide (10 secondes)
```cmd
python demo.py
```

### Lancer avec intervalle personnalisé
Éditez `src\main.py` ligne 135 :
```python
monitor = NetworkMonitor(interval=1.0)  # Mesure chaque seconde
```

### Voir les graphiques générés
```cmd
explorer data
```

## Configuration avancée

### Changer les serveurs de ping

Éditez `src\modules\ping_monitor.py` ligne 22 :

```python
TARGETS = {
    'Google': '8.8.8.8',
    'Cloudflare': '1.1.1.1',
    'OpenDNS': '208.67.222.222',  # Ajouter
    'Quad9': '9.9.9.9',           # Ajouter
}
```

### Utiliser UTF-8 par défaut dans CMD

Avant de lancer l'application :
```cmd
chcp 65001
python src\main.py
```

## Performances

### Application lente ?

1. **Augmentez l'intervalle de mesure** (moins de mesures = moins de CPU)
   ```python
   monitor = NetworkMonitor(interval=5.0)  # 5 secondes au lieu de 2
   ```

2. **Fermez d'autres applications réseau** (VPN, torrents, etc.)

### Consommation mémoire élevée ?

**Normal** si vous laissez tourner longtemps. Les données sont stockées en mémoire pour les graphiques.

**Solution :** Arrêtez et relancez régulièrement l'application.

## Support

### Vérifier la version de Python
```cmd
python --version
```

Minimum requis : **Python 3.8+**

### Vérifier les dépendances installées
```cmd
pip list
```

Vérifiez que ces packages sont présents :
- colorama
- psutil
- ping3
- matplotlib

### Réinstallation complète

```cmd
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

## Exemples de sorties

### Surveillance normale
```
┌─ LATENCE (PING) ─────────────────────────────────────────┐
│  🌐  Google      : 15.23 ms (Excellent)
│  ☁️  Cloudflare  : 12.45 ms (Excellent)
└──────────────────────────────────────────────────────────┘
```

### Problème réseau détecté
```
┌─ LATENCE (PING) ─────────────────────────────────────────┐
│  🌐  Google      : 250.00 ms (Mauvais)
│  ☁️  Cloudflare  : TIMEOUT
└──────────────────────────────────────────────────────────┘
```

## Désinstallation

```cmd
pip uninstall colorama psutil ping3 matplotlib speedtest-cli -y
```

Puis supprimez le dossier `network_monitor`

## Notes importantes

1. **L'application ne nécessite PAS de privilèges administrateur** grâce au fallback sur la commande système `ping`

2. **Les emojis peuvent ne pas s'afficher correctement** dans CMD classique. Utilisez Windows Terminal.

3. **Les graphiques sont sauvegardés dans le dossier `data/`** même si vous ne les voyez pas s'afficher

4. **Appuyez sur Ctrl+C pour arrêter** proprement l'application et générer les graphiques

## Bon à savoir

- La première mesure de bande passante est toujours à 0 (initialisation)
- Les pings peuvent varier selon votre connexion (Wi-Fi vs Ethernet)
- Un ping < 50ms est considéré comme bon pour la plupart des usages
- La bande passante mesure l'utilisation réelle, pas la vitesse maximale de votre connexion

## Contact

Pour tout problème, vérifiez d'abord :
1. Python est installé et dans le PATH
2. Les dépendances sont installées (`pip install -r requirements.txt`)
3. Vous utilisez un terminal moderne (Windows Terminal recommandé)
