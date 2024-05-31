"""
Class that has business logic for android ui to describe help window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import HelpWindow


class AndroidHelpWindow(HelpWindow):
    def open_window(self):
        print("Open main window on android")

    def close_window(self):
        print("Close main window on android")

    def open_settings(self):
        print("Open settings window on android")

    def close_settings(self):
        print("Close settings window on android")

    def close_help(self):
        print("Close  help window on android")
