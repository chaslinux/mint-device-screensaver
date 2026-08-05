"""
trails.py

Holographic ghost trail effect.

Creates fading copies behind moving icons.
"""

import time

from giimports import Clutter



class TrailGhost:


    def __init__(
        self,
        source_actor,
        layer,
        x,
        y
    ):

        self.layer = layer

        self.age = 0

        self.lifetime = 1.2


        #
        # Create a copy actor.
        #

        self.actor = Clutter.Clone(
            source_actor
        )


        self.layer.add_child(
            self.actor
        )


        self.actor.set_position(
            x,
            y
        )


        self.actor.set_opacity(
            120
        )


        #
        # Slight hologram tint.
        #

        self.actor.set_color(
            Clutter.Color.new(
                80,
                220,
                255,
                255
            )
        )



    def update(
        self,
        delta
    ):

        self.age += delta


        progress = (
            self.age
            /
            self.lifetime
        )


        if progress >= 1.0:

            self.actor.destroy()

            return False


        #
        # Fade away.
        #

        opacity = int(
            120
            *
            (1.0 - progress)
        )


        self.actor.set_opacity(
            opacity
        )


        #
        # Slight expansion.
        #

        scale = (
            1.0
            +
            progress * 0.3
        )


        self.actor.set_scale(
            scale,
            scale
        )


        return True



class TrailSystem:


    def __init__(
        self,
        layer
    ):

        self.layer = layer

        self.trails = []

        self.timer = 0



    def add_trail(
        self,
        actor,
        x,
        y
    ):

        trail = TrailGhost(
            actor,
            self.layer,
            x,
            y
        )


        self.trails.append(
            trail
        )



    def update(
        self,
        delta
    ):

        remaining = []


        for trail in self.trails:

            if trail.update(delta):

                remaining.append(
                    trail
                )


        self.trails = remaining
