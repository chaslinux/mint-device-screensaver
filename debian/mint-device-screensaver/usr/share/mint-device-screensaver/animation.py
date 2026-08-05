"""
animation.py

Central animation clock.

Every animated object in the screensaver will eventually update from here.

This avoids having dozens of independent timers fighting each other.
"""

import time

from giimports import GLib


class AnimationManager:

    def __init__(self, scene):

        self.scene = scene

        self.running = False

        self.last_time = time.monotonic()


    def start(self):

        if self.running:
            return

        self.running = True

        self.last_time = time.monotonic()

        #
        # Approximately 60 FPS.
        #
        GLib.timeout_add(
            16,
            self.update
        )


    def update(self):

        if not self.running:
            return False


        now = time.monotonic()

        delta = now - self.last_time

        self.last_time = now


        #
        # Future animation calls go here:
        #
        self.scene.update(delta)
        #


        return True


    def stop(self):

        self.running = False
