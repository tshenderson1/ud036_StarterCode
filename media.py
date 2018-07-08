import webbrowser

#################################################
#  Created by T Henderson using instructions
#  from udacity full stack web course
#  for Movie Trailer Project
#  submitted 5/20/2018
#
#################################################


class Movie():
    """
    Creates a Movie object to be used to display poster image and movie trailer

    Attributes:
        movie_title (str) : string title of movie for display
        poster_image_url (str) : string url address for movie poster
        trailer_youtube (str) : string url address for movie trailer
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showTrailer(self):
        """Public method to display trailer_youtube_url in a webbrowser"""

        webbrowser.open(self.trailer_youtube_url)


    def showPoster(self):
        """Public method to display poster_image_url in a webbrowser"""
        webbrowser.open(self.poster_image_url)
