# Network Monitor - Surveillance Réseau CLI

Application CLI de surveillance réseau en temps réel avec interface ASCII colorée et génération de graphiques.

## Fonctionnalités

- **Surveillance en temps réel**
  - Latence (ping) vers Google (8.8.8.8) et Cloudflare (1.1.1.1)
  - Bande passante Upload/Download
  - Interface CLI colorée avec ASCII art
  - Indicateurs visuels de qualité

- **Résumé et statistiques**
  - Statistiques complètes (min, max, moyenne)
  - Taux de perte de paquets
  - Durée totale de surveillance

- **Graphiques**
  - Graphique combiné avec tous les indicateurs
  - Graphiques individuels (ping, bande passante)
  - Export en PNG haute résolution

## Prérequis

- Python 3.8 ou supérieur
- pip

## Installation

1. Installez les dépendances :

```bash
cd network_monitor
pip install -r requirements.txt
```

## Utilisation

### Lancer la surveillance

```bash
python src/main.py
```

### Arrêter la surveillance

Appuyez sur `Ctrl+C` pour arrêter la surveillance et générer le résumé.

## Interface

L'interface affiche en temps réel :

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   ███╗   ██╗███████╗████████╗    ███╗   ███╗ ██████╗ ███╗   ██╗
║   ████╗  ██║██╔════╝╚══██╔══╝    ████╗ ████║██╔═══██╗████╗  ██║
║   ██╔██╗ ██║█████╗     ██║       ██╔████╔██║██║   ██║██╔██╗ ██║
║   ██║╚██╗██║██╔══╝     ██║       ██║╚██╔╝██║██║   ██║██║╚██╗██║
║   ██║ ╚████║███████╗   ██║       ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
║   ╚═╝  ╚═══╝╚══════╝   ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
║                                                           ║
║              Surveillance Réseau en Temps Réel            ║
╚═══════════════════════════════════════════════════════════╝

    SURVEILLANCE EN COURS - Appuyez sur Ctrl+C pour arrêter

  ⏱  Durée de surveillance: 02:45

┌─ LATENCE (PING) ─────────────────────────────────────────┐
│
│  🌐  Google      : 15.23 ms (Excellent)
│  ☁️  Cloudflare  : 12.45 ms (Excellent)
│
└──────────────────────────────────────────────────────────┘

┌─ BANDE PASSANTE ─────────────────────────────────────────┐
│
│  Upload    : ↑ ▅▅▅ 45.32 Mbps
│  Download  : ↓ ███ 125.67 Mbps
│
└──────────────────────────────────────────────────────────┘
```

## Indicateurs de qualité

### Latence (Ping)
- 🟢 **Excellent** : < 20 ms
- 🟡 **Bon** : 20-50 ms
- 🟠 **Moyen** : 50-100 ms
- 🔴 **Mauvais** : > 100 ms

### Bande passante
- Barres visuelles proportionnelles à la vitesse
- Couleurs graduées selon le débit

## Structure du projet

```
network_monitor/
├── src/
│   ├── main.py                      # Application principale
│   └── modules/
│       ├── ping_monitor.py          # Surveillance ping
│       ├── bandwidth_monitor.py     # Surveillance bande passante
│       ├── display.py               # Interface CLI
│       └── graph_generator.py       # Génération de graphiques
├── data/                            # Dossier des graphiques générés
├── requirements.txt
└── README.md
```

## Modules

### PingMonitor (`src/modules/ping_monitor.py`)
- Mesure le ping vers Google et Cloudflare
- Calcule les statistiques (min, max, moyenne, perte)
- Stocke l'historique complet

### BandwidthMonitor (`src/modules/bandwidth_monitor.py`)
- Surveille la bande passante upload/download
- Convertit automatiquement en Mbps
- Calcule les statistiques de débit

### Display (`src/modules/display.py`)
- Interface CLI colorée avec Colorama
- ASCII art et formatage visuel
- Indicateurs de qualité automatiques

### GraphGenerator (`src/modules/graph_generator.py`)
- Génère des graphiques avec Matplotlib
- Vue combinée et vues individuelles
- Export PNG haute résolution

## Graphiques générés

À l'arrêt de la surveillance, 3 graphiques sont générés dans `data/` :

1. **network_summary_YYYYMMDD_HHMMSS.png** - Vue d'ensemble complète
2. **ping_YYYYMMDD_HHMMSS.png** - Évolution de la latence
3. **bandwidth_YYYYMMDD_HHMMSS.png** - Évolution de la bande passante

## Configuration

Vous pouvez modifier l'intervalle de mesure en éditant `src/main.py:120` :

```python
monitor = NetworkMonitor(interval=2.0)  # Mesure toutes les 2 secondes
```

## Dépendances

- **colorama** : Couleurs dans le terminal
- **psutil** : Informations système et réseau
- **ping3** : Mesure de latence
- **matplotlib** : Génération de graphiques
- **speedtest-cli** : Tests de vitesse (réservé pour usage futur)

## Permissions

Sur Linux/Mac, certaines mesures peuvent nécessiter des privilèges root :

```bash
sudo python src/main.py
```

## Résolution de problèmes

### Erreur "Permission denied" pour ping
Sur Linux, donnez les permissions ICMP :

```bash
sudo setcap cap_net_raw+ep $(which python3)
```

### Les graphiques ne s'affichent pas
Vérifiez que matplotlib est correctement installé :

```bash
pip install --upgrade matplotlib
```

### Colorama ne fonctionne pas sur Windows
Assurez-vous d'utiliser un terminal compatible (Windows Terminal, PowerShell 7+)

## Exemples de résultats

Après arrêt de la surveillance :

```
═══════════════════════════════════════════════════════════
                    RÉSUMÉ DE LA SURVEILLANCE
═══════════════════════════════════════════════════════════

Durée totale: 5 min 23 sec

STATISTIQUES DE LATENCE:
──────────────────────────────────────────────────────────

Google:
  Min:     12.45 ms
  Max:     28.34 ms
  Moyenne: 15.67 ms
  Perte:   0.0%

Cloudflare:
  Min:     10.23 ms
  Max:     25.12 ms
  Moyenne: 13.45 ms
  Perte:   0.0%

STATISTIQUES DE BANDE PASSANTE:
──────────────────────────────────────────────────────────

Upload:
  Min:     2.34 Mbps
  Max:     52.45 Mbps
  Moyenne: 28.12 Mbps

Download:
  Min:     15.67 Mbps
  Max:     145.23 Mbps
  Moyenne: 95.34 Mbps

──────────────────────────────────────────────────────────

📊 Génération des graphiques...

✓ Graphiques sauvegardés: data/network_summary_20251020_184523.png
   • Ping: data/ping_20251020_184523.png
   • Bande passante: data/bandwidth_20251020_184523.png
```

## Développement futur

- [ ] Export des données en CSV/JSON
- [ ] Alertes configurables
- [ ] Support multi-serveurs personnalisés
- [ ] Dashboard web en temps réel
- [ ] Tests de vitesse intégrés (speedtest)
- [ ] Détection d'anomalies réseau
- [ ] Notifications (email, webhook)

## Licence

MIT

## Auteur

Créé avec Claude Code
