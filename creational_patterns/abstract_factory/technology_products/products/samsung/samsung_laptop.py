"""
Class that describes samsung laptop functionality.
"""
from ..base import Laptop as Parent


class SamsungLaptop(Parent):
    def show_display(self):
        print("You see display on laptop by samsung.")

    def turn_on(self):
        print("You turn on smartphone by samsung.")

    def turn_off(self):
        print("you turn off smartphone by samsung.")
