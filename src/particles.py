"""
particles.py

Starfield-style atmospheric particle system.

Creates:
- randomly distributed particles
- depth illusion
- slow drifting motion
- twinkling brightness
- configurable particle style support
"""

import random
import math

from giimports import Clutter



class Particle:


    def __init__(
        self,
        actor,
        width,
        height,
        style="circle"
    ):

        self.actor = actor
        self.style = style

        self.width = width
        self.height = height


        #
        # Random full-screen placement.
        #

        self.x = random.uniform(
            0,
            width
        )

        self.y = random.uniform(
            0,
            height
        )


        #
        # Depth:
        # small = far particle
        # large = near particle
        #

        self.depth = random.uniform(
            0.1,
            1.0
        )


        #
        # Particle size.
        #

        self.size = (
            1
            +
            self.depth * 5
        )


        #
        # Very slow random movement.
        #

        self.speed_x = random.uniform(
            -100,
            100
        ) * self.depth


        self.speed_y = random.uniform(
            -100,
            100
        ) * self.depth


        #
        # Twinkle timing.
        #

        self.phase = random.uniform(
            0,
            math.pi * 2
        )


        self.twinkle_speed = random.uniform(
            0.5,
            2.0
        )


        self.base_alpha = random.randint(
            50,
            180
        )


        self.apply_style()

        self.update_colour()



    def apply_style(self):

        """
        Apply particle appearance.

        Styles are currently prepared for:
        - circle
        - square
        - star

        Rendering remains intentionally simple while
        preserving current visual behaviour.
        """

        self.actor.set_size(
            self.size,
            self.size
        )


        if self.style not in (
            "circle",
            "square",
            "star"
        ):

            self.style = "circle"



    def update_colour(self):

        brightness = int(
            180
            +
            self.depth * 75
        )


        self.actor.set_background_color(
            Clutter.Color.new(
                brightness,
                brightness,
                255,
                self.base_alpha
            )
        )



    def update(
        self,
        delta,
        width,
        height
    ):

        #
        # Move particle.
        #

        self.x += (
            self.speed_x
            *
            delta
        )

        self.y += (
            self.speed_y
            *
            delta
        )


        #
        # Twinkle.
        #

        self.phase += (
            delta
            *
            self.twinkle_speed
        )


        brightness = (
            0.55
            +
            math.sin(self.phase)
            *
            0.45
        )


        alpha = int(
            self.base_alpha
            *
            brightness
        )


        self.actor.set_opacity(
            alpha
        )


        #
        # Wrap edges.
        #

        if self.x < 0:

            self.x = width

        elif self.x > width:

            self.x = 0


        if self.y < 0:

            self.y = height

        elif self.y > height:

            self.y = 0


        self.actor.set_position(
            self.x,
            self.y
        )



class ParticleSystem:


    def __init__(
        self,
        layer,
        count=180,
        style="circle"
    ):

        self.layer = layer
        self.style = style

        self.particles = []

        self.width = 1920
        self.height = 1080


        for i in range(count):

            actor = Clutter.Actor()


            layer.add_child(
                actor
            )


            particle = Particle(
                actor,
                self.width,
                self.height,
                self.style
            )


            self.particles.append(
                particle
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

        for particle in self.particles:

            particle.update(
                delta,
                self.width,
                self.height
            )
