"""
animation.py

Central animation clock.

Every animated object in the screensaver will eventually update from here.

This avoids having dozens of independent timers fighting each other.
"""

import logging
import time

from giimports import GLib



class AnimationManager:


    def __init__(self, scene):

        logging.debug(
            "Creating animation manager."
        )


        self.scene = scene

        self.running = False

        self.last_time = time.monotonic()


        self.speed = (
            self.scene.application.config.animation_speed
            if hasattr(self.scene, "application")
            else 1.0
        )


        logging.debug(
            "Animation speed: %s",
            self.speed
        )



    def start(self):

        if self.running:

            logging.debug(
                "Animation already running."
            )

            return


        self.running = True


        self.last_time = time.monotonic()


        interval = int(
            16 / self.speed
        )


        if interval < 1:

            interval = 1


        logging.debug(
            "Starting animation timer: interval=%sms",
            interval
        )


        GLib.timeout_add(
            interval,
            self.update
        )



    def update(self):

        if not self.running:

            logging.debug(
                "Animation stopped. Removing timer."
            )

            return False


        now = time.monotonic()

        delta = now - self.last_time

        self.last_time = now


        self.scene.update(
            delta * self.speed
        )


        return True



    def stop(self):

        if self.running:

            logging.debug(
                "Stopping animation."
            )


        self.running = False
