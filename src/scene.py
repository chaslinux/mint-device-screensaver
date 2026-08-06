"""
scene.py

Owns the Clutter scene graph.

All visual layers live here.
"""

import logging

from giimports import Clutter

from background import Background
from particles import ParticleSystem
from icon_system import IconSystem



class Scene:


    def __init__(self, stage):

        logging.debug(
            "Initializing scene."
        )


        self.stage = stage


        self.root = Clutter.Actor()

        stage.add_child(
            self.root
        )


        logging.debug(
            "Creating background layer."
        )


        self.background = self.create_layer()

        self.background_effect = Background(
            self.background
        )


        logging.debug(
            "Creating ribbon layer."
        )


        self.ribbons = self.create_layer()


        logging.debug(
            "Creating particle layer."
        )


        self.particles = self.create_layer()

        self.particle_effect = ParticleSystem(
            self.particles
        )


        logging.debug(
            "Creating icon layer."
        )


        self.icons = self.create_layer()

        self.icon_effect = IconSystem(
            self.icons
        )


        logging.debug(
            "Creating overlay layer."
        )


        self.overlay = self.create_layer()


        logging.debug(
            "Scene initialization complete."
        )



    def create_layer(self):

        """
        Creates a transparent Clutter layer.
        """

        layer = Clutter.Actor()

        self.root.add_child(
            layer
        )


        return layer



    def resize(self, width, height):

        """
        Resize all layers when the window changes size.
        """


        logging.debug(
            "Resizing scene: %sx%s",
            width,
            height
        )


        for layer in (
            self.root,
            self.background,
            self.ribbons,
            self.particles,
            self.icons,
            self.overlay,
        ):

            layer.set_size(
                width,
                height
            )


        self.background_effect.resize(
            width,
            height
        )


        self.particle_effect.resize(
            width,
            height
        )


        self.icon_effect.resize(
            width,
            height
        )



    def update(self, delta):

        """
        Called once per animation frame.
        """


        self.background_effect.update(
            delta
        )


        self.particle_effect.update(
            delta
        )


        self.icon_effect.update(
            delta
        )
