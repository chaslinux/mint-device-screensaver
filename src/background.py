"""
background.py

Animated background layer.

This will eventually contain:

- aurora ribbons
- gradients
- colour themes
- atmospheric effects

For now it creates a slowly shifting animated colour field.
"""


import math

from giimports import Clutter



class Background:


    def __init__(self, layer):

        self.layer = layer

        self.time = 0.0


        #
        # Create a full-screen rectangle.
        #

        self.actor = Clutter.Actor()


        self.layer.add_child(
            self.actor
        )


        self.actor.set_background_color(
            Clutter.Color.new(
                20,
                30,
                70,
                255
            )
        )



    def resize(self, width, height):

        self.actor.set_size(
            width,
            height
        )



    def update(self, delta):

        """
        Called every frame.
        """

        self.time += delta


        #
        # Slowly oscillating colours.
        #

        red = int(
            40 +
            30 *
            math.sin(self.time * 0.20)
        )


        green = int(
            50 +
            40 *
            math.sin(self.time * 0.15 + 2)
        )


        blue = int(
            90 +
            60 *
            math.sin(self.time * 0.10 + 4)
        )


        self.actor.set_background_color(
            Clutter.Color.new(
                red,
                green,
                blue,
                255
            )
        )
