@echo off
setlocal enabledelayedexpansion

REM --- Configuration ---
set "target_dir=%~dp0incoming"
set "num_files=500"
set "extensions=pdf docx txt jpg tmp bak md csv"

REM --- Create target directory if it doesn't exist ---
if not exist "%target_dir%" (
    echo Creating directory: %target_dir%
    mkdir "%target_dir%"
)

REM --- Create an array of extensions ---
set count=0
for %%e in (%extensions%) do (
    set "ext[!count!]=%%e"
    set /a count+=1
)

REM --- Main loop to create files ---
echo Creating %num_files% files...
for /l %%i in (1, 1, %num_files%) do (
    REM --- Generate random file name ---
    set "filename=file_%%i"
   
    REM --- Get random extension ---
    set /a "rand_ext_index=!RANDOM! %% %count%"
    set "random_ext=!ext[%rand_ext_index%]!"

    REM --- Generate random date ---
    set /a "rand_month=!RANDOM! %% 12 + 1"
    set /a "rand_day=!RANDOM! %% 28 + 1"

    REM --- Create the file ---
    echo "Dummy file %%i" > "%target_dir%\%filename%.!random_ext!"

    REM --- Set the creation and last write date using PowerShell ---
    powershell -NoProfile -Command "(Get-Item -Path '%target_dir%\%filename%.!random_ext!').CreationTime = (Get-Date -Year (Get-Date).Year -Month !rand_month! -Day !rand_day!)"
    powershell -NoProfile -Command "(Get-Item -Path '%target_dir%\%filename%.!random_ext!').LastWriteTime = (Get-Date -Year (Get-Date).Year -Month !rand_month! -Day !rand_day!)"
)

echo.
echo %num_files% dummy files have been successfully created in the '%target_dir%' directory.
echo You can run this script again at any time.

endlocal
pause