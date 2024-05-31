"""
Interface that describe business logic abstract factory for:
web ui,
desktop ui,
mobile ui.
"""
from abc import ABC, abstractmethod


class UiFactory(ABC):
    @abstractmethod
    def create_main_window(self):
        pass

    @abstractmethod
    def create_help_window(self):
        pass

    @abstractmethod
    def create_settings_window(self):
        pass
