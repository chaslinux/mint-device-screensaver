"""
Mint Device Screensaver Settings

GTK settings application for configuring
Mint Device Screensaver.
"""


import logging

from giimports import Gtk, Gdk

from config import Config



class SettingsWindow(Gtk.Window):


    def __init__(self):

        super().__init__(
            title="Mint Device Screensaver Settings"
        )


        self.set_border_width(
            20
        )

        self.set_default_size(
            400,
            300
        )


        self.config = Config()


        layout = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12
        )

        self.add(
            layout
        )


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

        self.speed_scale.set_digits(
            2
        )


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



        color_title = Gtk.Label(
            label="Background Color"
        )


        layout.pack_start(
            color_title,
            False,
            False,
            0
        )



        self.color_button = Gtk.ColorButton()


        self.update_color_button()



        layout.pack_start(
            self.color_button,
            False,
            False,
            0
        )



        button_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=10
        )


        layout.pack_start(
            button_box,
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


        button_box.pack_start(
            save_button,
            True,
            True,
            0
        )



        reset_button = Gtk.Button(
            label="Reset to Defaults"
        )


        reset_button.connect(
            "clicked",
            self.reset_settings
        )


        button_box.pack_start(
            reset_button,
            True,
            True,
            0
        )



        self.connect(
            "destroy",
            Gtk.main_quit
        )



    def update_color_button(self):

        color = Gdk.RGBA()


        color.red = (
            self.config.background_color[0] / 255
        )

        color.green = (
            self.config.background_color[1] / 255
        )

        color.blue = (
            self.config.background_color[2] / 255
        )

        color.alpha = 1.0


        self.color_button.set_rgba(
            color
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


        color = (
            self.color_button
            .get_rgba()
        )


        self.config.background_color = (
            int(color.red * 255),
            int(color.green * 255),
            int(color.blue * 255)
        )


        self.config.save()



    def reset_settings(self, button):

        logging.info(
            "Resetting settings."
        )


        self.config.reset()


        self.speed_scale.set_value(
            self.config.animation_speed
        )


        self.mouse_check.set_active(
            self.config.exit_on_mouse_move
        )


        self.update_color_button()



def main():

    window = SettingsWindow()

    window.show_all()

    Gtk.main()



if __name__ == "__main__":

    main()
