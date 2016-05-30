import webbrowser


class Movie():
    """Class for all movie objects to store data

    Attributes:
        movie_title (str): Title of the movie
        movie_storyline (str): Short description of the movie (1 paragraph)
        poster_image (str): URL of the movie poster image
        trailer_youtube (str): URL to the movie trailer
    """

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
