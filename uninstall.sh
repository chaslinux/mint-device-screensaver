#!/usr/bin/env bash

set -e

echo
echo "=========================================="
echo " Mint Device Screensaver Uninstaller"
echo "=========================================="
echo

if ! dpkg -s mint-device-screensaver >/dev/null 2>&1; then

    echo "Mint Device Screensaver is not currently installed."
    echo
    exit 0

fi

echo "Removing Debian package..."
echo

sudo apt remove -y mint-device-screensaver

echo

read -rp "Remove your personal configuration and logs? [y/N] " ANSWER

if [[ "$ANSWER" =~ ^[Yy]$ ]]; then

    rm -rf "$HOME/.config/mint-device-screensaver"
    rm -rf "$HOME/.local/state/mint-device-screensaver"

    echo
    echo "Configuration and log files removed."

fi

echo
echo "Cinnamon lock and authentication settings have not been changed."
echo

echo "Uninstallation complete."
echo
