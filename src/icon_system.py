"""
icon_system.py

Manages all animated device icons.
"""

from icon_loader import IconLoader
from icon_actor import IconActor



class IconSystem:


    def __init__(self, layer):

        self.layer = layer

        self.icons = []

        self.width = 1920
        self.height = 1080


        loader = IconLoader()

        icon_paths = loader.load_icons()


        print(
            "Creating icons:",
            len(icon_paths)
        )


        for path in icon_paths:

            icon = IconActor(
                path,
                layer,
                self.width,
                self.height
            )

            self.icons.append(
                icon
            )


        print(
            "Icons created:",
            len(self.icons)
        )



    def resize(
        self,
        width,
        height
    ):

        self.width = width
        self.height = height



    def update(
        self,
        delta
    ):

        for icon in self.icons:

            icon.update(
                delta,
                self.width,
                self.height
            )
