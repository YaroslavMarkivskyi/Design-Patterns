"""
Class that has business logic to describe main window.
"""
from abc import ABC, abstractmethod


class MainWindow(ABC):
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
    def open_help(self):
        pass

    @abstractmethod
    def close_help(self):
        pass
