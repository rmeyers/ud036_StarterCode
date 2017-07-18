
class Movie():
    ''' This creates a new movie instance, including variables for
    movie title, poster_image, and YouTube link. '''
    def __init__(
        self, movie_title, movie_storyline, poster_image,
        trailer_youtube
    ):
        # Here we create the self variables from the function inputs.
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
