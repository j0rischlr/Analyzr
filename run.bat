@echo off
echo ========================================
echo                ANALYZR
echo ========================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou n'est pas dans le PATH
    pause
    exit /b 1
)

REM Vérifier si les dépendances sont installées
echo Verification des dependances...
pip show colorama >nul 2>&1
if errorlevel 1 (
    echo Installation des dependances...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERREUR: Impossible d'installer les dependances
        pause
        exit /b 1
    )
)

echo.
echo Demarrage de la surveillance...
echo.

REM Lancer l'application
python src\main.py

echo.
echo Surveillance terminee.
pause
