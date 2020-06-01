'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class Pen():
    """Pen class.

    Args:
        tip_protect (list): type of the pen tip protection,
                    ["no tip protection", "cap", "click_button", "rotation"]
        draw_type (list): type of pen writing method,
                        ["ballpoint", "drawing", "fountain", "rollerball"]
        ink_type (list): type of the ink that pen uses,
                        ["water-based", "oil-based", "gel"]

    """

    tip_protect = ["no tip protection", "cap", "click_button", "rotation"]
    draw_type = ["ballpoint", "drawing", "fountain", "rollerball"]
    ink_type = ["water-based", "oil-based", "gel"]

    def __init__(self, amount, length, tip=0, draw=0, ink=0):
        """Pen constructor.

        Args:
            amount (int): number of pens.
            length (int): pen length.
            tip (int): type of tip protection, from 0 to 3.
            draw (int): pen method of drawing, from 0 to 3.
            ink (int): pen ink type, from 0 to 2.

        """
        self.amount = amount
        self.length = length
        self.tip = tip
        self.draw = draw
        self.ink = ink

    def __str__(self):
        """Print decoded pen info."""
        return f"""Pen, {self.amount} unit, with {Pen.tip_protect[self.tip]}, \
{Pen.draw_type[self.draw]} draw type, with {Pen.ink_type[self.ink]} ink and \
{self.length} mm length"""

    def __add__(self, n_items):
        summa = self.amount + n_items
        return Pen(summa, self.length, self.tip, self.draw, self.ink)


class Slippers():
    """Slippers class.

    Args:
        design: (list): slippers design, ["classic", "modern"]
        sizes (list): slippers sizes, [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

    """

    designs = ["classic", "modern"]
    sizes = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

    def __init__(self, amount, design=0, size=7):
        """Slippers constructor.

        Args:
            amount (int): number of slippers pairs.
            design (int): slippers design, from 0 to 1.
            size (int): type of tip protection, from 36 to 45 (default 43).

        """

        self.amount = amount
        self.design = design
        self.size = size

    def __str__(self):
        """Print decoded slipper info."""
        return f"""{self.amount} pair of {Slippers.designs[self.design]} \
slippers {Slippers.sizes[self.size]} size."""

    def __add__(self, n_items):
        summa = self.amount + n_items
        return Slippers(summa, self.design, self.size)


class Massager():
    """Massager class.

    Args:
        power_type (list): type of power supply,
                        ["no power", "battery", "power cord"]
        use_type (list): used by hands or automatic,
                        ["manual", "semi-automatic", "automatic"]

    """

    power_type = ["no power", "battery", "power cord"]
    use_type = ["manual", "semi-automatic", "automatic"]

    def __init__(self, amount, m_place, power=0, use=0):
        """Massager constructor.

        Args:
            amount (int): number of massagers.
            m_place (str): part of the body massager designed for.
            power (int): type of electrical supply, from 0 to 2.
            use (int): type of use, from 0 to 2.

        """
        self.amount = amount
        self.m_place = m_place
        self.power = power
        self.use = use

    def __str__(self):
        """Print decoded massager info."""
        return f"""{self.amount} massager for {self.m_place} with \
{Massager.power_type[self.power]} and for {Massager.use_type[self.use]} use."""

    def __add__(self, n_items):
        summa = self.amount + n_items
        return Massager(summa, self.m_place, self.power, self.use)


if __name__ == "__main__":
    pen = Pen(1, 100)
    slippers = Slippers(1)
    massager = Massager(1, "neck")
    print(pen)
    print(massager)
    print(slippers)
    print("\n")
    print(pen + 10)
    print(slippers + 20)
    print(massager + 30)
