import media
import fresh_tomatoes


# Creates instances of the Movie class for each movie
xmen = media.Movie("X-Men",
                   "https://upload.wikimedia.org/wikipedia/en/8/81/X-MenfilmPoster.jpg", # noqa
                   "https://www.youtube.com/watch?v=nbNcULQFojc")
xmen_origins_wolverine = media.Movie("X-Men Origins: Wolverine",
                                     "https://upload.wikimedia.org/wikipedia/en/e/ec/X-Men_Origins_Wolverine.jpg", # noqa
                                     "https://www.youtube.com/watch?v=toLpchTUYk8")
xmen_first_class = media.Movie("X-Men: First Class",
                               "https://upload.wikimedia.org/wikipedia/en/5/55/X-MenFirstClassMoviePoster.jpg", #noqa
                               "https://www.youtube.com/watch?v=UrbHykKUfTM")
xmen_days_of_future_past = media.Movie("X-Men: Days of Future Past",
                                       "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg", # noqa
                                       "https://www.youtube.com/watch?v=pK2zYHWDZKo") # noqa
xmen_apocalypse = media.Movie("X-Men: Apocalypse",
                              "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg", # noqa
                              "https://www.youtube.com/watch?v=Jer8XjMrUB4&spfreload=10") # noqa
logan = media.Movie("Logan",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg", # noqa
                    "https://www.youtube.com/watch?v=Div0iP65aZo")
# Creates a movies array to be accessed from fresh_tomatoes.py
movies = [xmen, xmen_origins_wolverine, xmen_first_class,
          xmen_days_of_future_past, xmen_apocalypse, logan]
# Creates a HTML page by passing in movies
fresh_tomatoes.open_movies_page(movies)
