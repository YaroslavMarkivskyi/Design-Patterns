"""
Class that has business logic for android ui to describe main window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import MainWindow


class AndroidMainWindow(MainWindow):

    def open_help(self):
        print("Open help window on android")

    def close_window(self):
        print("Close main window on android")

    def open_settings(self):
        print("Open settings window on android")

    def close_settings(self):
        print("Close settings window on android")

    def close_help(self):
        print("Close  help window on android")
