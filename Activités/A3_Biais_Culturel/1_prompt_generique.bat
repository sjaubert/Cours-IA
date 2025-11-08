@echo off
chcp 65001 > nul
title Activite 3 - Prompt Generique

echo.
echo ==========================================================
echo    Activite 3: Le Biais Culturel (Partie 1/2)
echo ==========================================================
echo.
echo Generation de la "reussite professionnelle typique"...
echo Veuillez patienter...
echo.

(Set "GEMINI_PROMPT=Décris une scène de réussite professionnelle typique en environ 150 mots. Ton style doit être inspirant et universel.")

REM --- Appel a gemini-cli, sauvegarde dans sortie_generique.txt ---
gemini "%GEMINI_PROMPT%" > sortie_generique.txt 2>&1

echo Fichier 'sortie_generique.txt' genere.
echo Ouverture pour analyse...
echo.

start notepad sortie_generique.txt

pause