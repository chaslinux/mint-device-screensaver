"""
stage.py

Fullscreen GTK window containing the Clutter scene.
"""


from giimports import Gtk
from giimports import Gdk
from giimports import Clutter
from giimports import GtkClutter


from scene import Scene
from animation import AnimationManager



class ScreenSaverWindow(Gtk.Window):


    def __init__(self, application):

        super().__init__()


        self.application = application

        self.scene = None

        self.animation = None


        #
        # Enable mouse movement events
        #

        self.add_events(
            Gdk.EventMask.POINTER_MOTION_MASK
        )


        self.set_title(
            "Mint Device Screensaver"
        )


        self.fullscreen()


        self.connect(
            "destroy",
            Gtk.main_quit
        )


        self.connect(
            "key-press-event",
            self.on_key_press
        )


        self.connect(
            "motion-notify-event",
            self.on_mouse_move
        )


        self.connect(
            "realize",
            self.on_realize
        )


        self.connect(
            "size-allocate",
            self.on_resize
        )


        self.embed = GtkClutter.Embed()


        self.add(
            self.embed
        )


        self.stage = self.embed.get_stage()


        #
        # Load background from configuration
        #

        background = (
            self.application.config.background_color
        )


        self.stage.set_background_color(
            Clutter.Color.new(
                background[0],
                background[1],
                background[2],
                255
            )
        )



    def on_realize(self, widget):

        #
        # Hide cursor
        #

        window = self.get_window()


        if window:

            cursor = Gdk.Cursor.new_for_display(
                window.get_display(),
                Gdk.CursorType.BLANK_CURSOR
            )

            window.set_cursor(cursor)



        #
        # Create scene after window exists
        #

        if self.scene is None:

            self.scene = Scene(
                self.stage
            )


            self.animation = AnimationManager(
                self.scene
            )


            self.animation.start()



    def on_resize(self, widget, allocation):

        print(
            "GTK allocation:",
            allocation.width,
            allocation.height
        )


        if self.scene:

            self.scene.resize(
                allocation.width,
                allocation.height
            )



    def on_mouse_move(self, widget, event):

        if self.application.config.exit_on_mouse_move:

            if self.animation:

                self.animation.stop()


            Gtk.main_quit()



    def on_key_press(self, widget, event):

        if event.keyval == Gdk.KEY_Escape:

            if self.animation:

                self.animation.stop()


            Gtk.main_quit()
