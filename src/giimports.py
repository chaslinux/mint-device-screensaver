"""
giimports.py

Centralized imports for all GObject Introspection libraries.

Every other module imports Gtk, Clutter, etc. from here.

DO NOT call gi.require_version() anywhere else in the project.
"""

import gi

# GTK
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")

# Clutter
gi.require_version("Clutter", "1.0")
gi.require_version("GtkClutter", "1.0")
gi.require_version("Cogl", "1.0")

# SVG rendering
gi.require_version("Rsvg", "2.0")

from gi.repository import (
    Gtk,
    Gdk,
    Gio,
    GLib,
    GObject,
    Clutter,
    GtkClutter,
    Cogl,
    GdkPixbuf,
    Rsvg,
)

# Initialise GtkClutter once.
GtkClutter.init([])
