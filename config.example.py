"""
Fichier de configuration (optionnel)
Copiez ce fichier en config.py et modifiez selon vos besoins
"""

# Intervalle entre chaque mesure (en secondes)
MEASUREMENT_INTERVAL = 2.0

# Serveurs à surveiller pour le ping
PING_TARGETS = {
    'Google': '8.8.8.8',
    'Cloudflare': '1.1.1.1',
    # Vous pouvez ajouter d'autres serveurs :
    # 'OpenDNS': '208.67.222.222',
    # 'Quad9': '9.9.9.9',
}

# Timeout pour les pings (en secondes)
PING_TIMEOUT = 2

# Répertoire de sauvegarde des graphiques
OUTPUT_DIR = 'data'

# Résolution des graphiques (DPI)
GRAPH_DPI = 150

# Couleurs personnalisées (format hex)
COLORS = {
    'google': '#4285F4',
    'cloudflare': '#F6821F',
    'upload': '#4CAF50',
    'download': '#2196F3',
}
