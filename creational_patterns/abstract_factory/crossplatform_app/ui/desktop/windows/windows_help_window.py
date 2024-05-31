"""
Class that has business logic for windows ui to describe help window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import HelpWindow


class WindowsHelpWindow(HelpWindow):
    def open_window(self):
        print("Open main window on windows")

    def close_window(self):
        print("Close main window on windows")

    def open_settings(self):
        print("Open settings window on windows")

    def close_settings(self):
        print("Close settings window on windows")

    def close_help(self):
        print("Close  help window on windows")
