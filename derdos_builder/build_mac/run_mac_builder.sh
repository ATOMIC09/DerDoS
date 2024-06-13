#!/bin/bash

# Function to check if a command exists
check_command() {
  if ! command -v "$1" &> /dev/null; then
    echo "Error: $1 is not installed."
    exit 1
  fi
}

# Step 0: Check for dependencies
echo
echo "0️⃣  Checking for required dependencies..."

check_command pyinstaller
echo "✅ PyInstaller is installed."

check_command appdmg
echo "✅ appdmg is installed."
echo

# Step 1: Run pyinstaller to build main.app
echo "1️⃣  Running pyinstaller to build main.app..."
pyinstaller --onefile --noconsole --icon=../asset/mac-logo.icns ../../main.py
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
  echo
else
  echo "⚠️  dist/main.app not found! The build may have failed."
  exit 1
fi

# Step 3: Run appdmg to create the DMG file
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

read -p "4️⃣  Do you want to remove the application files? (y/n): " cleanup
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
