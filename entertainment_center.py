import movie
import urllib
import fresh_tomatoes

toyStory = media.Movie("Toy Story",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc", "PG")
avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY","PG-13")
clerks2 = media.Movie("Clerks 2",
                      "https://upload.wikimedia.org/wikipedia/en/0/03/Clerks_II_Theatrical_Poster.jpg",
                      "https://www.youtube.com/watch?v=gLvhJ0m5ask","PG-13")
schoolOfRock = media.Movie("School of Rock",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=3PsUJFEBC74","PG-13")
hungerGames = media.Movie("Hunger Games",
                          "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=RCDHJ6P_y0I","PG-13")
infinityWar = media.Movie("Avengers: Infinity War",
                          "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                          "https://www.youtube.com/watch?v=6ZfuNTqbHE8","PG-13")


movies = [toyStory, avatar, clerks2, schoolOfRock, hungerGames, infinityWar]
fresh_tomatoes.open_movies_page(movies)
