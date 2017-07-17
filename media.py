
class Movie():
    ''' This creates a new movie instance. '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        import webbrowser
        webbrowser.open(self.trailer_youtube_url)
