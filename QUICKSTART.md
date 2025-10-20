# Démarrage Rapide - Network Monitor

## Installation en 3 étapes

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Tester l'installation

```bash
python test_modules.py
```

### 3. Lancer la surveillance

**Windows:**
```bash
run.bat
```

ou

```bash
python src/main.py
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

ou

```bash
python3 src/main.py
```

## Utilisation

1. **Démarrer** : L'application affiche en temps réel :
   - Ping vers Google et Cloudflare
   - Bande passante Upload/Download
   - Durée de surveillance

2. **Arrêter** : Appuyez sur `Ctrl+C`

3. **Voir les résultats** :
   - Statistiques affichées dans le terminal
   - Graphiques générés dans le dossier `data/`

## Exemple de sortie

```
╔═══════════════════════════════════════════════════════════╗
║              Surveillance Réseau en Temps Réel            ║
╚═══════════════════════════════════════════════════════════╝

┌─ LATENCE (PING) ─────────────────────────────────────────┐
│  🌐  Google      : 15.23 ms (Excellent)
│  ☁️  Cloudflare  : 12.45 ms (Excellent)
└──────────────────────────────────────────────────────────┘

┌─ BANDE PASSANTE ─────────────────────────────────────────┐
│  Upload    : ↑ ▅▅▅ 45.32 Mbps
│  Download  : ↓ ███ 125.67 Mbps
└──────────────────────────────────────────────────────────┘
```

## Fichiers générés

Après l'arrêt, vous trouverez dans `data/` :
- `network_summary_YYYYMMDD_HHMMSS.png` - Vue complète
- `ping_YYYYMMDD_HHMMSS.png` - Graphique de latence
- `bandwidth_YYYYMMDD_HHMMSS.png` - Graphique de bande passante

## Problèmes courants

### Windows : "Permission denied"
Lancez le terminal en mode Administrateur

### Linux/Mac : "Operation not permitted"
```bash
sudo python3 src/main.py
```

### Graphiques vides
Laissez la surveillance tourner au moins 30 secondes avant d'arrêter

## Support

Consultez le [README.md](README.md) pour plus de détails.
