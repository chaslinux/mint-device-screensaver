"""
icon_loader.py

Loads Adwaita SVG device icons.

This module only handles locating icons.
Animation is handled elsewhere.
"""

import logging

from pathlib import Path

from constants import ICON_DIRECTORY



DEVICE_ICONS = [

    "audio-headphones.svg",
    "camera-web.svg",
    "computer.svg",
    "drive-harddisk.svg",
    "drive-removable-media.svg",
    "ebook-reader.svg",
    "input-gaming.svg",
    "input-keyboard.svg",
    "input-mouse.svg",
    "media-optical.svg",
    "microphone.svg",
    "video-display.svg",

]



class IconLoader:


    def __init__(self):

        self.icons = []


        logging.debug(
            "Icon loader initialized."
        )



    def load_icons(self):

        """
        Finds all requested SVG files.
        """

        logging.debug(
            "Searching for icons in: %s",
            ICON_DIRECTORY
        )


        self.icons.clear()


        for filename in DEVICE_ICONS:

            path = ICON_DIRECTORY / filename


            if path.exists():

                logging.debug(
                    "Found icon: %s",
                    filename
                )


                self.icons.append(
                    path
                )


            else:

                logging.warning(
                    "Missing icon: %s",
                    path
                )


        logging.info(
            "Loaded %s device icons.",
            len(self.icons)
        )


        return self.icons
