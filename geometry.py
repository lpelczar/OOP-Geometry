import math


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
            str: information bout shape
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
        self.check_if_args_not_below_zero(r)
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return 'Circle, r = {}'.format(r)


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.check_if_args_not_below_zero(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return 'Triangle, a = {}, b = {}, c = {}'.format(a, b, c)


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        super().__init__(a, a, a)

    def __str__(self):
        return 'EquilateralTriangle, a = {}'.format(a)


class Rectangle(Shape):

    def __init__(self, a, b):
        self.check_if_args_not_below_zero(a, b)
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * self.a + 2 * self.b

    def __str__(self):
        return 'Rectangle, a = {}, b = {}'.format(a, b)


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return 'Square, a = {}'.format(a)


class RegularPentagon(Shape):

    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a

    def get_area(self):
        return (self.a ** 2 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))) / 4

    def get_perimeter(self):
        return self.a * 5

    def __str__(self):
        return 'RegularPentagon, a = {}'.format(a)


class ShapeList:

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError
        self.shapes.append(shape)

    def get_largest_shape_by_perimeter(self):
        perimeters = list(map(lambda x: x.get_perimeter(), self.shapes))
        return self.shapes[perimeters.index(max(perimeters))]

    def get_largest_shape_by_area(self):
        areas = list(map(lambda x: x.get_area(), self.shapes))
        return self.shapes[areas.index(max(areas))]
