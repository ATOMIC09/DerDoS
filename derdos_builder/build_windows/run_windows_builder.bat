@echo off

REM Check if Nuitka is installed
echo Checking for Nuitka installation...
python -c "import nuitka" 2>nul
if %errorlevel% neq 0 (
    echo Nuitka is not installed. Installing now...
    pip install nuitka
) else (
    echo Nuitka is already installed.
)

REM Check if PyQt5 is installed
echo Checking for PyQt5 installation...
python -c "import PyQt5" 2>nul
if %errorlevel% neq 0 (
    echo PyQt5 is not installed. Installing now...
    pip install PyQt5
) else (
    echo PyQt5 is already installed.
)
echo.

REM Step 1: Run nuitka to build main.exe
echo 1. Running nuitka to build main.exe...
python -m nuitka --standalone ..\..\main.py --onefile --enable-plugin=pyqt5 --windows-icon-from-ico="..\asset\windows-logo.ico" --windows-console-mode=disable --company-name="ATOMIC09" --product-name="DerDos" --file-version=1.1 --product-version=1.1 --file-description="A Simple Denial of Service Tool with GUI" --copyright="Licensed under the GPLv3 License"
if %errorlevel% neq 0 (
    echo ! Nuitka failed to build the application.
    exit /b 1
)
echo / Nuitka build complete.
echo.

REM Step 2: Rename main.exe to DerDos.exe
echo 2. Renaming main.exe to DerDos.exe...
ren main.exe DerDos.exe
echo / Renaming complete.
echo.

REM Step 3: Clean up built artifacts
set /p cleanup="3. Do you want to remove the build directories (main.build, main.dist, main.onefile-build)? (y/n): "
if /i "%cleanup%"=="y" (
    rmdir /s /q main.build
    rmdir /s /q main.dist
    rmdir /s /q main.onefile-build
    echo / Cleanup complete.
) else if /i "%cleanup%"=="yes" (
    rmdir /s /q main.build
    rmdir /s /q main.dist
    rmdir /s /q main.onefile-build
    echo / Cleanup complete.
) else if /i "%cleanup%"=="Y" (
    rmdir /s /q main.build
    rmdir /s /q main.dist
    rmdir /s /q main.onefile-build
    echo / Cleanup complete.
) else (
    echo - Skipping cleanup.
)
echo.

REM Step 4: Echo run complete
echo / Run complete.
echo.
pause
