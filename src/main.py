#!/usr/bin/env python3
"""
main.py

Entry point for the Mint Device Screensaver.
"""

import sys

from application import Application
from config import Config
from version import VERSION, APP_NAME



def main():

    if "--version" in sys.argv:

        print(
            f"{APP_NAME} {VERSION}"
        )

        return



    if "--show-config" in sys.argv:

        config = Config()


        print(
            "Configuration:"
        )

        print(
            f"  exit_on_mouse_move = {config.exit_on_mouse_move}"
        )

        print(
            f"  animation_speed = {config.animation_speed}"
        )

        print(
            f"  background_color = {config.background_color}"
        )


        print()


        print(
            "Config file:"
        )

        print(
            f"  {config.config_path()}"
        )

        return



    if "--reset-config" in sys.argv:

        config = Config()

        config.reset()


        print(
            "Configuration reset."
        )

        print(
            f"Created: {config.config_path()}"
        )

        return



    app = Application(
        debug="--debug" in sys.argv
    )


    app.run()



if __name__ == "__main__":

    main()
