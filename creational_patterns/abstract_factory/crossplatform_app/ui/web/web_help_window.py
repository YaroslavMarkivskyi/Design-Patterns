"""
Class that has business logic for web ui to describe help window.
"""
from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import HelpWindow


class WebHelpWindow(HelpWindow):
    def open_window(self):
        print("Open main web")

    def close_window(self):
        print("Close main web")

    def open_settings(self):
        print("Open settings web")

    def close_settings(self):
        print("Close settings web")

    def close_help(self):
        print("Close  help web")
