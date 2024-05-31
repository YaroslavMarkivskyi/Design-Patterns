"""
Class that has business logic to describe help window.
"""
from abc import ABC, abstractmethod


class HelpWindow(ABC):
    @abstractmethod
    def open_window(self):
        pass

    @abstractmethod
    def close_window(self):
        pass

    @abstractmethod
    def open_settings(self):
        pass

    @abstractmethod
    def close_settings(self):
        pass

    @abstractmethod
    def close_help(self):
        pass
