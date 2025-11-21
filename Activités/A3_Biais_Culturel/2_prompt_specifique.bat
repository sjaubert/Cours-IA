@echo off
chcp 65001 > nul
title Activite 3 - Prompt Specifique

echo.
echo ==========================================================
echo    Activite 3: Le Biais Culturel (Partie 2/2)
echo ==========================================================
echo.
echo Generation de la "reussite professionnelle specifique"...
echo Veuillez patienter...
echo.

(Set "GEMINI_PROMPT=Décris une scène de réussite professionnelle selon une perspective rurale ou axée sur la communauté (par opposition à une réussite individuelle en entreprise). Rédige environ 150 mots.")

REM --- Appel a gemini-cli, sauvegarde dans sortie_specifique.txt ---
gemini "%GEMINI_PROMPT%" > sortie_specifique.txt 2>&1

echo Fichier 'sortie_specifique.txt' genere.
echo Ouverture pour analyse et comparaison...
echo.

start notepad sortie_specifique.txt

pause