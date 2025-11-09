@echo off
chcp 65001 > nul
echo.
echo =================================================================
echo    EQUIPE B : Demonstration que le teletravail DIMINUE la productivite
echo =================================================================
echo.
echo Lancement de la requete a Gemini...
echo.

gemini < equipe_B_diminution.GEMINI.md > resultat_B.txt

echo.
echo =================================================================
echo                       FIN DE LA DEMONSTRATION
echo =================================================================
pause