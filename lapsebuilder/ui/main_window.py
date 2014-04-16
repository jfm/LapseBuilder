from gi.repository import Gtk
from image_frame import ImageFrame
from filter_frame import FilterFrame
from settings_frame import SettingsFrame


class LapseBuilderWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="LapseBuilder")

        #Settings
        self.set_default_size(1000, 700)

        #Create and manipulate Grid Layout
        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)

        #Add Image Frame to window
        image_frame = ImageFrame(label='Image')
        image_frame.set_vexpand(True)
        image_frame.set_hexpand(True)
        grid.add(image_frame)

        #Add Settings Frame to window
        settings_frame = SettingsFrame(label='Project Settings')
        grid.attach_next_to(settings_frame, image_frame, Gtk.PositionType.RIGHT, 1, 2)

        #Add Filter Frame to Window
        filter_frame = FilterFrame(label='Video Settings')
        grid.attach_next_to(filter_frame, image_frame, Gtk.PositionType.BOTTOM, 1, 2)

        #Rendering Button
        renderer_button = Gtk.Button()
        renderer_button.set_label('Start Rendering')
        image = Gtk.Image(stock=Gtk.STOCK_MEDIA_PLAY)
        renderer_button.set_image(image)
        renderer_button.props.always_show_image = True
        renderer_button.set_image_position(Gtk.PositionType.LEFT)
        renderer_button.set_vexpand(False)
        renderer_button.set_hexpand(False)
        grid.attach_next_to(renderer_button, settings_frame, Gtk.PositionType.BOTTOM, 1, 1)

        self.add(grid)

window = LapseBuilderWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()