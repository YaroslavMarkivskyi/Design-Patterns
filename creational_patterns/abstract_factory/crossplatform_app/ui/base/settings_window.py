"""
Class that has business logic to describe settings window.
"""
from abc import ABC, abstractmethod


class SettingsWindow(ABC):
    @abstractmethod
    def open_window(self):
        pass

    @abstractmethod
    def close_window(self):
        pass

    @abstractmethod
    def close_settings(self):
        pass

    @abstractmethod
    def open_help(self):
        pass

    @abstractmethod
    def close_help(self):
        pass
