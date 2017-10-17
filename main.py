import sys
import os
import random
from geometry import *

OPTION_TITLE_INDEX = 0
OPTION_FUNCTION_INDEX = 1


def handle_first_menu_option(shapes):
    """
    This feature allows user to add new shape to shapes list.
    User is able to choose what kind of shapes he/she wants to add.
    Then he/she should specify attributes that a given shape requires.

    :param shapes: ShapeList -> object of ShapeList class
    """
    SHAPE_NAME_INDEX = 0
    PARAMETERS_STARTING_INDEX = 1

    user_input = ask_for_shape_input()
    try:
        shape_info = user_input.split(',')
        shape_name = shape_info[SHAPE_NAME_INDEX]
        shape_args = [int(i) for i in shape_info[PARAMETERS_STARTING_INDEX:]]
        new_shape = SHAPE_TYPES[shape_name](*shape_args)
        shapes.add_shape(new_shape)
        print('\n{} added successfully!\n'.format(str(new_shape)))
    except:
        print('\nWrong input!\n')


def handle_second_menu_option(shapes):
    """
    This feature should print table containing all shapes added to the list.

    :param shapes: ShapeList -> object of ShapeList class
    """
    print(shapes.get_shapes_table())


def handle_third_menu_option(shapes):
    """
    This feature prints shape with the largest perimeter from a list.

    :param shapes: ShapeList -> object of ShapeList class
    """
    print(shapes.get_largest_shape_by_perimeter())
    print('\n')


def handle_fourth_menu_option(shapes):
    """
    This feature prints shape with the largest area from a list.

    :param shapes: ShapeList -> object of ShapeList class
    """
    print(shapes.get_largest_shape_by_area())
    print('\n')


def handle_fifth_menu_option(shapes):
    """
    This feature should allow user to choose shape type and print it's formulas (perimeter, area).

    :param shapes: ShapeList -> object of ShapeList class
    """
    shape_type = ask_for_shape_type()
    if shape_type in ['c', 't', 'et', 'r', 's', 'rp']:
        print_shape_formulas(SHAPE_TYPES[shape_type])
    else:
        print('\nWrong input\n')


def handle_sixth_menu_option(shapes):
    """
    This feature generate random shape. Then tell the user the type of shape and it's attributes.
    The user should calculate the perimeter and area. The program check users answer.

    :param shapes: ShapeList -> object of ShapeList class
    """
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
    """
    Exits the program.
    """
    sys.exit()


def generate_random_shape():
    """
    Generate random shape with given minimum and maximum number of each parameter needed.

    :return: Shape -> object of Shape class
    """
    min_parameter_number = 1
    max_parameter_number = 20
    SQUARE_PARAMS_NUM = 1
    RECTANGLE_PARAMS_NUM = 2
    TRIANGLE_PARAMS_NUM = 3

    shape_name = random.choice([i for i in SHAPE_TYPES.keys()])
    if shape_name in ['s', 'c', 'et', 'rp']:
        shape_args = [random.randint(min_parameter_number, max_parameter_number) for i in range(SQUARE_PARAMS_NUM)]
    elif shape_name in ['r']:
        shape_args = [random.randint(min_parameter_number, max_parameter_number) for i in range(RECTANGLE_PARAMS_NUM)]
    elif shape_name in ['t']:
        shape_args = [random.randint(min_parameter_number, max_parameter_number) for i in range(TRIANGLE_PARAMS_NUM)]
    return SHAPE_TYPES[shape_name](*shape_args)


def ask_for_shape_type():
    """
    Ask user for input about shape he want to choose.

    :return: string -> string with shape shortcut
    """
    shape = input('Choose shape type:\n' + ' Circle (c)\n' + ' Triangle (t)\n' + ' Equilateral Triangle (et)\n' +
                  ' Rectangle (r)\n' + ' Square (s)\n' + ' Regular Pentagon (rp)\n ').lower()
    return shape


def ask_for_shape_input():
    """
    Ask user for shape formula and return it as a string.

    :return: string -> formula for create a shape as a string
    """
    user_input = input('Enter data in the following syntax:\n' +
                       ' Circle -> c,<radius>\n' +
                       ' Triangle -> t,<a>,<b>,<c>\n' +
                       ' Equilateral Triangle -> et,<a>\n' +
                       ' Rectangle -> r,<a>,<b>\n' +
                       ' Square -> s,<a>\n' +
                       ' Regular Pentagon -> rp,<a>\n ').lower()
    return user_input


def print_shape_formulas(shape):
    """
    Print formula of area and perimeter for a given shape.

    :param shape: Shape -> object of Shape class
    """
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
            print(' (' + key + ') ' + value[OPTION_TITLE_INDEX])
        user_input = input("Type number of option: ")
        if (user_input not in OPTIONS):
            os.system('clear')
        else:
            os.system('clear')
            OPTIONS[user_input][OPTION_FUNCTION_INDEX](shapes)


if __name__ == "__main__":
    main()
