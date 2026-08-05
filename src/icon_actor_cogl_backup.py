"""
icon_actor.py

Represents one animated SVG device icon.

Loads an SVG using librsvg, renders it through Cairo,
and displays it as a Clutter image actor.

Stable baseline version:
- SVG rendering
- Clutter image actor
- floating motion
- device-specific effects

No depth scaling yet.
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
        # Create actor.
        #

        self.actor = Clutter.Actor()


        self.layer.add_child(
            self.actor
        )


        #
        # Start positions.
        #

        self.x = random.uniform(
            100,
            width - 100
        )

        self.y = random.uniform(
            100,
            height - 100
        )


        self.render_svg()



    def detect_behaviour(self):

        """
        Select animation style from icon filename.
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


        image = Clutter.Image()


        image.set_data(
            surface.get_data(),
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


        #
        # Force normal visibility.
        #

        self.actor.set_scale(
            1.0,
            1.0
        )


        self.actor.set_opacity(
            255
        )


        self.actor.show()



    def update(
        self,
        delta,
        width,
        height
    ):

        """
        Animate icon.
        """

        self.time += delta


        #
        # Gentle floating movement.
        #

        self.x += (
            math.sin(self.time)
            *
            delta
            *
            15
        )


        self.y += (
            math.cos(self.time * 0.7)
            *
            delta
            *
            10
        )


        #
        # Device effects.
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

            self.y += (
                math.sin(self.time * 2)
                *
                delta
                *
                5
            )


        elif self.behaviour == "side":

            self.x += (
                math.sin(self.time)
                *
                delta
                *
                5
            )


        #
        # Keep icons visible.
        #

        if self.x < -200:
            self.x = width + 200


        if self.x > width + 200:
            self.x = -200


        if self.y < -200:
            self.y = height + 200


        if self.y > height + 200:
            self.y = -200


        self.actor.set_position(
            self.x,
            self.y
        )
