"""
Configuration loader.

Loads user configuration from:

    ~/.config/mint-device-screensaver/config.ini

If the file does not exist, a default configuration file is created.
"""

import configparser
from pathlib import Path


from constants import (
    EXIT_ON_MOUSE_MOVE,
    ANIMATION_SPEED,
    BACKGROUND_COLOR,
)



class Config:


    def __init__(self):

        self.exit_on_mouse_move = EXIT_ON_MOUSE_MOVE

        self.animation_speed = ANIMATION_SPEED

        self.background_color = BACKGROUND_COLOR


        self.create_default_config()

        self.load()



    def config_path(self):

        return (
            Path.home()
            /
            ".config"
            /
            "mint-device-screensaver"
            /
            "config.ini"
        )



    def create_default_config(self):

        path = self.config_path()


        if path.exists():

            return


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



    def reset(self):

        path = self.config_path()


        if path.exists():

            path.unlink()


        self.create_default_config()


        #
        # Reload values from the new file.
        #

        self.load()



    def load(self):

        path = self.config_path()


        if not path.exists():

            return


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


        except (
            configparser.Error,
            ValueError
        ):

            #
            # Keep defaults if config is invalid.
            #

            pass



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

            return BACKGROUND_COLOR


        try:

            return (
                int(value[0:2], 16),
                int(value[2:4], 16),
                int(value[4:6], 16),
            )


        except ValueError:

            return BACKGROUND_COLOR
