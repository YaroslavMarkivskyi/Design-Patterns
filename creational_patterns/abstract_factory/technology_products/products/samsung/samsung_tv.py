"""
Class that describes samsung tv functionality.
"""
from ..base import Tv as Parent


class SamsungTv(Parent):
    def connect_youtube(self):
        print("ypu watch youtube on tv by samsung.")

    def turn_on(self):
        print("You turn on smartphone by samsung.")

    def turn_off(self):
        print("you turn off smartphone by samsung.")
