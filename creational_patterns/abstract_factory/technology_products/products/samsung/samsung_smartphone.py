"""
Class that describes samsung smartphone functionality.
"""
from ..base import Smartphone as Parent


class SamsungSmartphone(Parent):
    def call(self):
        print("You call using smartphone by samsung.")

    def turn_on(self):
        print("You turn on smartphone by samsung.")

    def turn_off(self):
        print("you turn off smartphone by samsung.")
