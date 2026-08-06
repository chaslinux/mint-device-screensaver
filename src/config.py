"""
Configuration loader.

Loads user configuration from:

    ~/.config/mint-device-screensaver/config.ini

If the file does not exist, a default configuration file is created.
"""

import configparser
import logging
from pathlib import Path


from constants import (
    EXIT_ON_MOUSE_MOVE,
    ANIMATION_SPEED,
    BACKGROUND_COLOR,
)



class Config:


    def __init__(self):

        logging.debug(
            "Initializing configuration."
        )


        self.exit_on_mouse_move = EXIT_ON_MOUSE_MOVE

        self.animation_speed = ANIMATION_SPEED

        self.background_color = BACKGROUND_COLOR


        self.create_default_config()

        self.load()



    def config_path(self):

        path = (
            Path.home()
            /
            ".config"
            /
            "mint-device-screensaver"
            /
            "config.ini"
        )


        logging.debug(
            "Config path: %s",
            path
        )


        return path



    def create_default_config(self):

        path = self.config_path()


        if path.exists():

            logging.debug(
                "Existing config found."
            )

            return


        logging.debug(
            "Creating default configuration."
        )


        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        path.write_text(
            """# Mint Device Screensaver configuration

[general]
exit_on_mouse_move=true

[animation]
speed=1.0

[appearance]
background=#14141e
"""
        )


        logging.info(
            "Created default configuration: %s",
            path
        )



    def reset(self):

        path = self.config_path()


        logging.info(
            "Resetting configuration."
        )


        if path.exists():

            path.unlink()

            logging.debug(
                "Removed existing configuration."
            )


        self.create_default_config()


        self.load()



    def load(self):

        path = self.config_path()


        if not path.exists():

            logging.warning(
                "Configuration file missing: %s",
                path
            )

            return


        logging.debug(
            "Loading configuration."
        )


        parser = configparser.ConfigParser()


        try:

            parser.read(path)


            if parser.has_option(
                "general",
                "exit_on_mouse_move"
            ):

                self.exit_on_mouse_move = (
                    parser.getboolean(
                        "general",
                        "exit_on_mouse_move"
                    )
                )



            if parser.has_option(
                "animation",
                "speed"
            ):

                self.animation_speed = (
                    parser.getfloat(
                        "animation",
                        "speed"
                    )
                )



            if parser.has_option(
                "appearance",
                "background"
            ):

                self.background_color = (
                    self.parse_color(
                        parser.get(
                            "appearance",
                            "background"
                        )
                    )
                )


            logging.debug(
                "Configuration loaded: exit_on_mouse_move=%s speed=%s background=%s",
                self.exit_on_mouse_move,
                self.animation_speed,
                self.background_color
            )


        except (
            configparser.Error,
            ValueError
        ):

            logging.exception(
                "Invalid configuration. Using defaults."
            )



    def parse_color(self, value):

        """
        Convert #RRGGBB into RGB values.
        """

        value = (
            value
            .strip()
            .lstrip("#")
        )


        if len(value) != 6:

            logging.warning(
                "Invalid color value: %s",
                value
            )

            return BACKGROUND_COLOR


        try:

            return (
                int(value[0:2], 16),
                int(value[2:4], 16),
                int(value[4:6], 16),
            )


        except ValueError:

            logging.warning(
                "Invalid color value: %s",
                value
            )

            return BACKGROUND_COLOR
