@echo off
chcp 65001 > nul
echo.
echo =================================================================
echo    EQUIPE A : Demonstration que le teletravail AUGMENTE la productivite
echo =================================================================
echo.
echo Lancement de la requete a Gemini...
echo.

gemini < equipe_A_augmentation.GEMINI.md > resultat_A.txt

echo.
echo =================================================================
echo                       FIN DE LA DEMONSTRATION
echo =================================================================
pause