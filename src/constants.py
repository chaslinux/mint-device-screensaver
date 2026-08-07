"""
Global constants used throughout the project.
"""

from pathlib import Path


ICON_DIRECTORY = Path(
    "/usr/share/icons/Adwaita/scalable/devices"
)


FRAME_RATE = 60
BACKGROUND_COLOUR = (20, 20, 30)
BACKGROUND_TRANSITION_START = 5.0
BACKGROUND_TRANSITION_DURATION = 15.0

# Alias used by configuration system
BACKGROUND_COLOR = BACKGROUND_COLOUR
ANIMATION_SPEED = 1.0


LOG_DIRECTORY = (
    Path.home()
    /
    ".local"
    /
    "state"
    /
    "mint-device-screensaver"
)


LOG_FILENAME = (
    LOG_DIRECTORY
    /
    "mint-device-screensaver.log"
)


WINDOW_TITLE = "Mint Device Screensaver"


EXIT_ON_MOUSE_MOVE = True
