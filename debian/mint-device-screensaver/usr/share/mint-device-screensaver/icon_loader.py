"""
icon_loader.py

Loads Adwaita SVG device icons.

This module only handles locating icons.
Animation is handled elsewhere.
"""

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



    def load_icons(self):

        """
        Finds all requested SVG files.
        """

        self.icons.clear()


        for filename in DEVICE_ICONS:

            path = ICON_DIRECTORY / filename


            if path.exists():

                self.icons.append(
                    path
                )


        return self.icons
