#!/bin/bash

echo "========================================"
echo "                ANALYZR                 "
echo "========================================"
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "ERREUR: Python 3 n'est pas installé"
    exit 1
fi

# Vérifier si les dépendances sont installées
echo "Vérification des dépendances..."
if ! python3 -c "import colorama" &> /dev/null; then
    echo "Installation des dépendances..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERREUR: Impossible d'installer les dépendances"
        exit 1
    fi
fi

echo ""
echo "Démarrage de la surveillance..."
echo ""

# Lancer l'application
python3 src/main.py

echo ""
echo "Surveillance terminée."
