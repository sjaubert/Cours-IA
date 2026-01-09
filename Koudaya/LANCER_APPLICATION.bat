@echo off
REM ============================================================
REM SATEBA - Analyseur PMET
REM Version portable avec verification des dependances
REM ============================================================

echo.
echo ========================================
echo   SATEBA - Analyseur PMET
echo ========================================
echo.

REM Verifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe
    echo.
    echo Veuillez executer INSTALLER.bat d'abord
    echo.
    pause
    exit /b 1
)

REM Verifier les dependances
echo Verification des dependances...
python -c "import pandas, matplotlib, openpyxl, numpy" >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Dependances manquantes
    echo.
    echo Veuillez executer INSTALLER.bat pour installer les dependances
    echo.
    pause
    exit /b 1
)

echo [OK] Toutes les dependances sont presentes
echo.
echo Lancement de l'application...
echo.

REM Lancer l'application
python pmet_app.py

if errorlevel 1 (
    echo.
    echo [ERREUR] L'application s'est terminee avec une erreur
    echo.
)

pause
