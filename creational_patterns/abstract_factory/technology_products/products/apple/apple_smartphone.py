"""
Class that describes apple smartphone functionality.
"""
from ..base import Smartphone as Parent


class AppleSmartphone(Parent):
    def call(self):
        print("You call using smartphone by apple.")

    def turn_on(self):
        print("You turn on smartphone by apple.")

    def turn_off(self):
        print("you turn off smartphone by apple.")
