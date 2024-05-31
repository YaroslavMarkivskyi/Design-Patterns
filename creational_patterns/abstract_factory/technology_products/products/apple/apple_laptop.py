"""
Class that describes apple laptop functionality.
"""
from ..base import Laptop as Parent


class AppleLaptop(Parent):
    def show_display(self):
        print("You see display on laptop by apple.")

    def turn_on(self):
        print("You turn on smartphone by apple.")

    def turn_off(self):
        print("you turn off smartphone by apple.")
