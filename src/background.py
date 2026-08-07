"""
background.py

Animated background layer.

Displays the configured colour initially,
then transitions into the dynamic colour field.
"""


import math

from giimports import Clutter

from constants import (
    BACKGROUND_TRANSITION_START,
    BACKGROUND_TRANSITION_DURATION,
)



class Background:


    def __init__(
        self,
        layer,
        color=(20, 20, 30)
    ):

        self.layer = layer

        self.time = 0.0

        self.base_color = color


        self.actor = Clutter.Actor()


        self.layer.add_child(
            self.actor
        )


        self.actor.set_background_color(
            Clutter.Color.new(
                color[0],
                color[1],
                color[2],
                255
            )
        )



    def resize(
        self,
        width,
        height
    ):

        self.actor.set_size(
            width,
            height
        )



    def update(
        self,
        delta
    ):

        self.time += delta



        #
        # Stronger animated colour movement.
        #

        animated_red = int(
            70 +
            60 *
            math.sin(
                self.time * 0.12
            )
        )


        animated_green = int(
            80 +
            70 *
            math.sin(
                self.time * 0.09 + 2
            )
        )


        animated_blue = int(
            130 +
            90 *
            math.sin(
                self.time * 0.07 + 4
            )
        )



        if self.time < BACKGROUND_TRANSITION_START:

            red = self.base_color[0]
            green = self.base_color[1]
            blue = self.base_color[2]


        else:

            amount = (
                self.time
                -
                BACKGROUND_TRANSITION_START
            ) / BACKGROUND_TRANSITION_DURATION


            amount = max(
                0.0,
                min(
                    1.0,
                    amount
                )
            )


            red = int(
                self.base_color[0]
                *
                (1 - amount)
                +
                animated_red
                *
                amount
            )


            green = int(
                self.base_color[1]
                *
                (1 - amount)
                +
                animated_green
                *
                amount
            )


            blue = int(
                self.base_color[2]
                *
                (1 - amount)
                +
                animated_blue
                *
                amount
            )



        self.actor.set_background_color(
            Clutter.Color.new(
                red,
                green,
                blue,
                255
            )
        )
