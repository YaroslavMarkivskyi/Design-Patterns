"""
Class that describe business logic to create android ui.
"""
from creational_patterns.abstract_factory.crossplatform_app \
    .factories.UiFactory import UiFactory
from creational_patterns.abstract_factory.crossplatform_app \
    .ui.mobile.android import (AndroidHelpWindow,
                               AndroidSettingsWindow,
                               AndroidMainWindow
                               )


class AndroidFactory(UiFactory):
    def create_main_window(self):
        return AndroidMainWindow()

    def create_help_window(self):
        return AndroidHelpWindow()

    def create_settings_window(self):
        return AndroidSettingsWindow()
