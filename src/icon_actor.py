"""
icon_actor.py

Represents one animated SVG device icon.

Loads an SVG using librsvg, renders it through Cairo,
and displays it as a Clutter image actor.

Stable version:
- SVG rendering through librsvg
- Cairo rendering
- Clutter.Image display
- Gentle floating motion
- Device-specific animation
"""

import math
import random
import os

import cairo

from giimports import (
    Clutter,
    Cogl,
    Rsvg,
)



class IconActor:


    def __init__(
        self,
        svg_path,
        layer,
        width=1920,
        height=1080
    ):

        self.svg_path = svg_path

        self.icon_name = os.path.basename(
            str(svg_path)
        )

        self.behaviour = self.detect_behaviour()

        self.layer = layer

        self.time = random.random() * 10

        self.width = width
        self.height = height


        #
        # Keep pixel data alive.
        #

        self.image_data = None


        #
        # Create actor.
        #

        self.actor = Clutter.Actor()


        self.layer.add_child(
            self.actor
        )


        #
        # Fixed home position.
        #
        # Animation moves around this point.
        #

        self.home_x = random.uniform(
            100,
            width - 100
        )

        self.home_y = random.uniform(
            100,
            height - 100
        )


        self.render_svg()



    def detect_behaviour(self):

        """
        Select animation style based on icon name.
        """

        name = self.icon_name


        if "headphones" in name:
            return "rotate"

        if "optical" in name:
            return "spin"

        if "keyboard" in name:
            return "tilt"

        if "mouse" in name:
            return "side"

        if "camera" in name:
            return "pulse"

        if "microphone" in name:
            return "bounce"

        if "display" in name:
            return "hover"

        if "harddisk" in name:
            return "rotate"

        if "gaming" in name:
            return "playful"

        if "ebook" in name:
            return "tilt"

        return "float"



    def render_svg(self):

        """
        Render SVG into a Clutter.Image.

        Keeps image memory alive for Clutter.
        """

        size = 160


        surface = cairo.ImageSurface(
            cairo.FORMAT_ARGB32,
            size,
            size
        )


        context = cairo.Context(
            surface
        )


        handle = Rsvg.Handle.new_from_file(
            str(self.svg_path)
        )


        handle.render_cairo(
            context
        )


        surface.flush()


        #
        # Keep buffer alive.
        #

        self.image_data = bytes(
            surface.get_data()
        )


        image = Clutter.Image()


        image.set_data(
            self.image_data,
            Cogl.PixelFormat.BGRA_8888,
            size,
            size,
            surface.get_stride()
        )


        self.actor.set_content(
            image
        )


        self.actor.set_size(
            size,
            size
        )


        self.actor.set_scale(
            1.0,
            1.0
        )


        self.actor.set_opacity(
            255
        )


        self.actor.show()


        #
        # Initial placement.
        #

        self.actor.set_position(
            self.home_x,
            self.home_y
        )



    def update(
        self,
        delta,
        width,
        height
    ):

        """
        Animate icon around its home position.
        """

        self.time += delta


        #
        # Gentle floating motion.
        #

        offset_x = (
            math.sin(self.time)
            *
            50
        )

        offset_y = (
            math.cos(self.time * 0.7)
            *
            50
        )


        self.actor.set_position(
            self.home_x + offset_x,
            self.home_y + offset_y
        )


        #
        # Device-specific effects.
        #

        if self.behaviour == "rotate":

            self.actor.set_rotation(
                Clutter.RotateAxis.Z_AXIS,
                self.time * 10,
                0,
                0,
                0
            )


        elif self.behaviour == "spin":

            self.actor.set_rotation(
                Clutter.RotateAxis.Z_AXIS,
                self.time * 35,
                0,
                0,
                0
            )


        elif self.behaviour == "tilt":

            self.actor.set_rotation(
                Clutter.RotateAxis.Z_AXIS,
                math.sin(self.time) * 8,
                0,
                0,
                0
            )


        elif self.behaviour == "pulse":

            pulse = (
                1.0
                +
                math.sin(self.time * 2)
                *
                0.1
            )


            self.actor.set_scale(
                pulse,
                pulse
            )


        elif self.behaviour == "bounce":

            self.actor.set_position(
                self.home_x,
                self.home_y
                +
                math.sin(self.time * 2) * 30
            )


        elif self.behaviour == "side":

            self.actor.set_position(
                self.home_x
                +
                math.sin(self.time) * 40,
                self.home_y
            )
