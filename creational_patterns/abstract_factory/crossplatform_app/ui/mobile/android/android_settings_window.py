"""
Class that has business logic for android ui to describe settings window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import SettingsWindow


class AndroidSettingsWindow(SettingsWindow):

    def open_window(self):
        print("Open main window on android")

    def open_help(self):
        print("Open help window on android")

    def close_window(self):
        print("Close main window on android")

    def close_settings(self):
        print("Close settings window on android")

    def close_help(self):
        print("Close  help window on android")
