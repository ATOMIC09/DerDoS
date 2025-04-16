#!/bin/bash

# Check if npm is installed
if ! command -v npm &> /dev/null; then
  echo "⚠️  npm is not installed. Please install Node.js"
  exit 1
fi
# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
  echo "⚠️  Python 3 is not installed. Please install Python 3"
  exit 1
fi

# Function to install appdmg if not installed
install_appdmg() {
  if ! command -v appdmg &> /dev/null; then
    echo "⬇️  appdmg is not installed. Installing..."
    npm install -g appdmg
    if [ $? -ne 0 ]; then
      echo "⚠️  Failed to install appdmg."
      exit 1
    fi
    echo "✅ appdmg installed successfully."
  else
    echo "✅ appdmg is already installed."
  fi
}

# Function to install pyinstaller if not installed
install_pyinstaller() {
  if ! command -v pyinstaller &> /dev/null; then
    echo "⬇️  PyInstaller is not installed. Installing..."
    python3 -m pip install pyinstaller
    if [ $? -ne 0 ]; then
      echo "⚠️  Failed to install PyInstaller."
      exit 1
    fi
    echo "✅ PyInstaller installed successfully."
  else
    echo "✅ PyInstaller is already installed."
  fi
}

# Function to install PyQt6 if not installed
install_pyqt6() {
  if ! python3 -m pip show PyQt6 &> /dev/null; then
    echo "⬇️  PyQt6 is not installed. Installing..."
    python3 -m pip install PyQt6
    if [ $? -ne 0 ]; then
      echo "⚠️  Failed to install PyQt6."
      exit 1
    fi
    echo "✅ PyQt6 installed successfully."
  else
    echo "✅ PyQt6 is already installed."
  fi
}

# Function to check if a command exists and display its path
check_command() {
  if ! command -v "$1" &> /dev/null; then
    echo "⚠️  Error: $1 is not installed."
    if [ "$1" == "appdmg" ]; then
      install_appdmg
    elif [ "$1" == "pyinstaller" ]; then
      install_pyinstaller
    fi
  else
    location=$(command -v "$1")
    echo "✅ $1 is installed at: $location"
  fi
}

# Function to check if a Python package is installed and display its location
check_python_package() {
  if ! python3 -m pip show "$1" &> /dev/null; then
    echo "⚠️  Error: $1 is not installed."
    if [ "$1" == "PyQt6" ]; then
      install_pyqt6
    fi
  else
    location=$(python3 -c "import $1; print($1.__file__)")
    echo "✅ $1 is installed at: $location"
  fi
}

# Step 0: Check for dependencies
echo
echo "0️⃣  Checking for required dependencies..."
check_command appdmg
check_command pyinstaller
check_python_package PyQt6

# Step 1: Run pyinstaller to build main.app
echo
echo "1️⃣  Running pyinstaller to build main.app..."
pyinstaller --onefile --noconsole --icon=../asset/mac-logo.icns ../../main_mac.py
if [ $? -ne 0 ]; then
  echo "⚠️  PyInstaller failed to build the application."
  exit 1
fi
echo "✅ PyInstaller build complete."
echo

# Step 2: Copy "dist/main.app" to "DerDos.app"
if [ -d "dist/main.app" ]; then
  echo "2️⃣  Copying dist/main.app to DerDos.app..."
  cp -r "dist/main.app" "DerDos.app"
  echo "✅ Copy complete: dist/main.app to DerDos.app"
else
  echo "⚠️  dist/main.app not found! The build may have failed."
  exit 1
fi

# Step 3: Run appdmg to create the DMG file
echo
echo "3️⃣  Running appdmg to create derdos.dmg..."
appdmg derdos.json derdos.dmg
if [ $? -ne 0 ]; then
  echo "⚠️  appdmg command failed."
  exit 1
fi
echo
echo "✅ appdmg command executed successfully."
echo

# Step 4: Clean up built artifacts
read -p "4️⃣  Do you want to remove the build and dist directories? (y/n): " cleanup
if [ "$cleanup" == "y" ] || [ "$cleanup" == "Y" ]; then
  rm -rf build dist
  echo "✅ Cleanup complete."
else
  echo "⏭️  Skipping cleanup."
fi
echo

read -p "5️⃣  Do you want to remove the application files? (y/n): " cleanup
if [ "$cleanup" == "y" ] || [ "$cleanup" == "Y" ]; then
  rm -rf DerDos.app
  rm main.spec
  echo "✅ Cleanup complete."
else
  echo "⏭️  Skipping cleanup."
fi
echo

# Step 5: Echo run complete
echo "✅ Run complete."
echo
