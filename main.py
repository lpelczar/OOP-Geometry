import sys
import os
import time
from geometry import *


def handle_first_menu_option(shapes):
    new_shape = input('Enter new shape: ')
    shapes.add_shape(new_shape)


def handle_second_menu_option(shapes):
    print(shapes.get_shapes_table())


def handle_third_menu_option(shapes):
    print(shapes.get_largest_shape_by_perimeter())


def handle_fourth_menu_option(shapes):
    print(shapes.get_largest_shape_by_area())


def handle_fifth_menu_option(shapes):
    shape_type = input('Choose shape type:\n' + ' Circle (c)\n' + ' Triangle (t)\n' +
                       ' Equilateral Triangle (et)\n' + ' Rectangle (r)\n' + ' Square (s)\n' +
                       ' Regular Pentagon (rp)\n ').upper()
    if shape_type in ['CIRCLE', 'C']:
        print_shape_formulas(Circle)
    elif shape_type in ['TRIANGLE', 'T', 'EQUILATERAL TRIANGLE', 'ET']:
        print_shape_formulas(Triangle)
    elif shape_type in ['RECTANGLE', 'R']:
        print_shape_formulas(Rectangle)
    elif shape_type in ['SQUARE', 'S']:
        print_shape_formulas(Square)
    elif shape_type in ['REGULAR PENTAGON', 'RP']:
        print_shape_formulas(RegularPentagon)
    else:
        print('\nWrong input\n')


def handle_sixth_menu_option(shapes):
    sys.exit()


def print_shape_formulas(shape):
    print('\nArea formula: {} Perimeter formula: {}\n'.format(shape.get_area_formula(), shape.get_perimeter_formula()))


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
        print('Learn Geometry.\n What do you want to do?')
        for key, value in OPTIONS.items():
            print(' (' + key + ') ' + value[0])
        user_input = input("Type number of option: ")
        if (user_input not in OPTIONS):
            os.system('clear')
        else:
            os.system('clear')
            OPTIONS[user_input][1](shapes)


if __name__ == "__main__":
    main()
