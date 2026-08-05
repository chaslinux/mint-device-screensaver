"""
particles.py

Atmospheric particle system.

Creates soft drifting particles with:
- variable size
- depth illusion
- transparency
- gentle movement
"""

import random
import math

from giimports import Clutter



class Particle:


    def __init__(self, actor, width, height):

        self.actor = actor


        self.width = width
        self.height = height


        #
        # Position
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
        # Depth simulation.
        #
        # 0.2 = far away
        # 1.0 = close
        #

        self.depth = random.uniform(
            0.2,
            1.0
        )


        #
        # Size based on depth.
        #

        self.size = (
            2
            +
            self.depth * 7
        )


        #
        # Movement speed based on depth.
        #

        self.speed_x = random.uniform(
            -5,
            5
        ) * self.depth


        self.speed_y = random.uniform(
            -20,
            -5
        ) * self.depth


        #
        # Pulsing.
        #

        self.phase = random.uniform(
            0,
            math.pi * 2
        )


        self.base_alpha = random.randint(
            40,
            160
        )


        self.actor.set_size(
            self.size,
            self.size
        )


        self.update_colour()



    def update_colour(self):

        """
        Update particle brightness.
        """

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

        self.phase += delta


        #
        # Movement.
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
        # Gentle drifting.
        #

        self.x += (
            math.sin(
                self.phase
            )
            *
            self.depth
            *
            5
            *
            delta
        )


        #
        # Pulse brightness.
        #

        pulse = (
            0.7
            +
            math.sin(
                self.phase * 2
            )
            *
            0.3
        )


        alpha = int(
            self.base_alpha
            *
            pulse
        )


        self.actor.set_opacity(
            alpha
        )


        #
        # Wrap around.
        #

        if self.y < -20:

            self.y = height + 20


        if self.x < -20:

            self.x = width + 20


        if self.x > width + 20:

            self.x = -20


        self.actor.set_position(
            self.x,
            self.y
        )



class ParticleSystem:


    def __init__(self, layer):

        self.layer = layer

        self.particles = []

        self.width = 1920
        self.height = 1080


        #
        # Number of particles.
        #

        count = 100


        for i in range(count):

            actor = Clutter.Actor()


            layer.add_child(
                actor
            )


            particle = Particle(
                actor,
                self.width,
                self.height
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



    def update(self, delta):

        for particle in self.particles:

            particle.update(
                delta,
                self.width,
                self.height
            )
