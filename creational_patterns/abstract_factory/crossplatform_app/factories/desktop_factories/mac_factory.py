"""
Class that describe business logic to create mac ui.
"""
from creational_patterns.abstract_factory.crossplatform_app \
    .factories.UiFactory import UiFactory
from creational_patterns.abstract_factory.crossplatform_app \
    .ui.desktop.mac import (MacHelpWindow, MacSettingsWindow, MacMainWindow)


class MacFactory(UiFactory):
    def create_main_window(self):
        return MacMainWindow()

    def create_help_window(self):
        return MacHelpWindow()

    def create_settings_window(self):
        return MacSettingsWindow()
