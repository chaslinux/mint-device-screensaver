"""
Mint Device Screensaver Settings

GTK settings application for configuring
Mint Device Screensaver.
"""

import logging

from giimports import Gtk

from config import Config


class SettingsWindow(Gtk.Window):

    def __init__(self):

        super().__init__(
            title="Mint Device Screensaver Settings"
        )

        self.set_border_width(20)
        self.set_default_size(
            400,
            250
        )

        self.config = Config()


        layout = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12
        )

        self.add(layout)


        title = Gtk.Label(
            label="Mint Device Screensaver Settings"
        )

        layout.pack_start(
            title,
            False,
            False,
            0
        )


        speed_title = Gtk.Label(
            label="Animation Speed"
        )

        layout.pack_start(
            speed_title,
            False,
            False,
            0
        )


        self.speed_scale = Gtk.Scale.new_with_range(
            Gtk.Orientation.HORIZONTAL,
            0.25,
            3.0,
            0.25
        )

        self.speed_scale.set_value(
            self.config.animation_speed
        )

        self.speed_scale.set_digits(2)


        layout.pack_start(
            self.speed_scale,
            False,
            False,
            0
        )


        self.mouse_check = Gtk.CheckButton(
            label="Exit screensaver when mouse moves"
        )

        self.mouse_check.set_active(
            self.config.exit_on_mouse_move
        )


        layout.pack_start(
            self.mouse_check,
            False,
            False,
            0
        )


        save_button = Gtk.Button(
            label="Save"
        )

        save_button.connect(
            "clicked",
            self.save_settings
        )


        layout.pack_start(
            save_button,
            False,
            False,
            0
        )


        self.connect(
            "destroy",
            Gtk.main_quit
        )



    def save_settings(self, button):

        logging.info(
            "Saving settings."
        )


        self.config.animation_speed = (
            self.speed_scale.get_value()
        )


        self.config.exit_on_mouse_move = (
            self.mouse_check.get_active()
        )


        self.config.save()



def main():

    window = SettingsWindow()

    window.show_all()

    Gtk.main()



if __name__ == "__main__":

    main()
