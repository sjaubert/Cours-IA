@echo off
REM ============================================================
REM SATEBA - Analyseur PMET - Installation des dependances
REM ============================================================

echo.
echo ========================================
echo   SATEBA - Installation
echo ========================================
echo.

REM Verifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH
    echo.
    echo Telechargez Python depuis: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python detecte
python --version

echo.
echo Installation des dependances Python...
echo.

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERREUR] Installation echouee
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Installation terminee avec succes!
echo ========================================
echo.
echo Vous pouvez maintenant lancer l'application avec:
echo   LANCER_APPLICATION.bat
echo.
pause
