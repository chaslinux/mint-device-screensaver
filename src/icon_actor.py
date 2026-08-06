"""
icon_actor.py

Represents one animated SVG device icon.

Rendering:
- SVG -> librsvg -> Cairo -> Clutter.Image

Animation:
- orbital drifting
- device-specific effects
- depth variation
- smooth staggered fade-in
- subtle depth breathing
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


        #
        # Depth simulation.
        #

        self.depth = random.uniform(
            0.25,
            1.0
        )


        #
        # Visible depth scaling.
        #

        self.base_scale = (
            0.65
            +
            self.depth * 0.45
        )


        #
        # Fade state.
        #

        self.opacity = 0

        self.target_opacity = 220


        self.fade_delay = random.uniform(
            0,
            6
        )


        self.width = width
        self.height = height

        self.image_data = None


        #
        # Actor.
        #

        self.actor = Clutter.Actor()

        self.layer.add_child(
            self.actor
        )


        #
        # Orbit.
        #

        self.home_x = random.uniform(
            150,
            max(151, width - 150)
        )

        self.home_y = random.uniform(
            150,
            max(151, height - 150)
        )


        self.orbit_x = random.uniform(
            30,
            180
        )

        self.orbit_y = random.uniform(
            30,
            120
        )


        self.orbit_x *= self.depth
        self.orbit_y *= self.depth


        self.orbit_speed = random.uniform(
            0.15,
            0.45
        )


        self.phase = random.uniform(
            0,
            math.pi * 2
        )


        self.render_svg()



    def detect_behaviour(self):

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


        #
        # Keep SVG resolution.
        #

        self.actor.set_size(
            size,
            size
        )


        self.actor.set_opacity(
            0
        )


        self.actor.show()



    def update(
        self,
        delta,
        width,
        height
    ):

        self.time += delta


        #
        # Fade in.
        #

        if (
            self.time > self.fade_delay
            and
            self.opacity < self.target_opacity
        ):

            self.opacity += (
                self.target_opacity
                *
                delta
                *
                0.8
            )


            if self.opacity > self.target_opacity:

                self.opacity = self.target_opacity


            self.actor.set_opacity(
                int(self.opacity)
            )


        #
        # Depth breathing.
        #

        breathing_scale = (
            self.base_scale
            +
            math.sin(
                self.time * 0.5
            )
            *
            0.03
        )


        self.actor.set_scale(
            breathing_scale,
            breathing_scale
        )


        #
        # Orbit movement.
        #

        x = (
            self.home_x
            +
            math.sin(
                self.time * self.orbit_speed
                +
                self.phase
            )
            *
            self.orbit_x
        )


        y = (
            self.home_y
            +
            math.cos(
                self.time * self.orbit_speed
                +
                self.phase
            )
            *
            self.orbit_y
        )


        self.actor.set_position(
            x,
            y
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
                math.sin(
                    self.time * 2
                )
                *
                0.1
            )


            self.actor.set_scale(
                breathing_scale * pulse,
                breathing_scale * pulse
            )


        elif self.behaviour == "bounce":

            self.actor.set_position(
                x,
                y + math.sin(self.time * 2) * 20
            )


        elif self.behaviour == "side":

            self.actor.set_position(
                x + math.sin(self.time) * 30,
                y
            )
