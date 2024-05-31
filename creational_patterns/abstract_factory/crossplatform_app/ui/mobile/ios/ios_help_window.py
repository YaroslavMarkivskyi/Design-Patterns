"""
Class that has business logic for ios ui to describe help window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import HelpWindow


class IosHelpWindow(HelpWindow):
    def open_window(self):
        print("Open main window on ios")

    def close_window(self):
        print("Close main window on ios")

    def open_settings(self):
        print("Open settings window on ios")

    def close_settings(self):
        print("Close settings window on ios")

    def close_help(self):
        print("Close  help window on ios")
