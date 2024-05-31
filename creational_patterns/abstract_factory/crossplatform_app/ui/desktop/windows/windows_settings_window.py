"""
Class that has business logic for windows ui to describe settings window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import SettingsWindow


class WindowsSettingsWindow(SettingsWindow):

    def open_window(self):
        print("Open main window on windows")

    def open_help(self):
        print("Open help window on windows")

    def close_window(self):
        print("Close main window on windows")

    def close_settings(self):
        print("Close settings window on windows")

    def close_help(self):
        print("Close  help window on windows")
