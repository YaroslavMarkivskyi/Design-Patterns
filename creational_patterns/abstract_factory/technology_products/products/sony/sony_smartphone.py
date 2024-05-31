"""
Class that describes sony smartphone functionality.
"""
from ..base import Smartphone as Parent


class SonySmartphone(Parent):
    def call(self):
        print("You call using smartphone by sony.")

    def turn_on(self):
        print("You turn on smartphone by sony.")

    def turn_off(self):
        print("you turn off smartphone by sony.")
