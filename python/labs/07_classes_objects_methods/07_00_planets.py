'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Planet():
    """A Planet class that models attributes and methods of the planet object.

    """

    def __init__(self, name, radius):
        """Planet genarator.

        Args:
            name (str): name of the planet.
          radius (int): radius of the planet.

        """
        self.name = name
        self.radius = radius

    def __repr__(self):
        return f"This is {self.name} planet with {self.radius} radius."


if __name__ == "__main__":
    a = Planet("Earth", 6371)
    print(a)
