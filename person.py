class Person():
    """A simple definition of a Person

    Attributes:
        first_name: A string containing the directors first name
        last_name: A string containing the directors last name
        gender: A string that denotes the persons gender
    """
    def __init__(self, first_name, last_name, gender):
        """Initialises the Person class"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender


class Director(Person):
    """A simple definition of a Director

    Attributes:
        imdb_url: A string that contains a URL to the directors IMDb page.
    """
    def __init__(self, first_name, last_name, gender, imdb_url):
        """Initialises the Director class, a subclass of Person"""
        Person.__init__(self, first_name, last_name, gender)
        self.imdb_url = imdb_url
