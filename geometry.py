import math
from texttable import Texttable


class Shape:
    """
    This is a abstract class representing geometrical shape.
    """

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        pass

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        pass

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        pass

    @classmethod
    def check_if_args_not_below_zero(cls, *args):
        """
        Check if any of args are not below 0

        Returns:
            bool: True if any of args are not below 0

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        if list(filter(lambda x: x < 0, args)):
            raise ValueError
        return True

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        pass


class Circle(Shape):

    def __init__(self, r):
        """
        Constructs an Circle object

        :param r: float -> radius of a circle
        """
        self.check_if_args_not_below_zero(r)
        self.r = r

    def get_area(self):
        """
        Calculates circle area using formula: π×r^2

        :return: float -> area of the circle
        """
        return math.pi * self.r ** 2

    def get_perimeter(self):
        """
        Calculates perimeter of circle using formula: 2×π×r

        :return: float -> perimeter of the circle
        """
        return 2 * math.pi * self.r

    def __str__(self):
        """
        Returns a formatted string with details about Circle.

        :return: string
        """
        return 'Circle, r={:0.2f}'.format(self.r)

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Circle as a string.

        :return: string
        """
        return 'π×r^2'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Circle as a string.

        :return: string
        """
        return '2×π×r'


class Triangle(Shape):

    def __init__(self, a, b, c):
        """
        Constructs a Triangle object

        :param a: float -> first side of triangle
        :param b: float -> second side of triangle
        :param c: float -> third side of triangle
        """
        self.check_if_args_not_below_zero(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """
        Calculates triangle area using formula: sqrt(s(s-a)(s-b)(s-c)) where s =(a+b+c)/2

        :return: float -> area of the triangle
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        """
        Calculates perimeter of triangle using formula: a+b+c

        :return: float -> perimeter of the trangle
        """
        return self.a + self.b + self.c

    def __str__(self):
        return 'Triangle, a={:0.2f}, b={:0.2f}, c={:0.2f}'.format(self.a, self.b, self.c)

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Triangle as a string.

        :return: string
        """
        return 'sqrt(s(s-a)(s-b)(s-c)) where s =(a+b+c)/2'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Triangle as a string.

        :return: string
        """
        return 'a+b+c'


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        """
        Constructs an EquilateralTriangle object

        :param a: float -> side of triangle
        """
        super().__init__(a, a, a)

    def __str__(self):
        """
        Returns a formatted string with details about EquilateralTriangle.

        :return: string
        """
        return 'EquilateralTriangle, a = {:0.2f}'.format(self.a)


class Rectangle(Shape):

    def __init__(self, a, b):
        """
        Constructs a Rectangle object

        :param a: float -> first side of rectangle
        :param b: float -> second side of rectangle
        """
        self.check_if_args_not_below_zero(a, b)
        self.a = a
        self.b = b

    def get_area(self):
        """
        Calculates rectangle area using formula: a×b

        :return: float -> area of the rectangle
        """
        return self.a * self.b

    def get_perimeter(self):
        """
        Calculates perimeter of rectangle using formula: 2a+2b

        :return: float -> perimeter of the rectangle
        """
        return 2 * self.a + 2 * self.b

    def __str__(self):
        """
        Returns a formatted string with details about Rectangle.

        :return: string
        """
        return 'Rectangle, a={:0.2f}, b={:0.2f}'.format(self.a, self.b)

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Rectangle as a string.

        :return: string
        """
        return 'a×b'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Rectangle as a string.

        :return: string
        """
        return '2a+2b'


class Square(Rectangle):

    def __init__(self, a):
        """
        Constructs a Square object

        :param a: float -> side of square
        """
        super().__init__(a, a)

    def __str__(self):
        """
        Returns a formatted string with details about Square.

        :return: string
        """
        return 'Square, a={:0.2f}'.format(self.a)

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Square as a string.

        :return: string
        """
        return 'a^2'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Square as a string.

        :return: string
        """
        return '4a'


class RegularPentagon(Shape):

    def __init__(self, a):
        """
        Constructs a RegularPentagon object

        :param a: float -> side of pentagon
        """
        self.check_if_args_not_below_zero(a)
        self.a = a

    def get_area(self):
        """
        Calculates regular pentagon area using formula: (a^2 sqrt(5(5+2sqrt(5))))/4

        :return: float -> area of the regular pentagon
        """
        return (self.a ** 2 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))) / 4

    def get_perimeter(self):
        """
        Calculates perimeter of regular pentagon using formula: 5a

        :return: float -> perimeter of the regular pentagon
        """
        return self.a * 5

    def __str__(self):
        """
        Returns a formatted string with details about RegularPentagon.

        :return: string
        """
        return 'RegularPentagon, a={:0.2f}'.format(self.a)

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for RegularPentagon as a string.

        :return: string
        """
        return '(a^2 sqrt(5(5+2sqrt(5))))/4'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for RegularPentagon as a string.

        :return: string
        """
        return '5a'


class ShapeList:

    def __init__(self):
        """
        Constructs a ShapeList object
        """
        self.shapes = []

    def add_shape(self, shape):
        """
        Adds shape to shapes list. This method check if shape's has Shape class as it's ancestor.
        If not it aise TypeError.
        :param shape: Shape -> Shape class object
        """
        if not isinstance(shape, Shape):
            raise TypeError
        self.shapes.append(shape)

    def get_shapes_table(self):
        """
        This method returns shapes list as string formatted into table.
        :return: string -> formatted table
        """
        t = Texttable()
        t.add_rows([['idx', 'Class', '__str__', 'Perimeter', 'Formula', 'Area', 'Formula']] +
                   [[self.shapes.index(s), type(s).__name__, str(s), s.get_perimeter(), s.get_perimeter_formula(),
                     s.get_area(), s.get_area_formula()] for s in self.shapes])
        return t.draw()

    def get_largest_shape_by_perimeter(self):
        """
        Returns shape with largest perimeter.
        :return: Shape -> object with largest perimeter
        """
        perimeters = list(map(lambda x: x.get_perimeter(), self.shapes))
        return self.shapes[perimeters.index(max(perimeters))]

    def get_largest_shape_by_area(self):
        """
        Returns shape with largest area.
        :return: Shape -> object with largest area
        """
        areas = list(map(lambda x: x.get_area(), self.shapes))
        return self.shapes[areas.index(max(areas))]
