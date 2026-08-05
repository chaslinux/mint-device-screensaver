#!/usr/bin/env bash

#
# Mint Device Screensaver dependency installer
#
# Tested target:
# Linux Mint 22.3
#

set -e


echo "Updating package lists..."

sudo apt update


echo "Installing system dependencies..."


sudo apt install -y \
    python3 \
    python3-pip \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    gir1.2-clutter-1.0 \
    gir1.2-gtkclutter-1.0 \
    gir1.2-cogl-1.0 \
    gir1.2-rsvg-2.0 \
    libcairo2 \
    librsvg2-2


echo
echo "Checking Python GI imports..."


python3 - <<EOF
import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Clutter", "1.0")
gi.require_version("GtkClutter", "1.0")
gi.require_version("Rsvg", "2.0")

from gi.repository import Gtk, Clutter, GtkClutter, Rsvg

print("GI libraries loaded successfully")
EOF


echo
echo "Dependencies installed successfully."
echo
echo "Run the screensaver with:"
echo
echo "    python3 src/main.py"
echo
