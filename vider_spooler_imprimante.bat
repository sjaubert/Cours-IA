@echo off
REM ========================================
REM Script pour vider le spooler d'imprimante
REM Ce script doit être exécuté en tant qu'administrateur
REM ========================================

echo ========================================
echo Vidage du spooler d'imprimante
echo ========================================
echo.

REM Vérification des privilèges administrateur
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ERREUR: Ce script doit être execute en tant qu'administrateur !
    echo Faites un clic droit sur le fichier et selectionnez "Executer en tant qu'administrateur"
    echo.
    pause
    exit /b 1
)

echo [1/3] Arret du service Spooler d'impression...
net stop spooler
if %errorLevel% neq 0 (
    echo ERREUR: Impossible d'arreter le service Spooler
    pause
    exit /b 1
)
echo Service arrete avec succes.
echo.

echo [2/3] Suppression des fichiers du spooler...
del /Q /F /S "%systemroot%\System32\spool\PRINTERS\*.*"
if %errorLevel% equ 0 (
    echo Fichiers supprimes avec succes.
) else (
    echo ATTENTION: Certains fichiers n'ont peut-etre pas pu etre supprimes.
)
echo.

echo [3/3] Redemarrage du service Spooler d'impression...
net start spooler
if %errorLevel% neq 0 (
    echo ERREUR: Impossible de redemarrer le service Spooler
    pause
    exit /b 1
)
echo Service redemarre avec succes.
echo.

echo ========================================
echo Operation terminee avec succes !
echo Le spooler d'imprimante a ete vide.
echo ========================================
echo.
pause
