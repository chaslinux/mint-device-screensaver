"""
Configuration loader.

Later versions will support a configuration file in
~/.config/mint-device-screensaver/

For now this simply exposes defaults.
"""

from constants import EXIT_ON_MOUSE_MOVE


class Config:

    def __init__(self):

        self.exit_on_mouse_move = EXIT_ON_MOUSE_MOVE
