"""
Class that has business logic for web ui to describe settings window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import SettingsWindow


class WebSettingsWindow(SettingsWindow):

    def open_window(self):
        print("Open main web")

    def open_help(self):
        print("Open help web")

    def close_window(self):
        print("Close main web")

    def close_settings(self):
        print("Close settings web")

    def close_help(self):
        print("Close  help web")
