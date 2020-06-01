'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class Rectangle():
    """Class to model a rectangle.
    """

    def __init__(self, length, width):
        """Rectangle constructor.

        Args:
            length (int): rectangle side length.
            width (int): rectangle side width.

        """
        self.length = length
        self.width = width

    def __repr__(self):
        return f"Rectangle with {self.length} length and {self.width} width."


class Circle():
    """Class to model a circle.
    """

    def __init__(self, radius):
        """Circle constructor.

        Args:
            radius (int): circle radius in centimeters.

        """
        self.radius = radius

    def __repr__(self):
        return f"Circle with {self.radius} radius."


if __name__ == "__main__":
    r = Rectangle(100, 50)
    c = Circle(75)
    print(r, c)
    print("Rectangle area:", r.length * r.width)
    print("Rectangle perimeter:", r.length * 2 + r.width * 2)
    print("Circle circumference:", 2 * 3.14 * c.radius)
