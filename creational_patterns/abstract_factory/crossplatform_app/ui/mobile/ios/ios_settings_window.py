"""
Class that has business logic for ios ui to describe settings window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import SettingsWindow


class IosSettingsWindow(SettingsWindow):

    def open_window(self):
        print("Open main window on ios")

    def open_help(self):
        print("Open help window on ios")

    def close_window(self):
        print("Close main window on ios")

    def close_settings(self):
        print("Close settings window on ios")

    def close_help(self):
        print("Close  help window on ios")
