'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''


class Movie():
    """Movie class for fun!

    Args:
        year (int): movie year of creation.
        title (str): movie name.
        country (str): country where the film was made.
        rating (float): movie rating based on reviews, e.g. 4.5.

    """

    def __init__(self, year, title, country, rating):
        self.year = year
        self.title = title
        self.country = country
        self.rating = rating

    def __repr__(self):
        return f"{self.title} - movie from {self.country}, first shown in \
{self.year} and with {self.rating} rating."


class RomCom(Movie):
    """Movie child class. Specifying genre and actors.

    Args:
        year (int): movie year of creation.
        title (str): movie name.
        country (str): country where the film was made.
        rating (float): movie rating based on reviews, e.g. 4.5.
        actors (str): main actors from the film.

    """

    genre = "romantic comedy"

    def __init__(self, year, title, country, rating, actors):
        super().__init__(year, title, country, rating)
        self.actors = actors

    def __repr__(self):
        return f"{self.title} - {RomCom.genre} movie from {self.country}, \
first shown in {self.year}, with {self.actors} and with \
{self.rating} rating."


class ActionMovie(Movie):
    """Movie child class. Specifying genre, budget and PG.

    Args:
        year (int): movie year of creation.
        title (str): movie name.
        country (str): country where the film was made.
        rating (float): movie rating based on reviews, e.g. 4.5.
        budget (int): film budget in dollars.
        pg (int): Motion Picture Association of America movie rating.

    """

    genre = "action"

    def __init__(self, year, title, country, rating, budget, pg=13):
        super().__init__(year, title, country, rating)
        self.budget = budget
        self.pg = pg

    def __repr__(self):
        return f"{self.title} - {ActionMovie.genre} movie \
from {self.country}, first shown in {self.year} and with {self.budget} \
$ budget with rating PG{self.pg} and viewers rating {self.rating}."


if __name__ == "__main__":
    movie = Movie(2020, "Pandemic madness", "Greenland", 4.9)
    c_movie = RomCom(2021, "Pandemic madness II", "Israel", 4.8,
                     "Jenifer Lawrence, Bruce Willis")
    a_movie = ActionMovie(c_movie.year, "Pandemic madness III: Payback",
                          "Russia", 2.1, 5000, 11)
    print(movie)
    print(c_movie)
    print(a_movie)
