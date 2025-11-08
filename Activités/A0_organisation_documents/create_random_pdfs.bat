@echo off
setlocal enabledelayedexpansion

set "outputDir=C:\Users\s.jaubert\OneDrive - CFAI Centre\IA\Cours\Activités\A0_organisation_documents\incoming"

if not exist "%outputDir%" (
    mkdir "%outputDir%"
)

for /L %%i in (1,1,50) do (
    set /a year=!random! %% 6 + 2020
    set /a month=!random! %% 12 + 1
    set /a day=!random! %% 28 + 1

    set "monthStr=!month!"
    if !month! lss 10 set "monthStr=0!month!"

    set "dayStr=!day!"
    if !day! lss 10 set "dayStr=0!day!"

    set "randomString=!random!!random!"

    set "fileName=!year!-!monthStr!-!dayStr!_!randomString!.pdf"
    
    echo Creating !fileName!
    type nul > "%outputDir%\!fileName!"
)

echo.
echo 50 PDF files created in %outputDir%
pause
