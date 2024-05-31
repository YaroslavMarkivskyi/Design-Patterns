"""
Class that has business logic for web ui to describe main window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import MainWindow


class WebMainWindow(MainWindow):

    def open_help(self):
        print("Open help web")

    def close_window(self):
        print("Close main web")

    def open_settings(self):
        print("Open settings web")

    def close_settings(self):
        print("Close settings web")

    def close_help(self):
        print("Close  help web")
