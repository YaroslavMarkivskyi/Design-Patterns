"""
Class that describes apple tv functionality.
"""
from ..base import Tv as Parent


class AppleTv(Parent):
    def connect_youtube(self):
        print("ypu watch youtube on tv by apple.")

    def turn_on(self):
        print("You turn on smartphone by apple.")

    def turn_off(self):
        print("you turn off smartphone by apple.")
