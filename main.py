import sys
import os
from geometry import *


def handle_first_menu_option(shapes):
    pass


def handle_second_menu_option(shapes):
    pass


def handle_third_menu_option(shapes):
    pass


def handle_fourth_menu_option(shapes):
    pass


def handle_fifth_menu_option(shapes):
    pass


def handle_sixth_menu_option(shapes):
    sys.exit()


OPTIONS = {
    '1': ['Add new shape', handle_first_menu_option],
    '2': ['Show all shapes', handle_second_menu_option],
    '3': ['Show shape with the largest perimeter', handle_third_menu_option],
    '4': ['Show shape with the largest area', handle_fourth_menu_option],
    '5': ['Show formulas', handle_fifth_menu_option],
    '0': ['Exit program', handle_sixth_menu_option]}


def main():

    os.system('clear')
    shapes = ShapeList()
    while True:
        for key, value in OPTIONS.items():
            print('(' + key + ') ' + value[0])
        user_input = input("Type number of option: ")
        if (user_input not in OPTIONS):
            os.system('clear')
        else:
            os.system('clear')
            OPTIONS[user_input][1](shapes)


if __name__ == "__main__":
    main()
