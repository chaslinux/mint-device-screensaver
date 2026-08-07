#!/usr/bin/env bash

set -e

echo
echo "=========================================="
echo " Mint Device Screensaver Installer"
echo "=========================================="
echo

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

#
# Check for Cinnamon
#

if ! command -v cinnamon-screensaver-command >/dev/null 2>&1; then

    echo "Warning:"
    echo
    echo "Cinnamon does not appear to be installed."
    echo
    echo "Mint Device Screensaver was designed for"
    echo "the Linux Mint Cinnamon desktop."
    echo

    read -rp "Continue anyway? [y/N] " ANSWER

    if [[ ! "$ANSWER" =~ ^[Yy]$ ]]; then

        echo
        echo "Installation cancelled."
        exit 1

    fi

fi


echo "Installing required dependencies..."

./install-dependencies.sh


echo
echo "Building Debian package..."

./debian/build-deb.sh


PACKAGE=$(ls -t ../mint-device-screensaver_*.deb | head -n1)


echo
echo "Installing package:"
echo "  $PACKAGE"
echo

sudo dpkg -i "$PACKAGE" || sudo apt install -f -y


echo
echo "Installation complete."
echo

echo "Mint Device Screensaver has been installed as a standalone application."

echo
echo "Cinnamon lock and authentication settings have not been changed."
echo "Mint Device Screensaver runs as a standalone application."
echo "The application can be launched manually from the menu"
echo "or from a terminal using:"
echo
echo "  mint-device-screensaver"
echo


read -rp "Launch a test now? [Y/n] " ANSWER

if [[ ! "$ANSWER" =~ ^[Nn]$ ]]; then

    mint-device-screensaver

fi


echo
echo "Done."
echo
