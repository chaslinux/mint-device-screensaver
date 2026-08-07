#!/usr/bin/env bash

set -e

echo
echo "=========================================="
echo " Mint Device Screensaver Debian Builder"
echo "=========================================="
echo

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

#
# Clean previous Debian build artifacts
#

echo "Cleaning previous Debian build artifacts..."

rm -f ../mint-device-screensaver_*.deb
rm -f ../mint-device-screensaver_*.changes
rm -f ../mint-device-screensaver_*.buildinfo
rm -f ../mint-device-screensaver_*.dsc
rm -f ../mint-device-screensaver_*.tar.xz

#
# Build package
#

echo
echo "Building Debian package..."

dpkg-buildpackage -us -uc -b

#
# Locate generated package
#

PACKAGE=$(ls -t ../mint-device-screensaver_*.deb | head -n1)

echo
echo "Build complete."
echo

echo "Package created:"
ls -lh "$PACKAGE"

echo
echo "Install with:"
echo
echo "  sudo dpkg -i $PACKAGE"
echo "  sudo apt install -f"
echo
