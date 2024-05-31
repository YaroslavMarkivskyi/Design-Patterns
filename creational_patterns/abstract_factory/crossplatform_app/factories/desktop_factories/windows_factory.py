"""
Class that describe business logic to create windows ui.
"""
from creational_patterns.abstract_factory.crossplatform_app \
    .factories.UiFactory import UiFactory
from creational_patterns.abstract_factory.crossplatform_app \
    .ui.desktop.windows import (WindowsHelpWindow,
                                WindowsSettingsWindow,
                                WindowsMainWindow)


class WindowsFactory(UiFactory):
    def create_main_window(self):
        return WindowsMainWindow()

    def create_help_window(self):
        return WindowsHelpWindow()

    def create_settings_window(self):
        return WindowsSettingsWindow()
