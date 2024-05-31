"""
Class that has business logic for android ui to describe main window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import MainWindow


class MacMainWindow(MainWindow):

    def open_help(self):
        print("Open help window on mac")

    def close_window(self):
        print("Close main window on mac")

    def open_settings(self):
        print("Open settings window on mac")

    def close_settings(self):
        print("Close settings window on mac")

    def close_help(self):
        print("Close  help window on mac")
