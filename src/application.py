"""
application.py

Main application controller.
"""

from giimports import Gtk

from config import Config
from utils import setup_logging
from stage import ScreenSaverWindow


class Application:

    def __init__(self):

        setup_logging()

        self.config = Config()

        self.window = None

    def run(self):

        self.window = ScreenSaverWindow(self)

        self.window.show_all()

        Gtk.main()
