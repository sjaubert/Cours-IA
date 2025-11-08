@echo off
REM --- Configure la console pour afficher correctement les accents (UTF-8) ---
chcp 65001 > nul
title Activite 1 - Generation de Biographie

echo.
echo ==========================================================
echo    Activite 1: L'illusion de la verite
echo ==========================================================
echo.
echo Generation de la biographie en cours... Veuillez patienter.
echo (Cela peut prendre quelques secondes)
echo.

REM --- 
REM --- Definition du prompt piege. Utilisation de "GEMINI_PROMPT" (non reserve).
REM ---
(Set "GEMINI_PROMPT=Tu es un excellent redacteur et biographe, mais tu as une mauvaise memoire des details fins. Redige une biographie de Marie Curie d'environ 200 mots pour un magazine de vulgarisation scientifique. Ton style doit etre tres confiant, fluide et academique. Inclus des faits sur sa vie, ses decouvertes et ses prix Nobel. Comme tu ecris de memoire, tu vas probablement te tromper sur 3 ou 4 details (par exemple, une date exacte, le nom d'une substance, le prenom d'un proche, ou le domaine d'un prix).")

REM --- 
REM --- CORRECTION: Suppression des drapeaux "-t" et "-p" non reconnus.
REM --- Le prompt est le dernier argument, sans drapeau.
REM --- Ajout de "2>&1" pour capturer les erreurs.
REM ---
gemini "%GEMINI_PROMPT%" > biographie_generee.txt 2>&1

REM --- Verification amelioree: Verifie si le fichier existe ET s'il n'est pas vide ---
if not exist biographie_generee.txt (
    echo ERREUR: Le fichier 'biographie_generee.txt' n'a pas ete cree.
    pause
    exit /b
)

REM --- La commande "for" recupere la taille (%%~zI) du fichier ---
for %%I in (biographie_generee.txt) do (
    if %%~zI EQU 0 (
        echo.
        echo ATTENTION: Le fichier genere est vide.
        echo Cela signifie que 'gemini-cli' n'a rien repondu (ou a echoue).
        echo Causes possibles: Pas de connexion internet, ou cle API non configuree.
        echo Le script va quand meme ouvrir le fichier pour que vous puissiez voir l'erreur.
    ) else (
        echo Le fichier 'biographie_generee.txt' a ete cree avec succes.
    )
)

echo.
echo Ouverture du fichier pour analyse...
echo Suivez maintenant les instructions du formateur et du fichier 'instructions_apprenant.md'.
echo.

REM --- Ouvre automatiquement le fichier genere dans le Bloc-notes ---
start notepad biographie_generee.txt

pause