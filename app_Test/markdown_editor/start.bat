@echo off
echo ========================================
echo   Lancement de Markdown Editor
echo ========================================
echo.

cd /d "c:\Users\s.jaubert\projets\Cours-IA\app_Test\markdown_editor"

REM Verifier si node_modules existe
if not exist "node_modules\" (
    echo [INFO] Installation des dependances necessaires...
    echo Cela peut prendre quelques minutes la premiere fois.
    echo.
    npm install
    if errorlevel 1 (
        echo.
        echo [ERREUR] L'installation a echoue.
        echo Verifiez que Node.js est installe sur votre systeme.
        pause
        exit /b 1
    )
    echo.
    echo [OK] Dependances installees avec succes !
    echo.
)

echo [INFO] Demarrage du serveur de developpement...
echo L'application sera accessible dans votre navigateur.
echo.
npm run dev

pause
