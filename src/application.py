"""
application.py

Main application controller.
"""

import logging

from giimports import Gtk

from config import Config
from utils import setup_logging
from stage import ScreenSaverWindow



class Application:


    def __init__(self, debug=False):

        self.debug = debug


        setup_logging(
            self.debug
        )


        logging.debug(
            "Creating configuration."
        )


        self.config = Config()


        self.window = None



    def run(self):

        logging.debug(
            "Creating screensaver window."
        )


        self.window = ScreenSaverWindow(
            self
        )


        self.window.show_all()


        logging.debug(
            "Starting GTK main loop."
        )


        Gtk.main()
