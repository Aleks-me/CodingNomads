'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car():
    """Class to model a car.

    """

    def __init__(self, model, year, max_speed):
        """Car model constructor.

        Args:
            model (str): car model name.
            year (int): car model year of creation.
            max_speed (int): maximum car speed in km/h.

        """
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def gazu_gazu(self):
        """Increasing max_speed by 5 when called.

        """
        self.max_speed += 5

    def __repr__(self):
        return f"""This is a {self.model} car of {self.year} year \
and with max speed of {self.max_speed} km/h."""


if __name__ == "__main__":
    model = Car("Range Rover", 2008, 200)
    print(model)
    print("Can we go a little faster?")
    model.gazu_gazu()
    print(model)
