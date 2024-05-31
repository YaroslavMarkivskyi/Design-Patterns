"""
Class that describe business logic to create ios ui.
"""
from creational_patterns.abstract_factory.crossplatform_app \
    .factories.UiFactory import UiFactory
from creational_patterns.abstract_factory.crossplatform_app \
    .ui.mobile.ios import (IosHelpWindow,
                           IosSettingsWindow,
                           IosMainWindow
                           )


class IosFactory(UiFactory):
    def create_main_window(self):
        return IosMainWindow()

    def create_help_window(self):
        return IosHelpWindow()

    def create_settings_window(self):
        return IosSettingsWindow()
