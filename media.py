import webbrowser

class Movie():
    """This class provides a means of storing movie object in a single object space"""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def showPoster(self):
        webbrowser.open(self.poster_image_url)
