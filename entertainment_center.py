import media
import urllib
import fresh_tomatoes

####################################################
#
#  Created by T Henderson using instructions
#  from udacity full stack web course
#  for Movie Trailer Project
#  submitted 5/20/2018
#
####################################################

#create several instances of class media.Movie
toyStory = media.Movie("Toy Story",
        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
        "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
clerks2 = media.Movie("Clerks 2",
        "https://upload.wikimedia.org/wikipedia/en/0/03/Clerks_II_Theatrical_Poster.jpg",
        "https://www.youtube.com/watch?v=gLvhJ0m5ask")
schoolOfRock = media.Movie("School of Rock",
        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
        "https://www.youtube.com/watch?v=3PsUJFEBC74")
hungerGames = media.Movie("Hunger Games",
        "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
        "https://www.youtube.com/watch?v=RCDHJ6P_y0I")
infinityWar = media.Movie("Avengers: Infinity War",
        "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")


#populate array with movie objects then call fresh_tomatoes to open web page
movies = [toyStory, avatar, clerks2, schoolOfRock, hungerGames, infinityWar]
fresh_tomatoes.open_movies_page(movies)
