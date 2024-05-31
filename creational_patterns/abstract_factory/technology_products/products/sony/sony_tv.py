"""
Class that describes sony tv functionality.
"""
from ..base import Tv as Parent


class SonyTv(Parent):
    def connect_youtube(self):
        print("ypu watch youtube on tv by sony.")

    def turn_on(self):
        print("You turn on smartphone by sony.")

    def turn_off(self):
        print("you turn off smartphone by sony.")
