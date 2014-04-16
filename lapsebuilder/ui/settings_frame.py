from gi.repository import Gtk
from system.system_tools import FileTools
from ui.image_frame import ImageFrame


class SettingsFrame(Gtk.Frame):
    source_folder_entry = Gtk.Entry()
    target_folder_entry = Gtk.Entry()

    def __init__(self, *args, **kwargs):
        super(SettingsFrame, self).__init__(*args, **kwargs)

        widget_grid = Gtk.Grid()
        widget_grid.set_row_spacing(5)
        widget_grid.set_column_spacing(5)

        #Source Folder
        source_label = Gtk.Label('Source Folder')
        source_label.set_alignment(0.02, 0.5)
        widget_grid.attach(source_label, 1, 1, 2, 1)
        widget_grid.attach_next_to(SettingsFrame.source_folder_entry, source_label, Gtk.PositionType.BOTTOM, 1, 1)
        source_folder_button = Gtk.Button("Browse")
        source_folder_button.connect("clicked", self.on_source_folder_button_clicked)
        widget_grid.attach_next_to(source_folder_button, SettingsFrame.source_folder_entry, Gtk.PositionType.RIGHT, 1, 1)

        #Target Folder
        target_label = Gtk.Label('Target Folder')
        target_label.set_alignment(0.02, 0.5)
        widget_grid.attach(target_label, 1, 3, 2, 1)
        widget_grid.attach_next_to(SettingsFrame.target_folder_entry, target_label, Gtk.PositionType.BOTTOM, 1, 1)
        target_folder_button = Gtk.Button("Browse")
        target_folder_button.connect("clicked", self.on_target_folder_button_clicked)
        widget_grid.attach_next_to(target_folder_button, SettingsFrame.target_folder_entry, Gtk.PositionType.RIGHT, 1, 1)

        #Target Movie File
        file_label = Gtk.Label('Target Filename')
        file_label.set_alignment(0.02, 0.5)
        widget_grid.attach_next_to(file_label, SettingsFrame.target_folder_entry, Gtk.PositionType.BOTTOM, 2, 1)
        file_entry = Gtk.Entry()
        widget_grid.attach_next_to(file_entry, file_label, Gtk.PositionType.BOTTOM, 2, 1)

        self.add(widget_grid)

    def on_source_folder_button_clicked(self, button):
        source_file_dialog = Gtk.FileChooserDialog('Select Source Folder', Gtk.Window(), Gtk.FileChooserAction.SELECT_FOLDER, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        response = source_file_dialog.run()

        if response == Gtk.ResponseType.OK:
            source_folder_path = source_file_dialog.get_filename()
            SettingsFrame.source_folder_entry.set_text(source_folder_path)
            source_file_list = FileTools.get_source_file_list(source_folder_path)
            ImageFrame.load_image(source_file_list[0])
        elif response == Gtk.ResponseType.CANCEL:
            pass

        source_file_dialog.destroy()

    def on_target_folder_button_clicked(self, button):
        target_file_dialog = Gtk.FileChooserDialog('Select Source Folder', Gtk.Window(), Gtk.FileChooserAction.SELECT_FOLDER, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        response = target_file_dialog.run()

        if response == Gtk.ResponseType.OK:
            SettingsFrame.target_folder_entry.set_text(target_file_dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            pass

        target_file_dialog.destroy()
