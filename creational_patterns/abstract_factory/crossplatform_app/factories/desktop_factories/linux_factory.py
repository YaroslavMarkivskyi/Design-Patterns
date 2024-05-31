"""
Class that describe business logic to create linux ui.
"""
from creational_patterns.abstract_factory.crossplatform_app \
    .factories.UiFactory import UiFactory
from creational_patterns.abstract_factory.crossplatform_app \
    .ui.desktop.linux import (LinuxHelpWindow,
                              LinuxSettingsWindow,
                              LinuxMainWindow)


class LinuxFactory(UiFactory):
    def create_main_window(self):
        return LinuxMainWindow()

    def create_help_window(self):
        return LinuxHelpWindow()

    def create_settings_window(self):
        return LinuxSettingsWindow()
