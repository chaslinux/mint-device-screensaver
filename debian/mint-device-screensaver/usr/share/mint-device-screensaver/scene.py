"""
scene.py

Owns the Clutter scene graph.

All visual layers live here.
"""

from giimports import Clutter

from background import Background
from particles import ParticleSystem
from icon_system import IconSystem



class Scene:


    def __init__(self, stage):

        self.stage = stage


        #
        # Root container
        #

        self.root = Clutter.Actor()

        stage.add_child(
            self.root
        )


        #
        # Background layer
        #

        self.background = self.create_layer()

        self.background_effect = Background(
            self.background
        )


        #
        # Future ribbon effects
        #

        self.ribbons = self.create_layer()


        #
        # Particle layer
        #

        self.particles = self.create_layer()

        self.particle_effect = ParticleSystem(
            self.particles
        )


        #
        # Device icon layer
        #

        self.icons = self.create_layer()

        self.icon_effect = IconSystem(
            self.icons
        )


        #
        # Overlay layer
        #

        self.overlay = self.create_layer()



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


        #
        # Resize background.
        #

        self.background_effect.resize(
            width,
            height
        )


        #
        # Resize particles.
        #

        self.particle_effect.resize(
            width,
            height
        )


        #
        # Resize icons.
        #

        self.icon_effect.resize(
            width,
            height
        )



    def update(self, delta):

        """
        Called once per animation frame.
        """

        #
        # Update animated background.
        #

        self.background_effect.update(
            delta
        )


        #
        # Update particles.
        #

        self.particle_effect.update(
            delta
        )


        #
        # Update device icons.
        #

        self.icon_effect.update(
            delta
        )
