"""
Class that describe business logic to create web ui.
"""
from creational_patterns.abstract_factory.crossplatform_app \
    .factories.UiFactory import UiFactory
from creational_patterns.abstract_factory.crossplatform_app \
    .ui.web import (WebHelpWindow,
                    WebSettingsWindow,
                    WebMainWindow
                    )


class WebFactory(UiFactory):
    def create_main_window(self):
        return WebMainWindow()

    def create_help_window(self):
        return WebHelpWindow()

    def create_settings_window(self):
        return WebSettingsWindow()
