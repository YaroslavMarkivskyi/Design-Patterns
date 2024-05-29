"""
Factory interface.
"""
from abc import ABC, abstractmethod


class LogisticCreator(ABC):
    @abstractmethod
    def create_deliver(self):
        pass
