"""
Global constants used throughout the project.
"""

from pathlib import Path

ICON_DIRECTORY = Path(
    "/usr/share/icons/Adwaita/scalable/devices"
)

FRAME_RATE = 60

BACKGROUND_COLOUR = (20, 20, 30)

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
