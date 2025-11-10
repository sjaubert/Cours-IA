@echo off
chcp 65001 > nul
title Activite 5 - Generation de Rapport

echo.
echo ==========================================================
echo    Activite 5: L'IA Redactrice de Rapports
echo ==========================================================
echo.
echo Verification des fichiers...

if not exist "maintenance_logs.csv" (
    echo ERREUR: Fichier 'maintenance_logs.csv' introuvable.
    echo Veuillez d'abord executer le script 'create_logs.py'.
    pause
    exit /b
)

if not exist "prompt_simple.txt" (
    echo ERREUR: Fichier 'prompt_simple.txt' introuvable.
    pause
    exit /b
)

echo.
echo Fichiers trouves.
echo Utilisation de 'prompt_simple.txt' pour interroger l'IA...
echo Analyse des 500 lignes de 'maintenance_logs.csv' en cours...
echo.
echo Veuillez patienter, cela peut prendre 10-20 secondes.
echo.

REM --- Lecture du prompt depuis le fichier texte ---
set /p GEMINI_PROMPT=<prompt_simple.txt

REM --- Appel a gemini-cli :
REM --- -i 'maintenance_logs.csv' passe le fichier en contexte (grace a MCP)
REM --- "%GEMINI_PROMPT%" passe la question
REM --- > rapport_genere.md sauvegarde le resultat
REM ---
gemini -i "maintenance_logs.csv" "%GEMINI_PROMPT%" > rapport_genere.md 2>&1

echo.
echo Fichier 'rapport_genere.md' genere avec succes !
echo.
echo Ouverture du rapport...
echo.

start "" "rapport_genere.md"

pause