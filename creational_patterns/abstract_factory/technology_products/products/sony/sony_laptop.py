"""
Class that describes sony laptop functionality.
"""
from ..base import Laptop as Parent


class SonyLaptop(Parent):
    def show_display(self):
        print("You see display on laptop by sony.")

    def turn_on(self):
        print("You turn on smartphone by sony.")

    def turn_off(self):
        print("you turn off smartphone by sony.")
