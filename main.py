import sys
import os
import time
import random
from geometry import *


def handle_first_menu_option(shapes):
    user_input = ask_for_shape_input()
    try:
        shape_info = user_input.split(',')
        shape_name = shape_info[0]
        shape_args = [int(i) for i in shape_info[1:]]
        new_shape = SHAPE_TYPES[shape_name](*shape_args)
        shapes.add_shape(new_shape)
        print('\n{} added successfully!\n'.format(str(new_shape)))
    except:
        print('\nWrong input!\n')


def handle_second_menu_option(shapes):
    print(shapes.get_shapes_table())


def handle_third_menu_option(shapes):
    print(shapes.get_largest_shape_by_perimeter())
    print('\n')


def handle_fourth_menu_option(shapes):
    print(shapes.get_largest_shape_by_area())
    print('\n')


def handle_fifth_menu_option(shapes):
    shape_type = ask_for_shape_type()
    if shape_type in ['c', 't', 'et', 'r', 's', 'rp']:
        print_shape_formulas(SHAPE_TYPES[shape_type])
    else:
        print('\nWrong input\n')


def handle_sixth_menu_option(shapes):
    random_shape = generate_random_shape()
    print('I have generated shape for you, which is {}\n'.format(str(random_shape)))
    while True:
        try:
            area = int(input('Enter the area: '))
            perimeter = int(input('Enter the perimeter: '))
            break
        except ValueError:
            print('Wrong input!')
    if abs(area - random_shape.get_area()) < 0.1 and abs(perimeter - random_shape.get_perimeter()) < 0.1:
        print('Correct!\n')
    else:
        print('You are wrong! Area: {:0.2f} Perimeter: {:0.2f}\n'.format(random_shape.get_area(),
                                                                         random_shape.get_perimeter()))


def handle_seventh_menu_option(shapes):
    sys.exit()


def generate_random_shape():
    min_parameter_number = 1
    max_parameter_number = 20

    shape_name = random.choice([i for i in SHAPE_TYPES.keys()])
    if shape_name in ['s', 'c', 'et', 'rp']:
        shape_args = [random.randint(min_parameter_number, max_parameter_number) for i in range(1)]
    elif shape_name in ['r']:
        shape_args = [random.randint(min_parameter_number, max_parameter_number) for i in range(2)]
    elif shape_name in ['t']:
        shape_args = [random.randint(min_parameter_number, max_parameter_number) for i in range(3)]
    return SHAPE_TYPES[shape_name](*shape_args)


def ask_for_shape_type():
    shape = input('Choose shape type:\n' + ' Circle (c)\n' + ' Triangle (t)\n' + ' Equilateral Triangle (et)\n' +
                  ' Rectangle (r)\n' + ' Square (s)\n' + ' Regular Pentagon (rp)\n ').lower()
    return shape


def ask_for_shape_input():
    user_input = input('Enter data in the following syntax:\n' +
                       ' Circle -> c,<radius>\n' +
                       ' Triangle -> t,<a>,<b>,<c>\n' +
                       ' Equilateral Triangle -> et,<a>\n' +
                       ' Rectangle -> r,<a>,<b>\n' +
                       ' Square -> s,<a>\n' +
                       ' Regular Pentagon -> rp,<a>\n ').lower()
    return user_input


def print_shape_formulas(shape):
    print('\nArea formula: {} Perimeter formula: {}\n'.format(shape.get_area_formula(), shape.get_perimeter_formula()))


SHAPE_TYPES = {'c': Circle,
               't': Triangle,
               'et': EquilateralTriangle,
               'r': Rectangle,
               's': Square,
               'rp': RegularPentagon}

OPTIONS = {
    '1': ['Add new shape', handle_first_menu_option],
    '2': ['Show all shapes', handle_second_menu_option],
    '3': ['Show shape with the largest perimeter', handle_third_menu_option],
    '4': ['Show shape with the largest area', handle_fourth_menu_option],
    '5': ['Show formulas', handle_fifth_menu_option],
    '6': ['Quiz mode', handle_sixth_menu_option],
    '0': ['Exit program', handle_seventh_menu_option]}


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
