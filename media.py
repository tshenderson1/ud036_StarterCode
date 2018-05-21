import webbrowser

class Movie():
    """This class provides a means of storing movie object in a single object space"""

#init requires a string title, string url for poster image, string url for trailer
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#simple method to display movie trailer
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
#simple method to display movie poster
    def showPoster(self):
        webbrowser.open(self.poster_image_url)
