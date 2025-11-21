@echo off
chcp 65001 > nul
title Activite 4 - L'illusion du raisonnement

echo.
echo ==========================================================
echo    Activite 4: L'illusion du raisonnement
echo ==========================================================
echo.
echo L'ENIGME QUI SERA POSEE A L'IA EST LA SUIVANTE :
echo.
echo    "Si Pierre a deux freres et que chaque frere a une soeur,
echo     combien y a-t-il d'enfants dans la famille ?"
echo.
echo.
echo Pour pieger l'IA, nous allons lui faire lire le fichier
echo 'orienter_ia.md' avant de lui poser la question.
echo Voici le contenu de ce fichier de "biais" :
echo ----------------------------------------------------------
type orienter_ia.md
echo ----------------------------------------------------------
echo.
echo Generation de la reponse en cours...
echo.

(Set "GEMINI_PROMPT=Analyse l'enigme suivante en te basant STRICTEMENT sur le contexte de logique fourni ci-dessus. Enigme : 'Si Pierre a deux freres et que chaque frere a une soeur, combien y a-t-il d'enfants dans la famille ?' Explique ton raisonnement etape par etape avant de donner la reponse.")

REM --- Appel a gemini-cli :
REM --- 1. 'type orienter_ia.md' lit le fichier de biais
REM --- 2. '|' (pipe) envoie ce texte en contexte a gemini
REM --- 3. CORRECTION: Suppression du drapeau '-t 1.0' non reconnu
REM --- 4. '%GEMINI_PROMPT%' est la question
REM --- 5. '> reponse_ia.txt 2>&1' sauvegarde le resultat (et les erreurs)
REM ---
type orienter_ia.md | gemini "%GEMINI_PROMPT%" > reponse_ia.txt 2>&1

echo Fichier 'reponse_ia.txt' genere.
echo Ouverture pour analyse...
echo.

start notepad reponse_ia.txt

pause