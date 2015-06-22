import webbrowser
import person


class Video():
    """A basic Video class

    Attributes:
        title: A string defining the title of the video.
        duration: a string containing the runtime of the video.
    """
    def __init__(self, title, duration):
        """Inits the Video class with title and duration"""
        self.title = title
        self.duration = duration


class Movie(Video):
    """A basic Movie class, which extends the Video class

    Attributes:
        storyline: a string detailing the story line of the movie.
        poster_image_url: a string containing the URL of the movie poster.
        trailer_youtube_url: a string containing the URL of the youtube
                             trailer for the movie.
        director: director object detailed in the Person package.
    """
    def __init__(self, movie_title, movie_duration, movie_storyline,
                 poster_image, trailer_youtube, director):
        """Initialises the Movie class with data provided"""
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = person.Director(director.first_name,
                                        director.last_name, director.gender,
                                        director.imdb_url)

    def show_trailer(self):
        """Opens a web browser with the Movie's YouTube Trailer URL"""
        webbrowser.open(self.trailer_youtube_url)
