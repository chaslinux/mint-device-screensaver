"""
particles.py

Atmospheric particle system.

Creates:
- randomly distributed particles
- depth illusion
- slow drifting motion
- twinkling brightness
- configurable particle styles
"""

import random
import math

import cairo

from giimports import (
    Clutter,
    Cogl,
)



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


        self.x = random.uniform(
            0,
            width
        )

        self.y = random.uniform(
            0,
            height
        )


        self.depth = random.uniform(
            0.1,
            1.0
        )


        #
        # Particle size.
        #

        self.size = (
            2
            +
            self.depth * 7
        )


        self.speed_x = random.uniform(
            -100,
            100
        ) * self.depth


        self.speed_y = random.uniform(
            -100,
            100
        ) * self.depth


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


        self.render_shape()


        self.actor.set_size(
            self.size,
            self.size
        )



    def render_shape(self):

        """
        Render particle shape using Cairo.
        """

        size = 48


        surface = cairo.ImageSurface(
            cairo.FORMAT_ARGB32,
            size,
            size
        )


        context = cairo.Context(
            surface
        )


        context.set_source_rgba(
            1,
            1,
            1,
            1
        )


        center = size / 2


        if self.style == "square":

            context.rectangle(
                6,
                6,
                size - 12,
                size - 12
            )


        elif self.style == "star":

            points = 5

            outer = 18
            inner = 8


            for i in range(
                points * 2
            ):

                angle = (
                    -math.pi / 2
                    +
                    i * math.pi / points
                )


                radius = (
                    outer
                    if i % 2 == 0
                    else inner
                )


                x = (
                    center
                    +
                    math.cos(angle)
                    *
                    radius
                )

                y = (
                    center
                    +
                    math.sin(angle)
                    *
                    radius
                )


                if i == 0:

                    context.move_to(
                        x,
                        y
                    )

                else:

                    context.line_to(
                        x,
                        y
                    )


            context.close_path()


        else:

            context.arc(
                center,
                center,
                16,
                0,
                math.pi * 2
            )


        context.fill()


        surface.flush()


        image = Clutter.Image()


        image.set_data(
            bytes(
                surface.get_data()
            ),
            Cogl.PixelFormat.BGRA_8888,
            size,
            size,
            surface.get_stride()
        )


        self.actor.set_content(
            image
        )



    def update_colour(self):

        """
        Colour is stored in the Cairo image.
        Only opacity is animated.
        """

        self.actor.set_opacity(
            self.base_alpha
        )



    def update(
        self,
        delta,
        width,
        height
    ):

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


        self.actor.set_opacity(
            int(
                self.base_alpha
                *
                brightness
            )
        )


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
