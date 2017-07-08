import media
import fresh_tomatoes
import httplib # Used in Python 2


conn = httplib.HTTPSConnection("api.themoviedb.org")
payload = "{}"
# Movie IDs from themoviedb.org
movie_id = ["246655", "2080", "49538", "127585", "246655", "263115"]
release_date = []

# for loop to find Release date for each movie_id
for moviedb in movie_id: 
    conn.request("GET", "/3/movie/" + moviedb + "/release_dates?api_key=c744541ef0c2fd5ff5ccba678f100347", payload) # noqa
    res = conn.getresponse()
    data = res.read()
    j = data.decode("utf-8").find("US") # find position of US release date info
    US = data.decode("utf-8")[j:]
    i = US.find("T00")
    release_date.append(US[i-10:i])

# Creates instances of the Movie class for each movie
xmen = media.Movie("X-Men",
                   "https://upload.wikimedia.org/wikipedia/en/8/81/X-MenfilmPoster.jpg", # noqa
                   "https://www.youtube.com/watch?v=nbNcULQFojc",
                    release_date[0])
xmen_origins_wolverine = media.Movie("X-Men Origins: Wolverine",
                                     "https://upload.wikimedia.org/wikipedia/en/e/ec/X-Men_Origins_Wolverine.jpg", # noqa
                                     "https://www.youtube.com/watch?v=toLpchTUYk8", # noqa
                                     release_date[1])
xmen_first_class = media.Movie("X-Men: First Class",
                               "https://upload.wikimedia.org/wikipedia/en/5/55/X-MenFirstClassMoviePoster.jpg", #noqa
                               "https://www.youtube.com/watch?v=UrbHykKUfTM", 
                               release_date[2])
xmen_days_of_future_past = media.Movie("X-Men: Days of Future Past",
                                       "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg", # noqa
                                       "https://www.youtube.com/watch?v=pK2zYHWDZKo", # noqa
                                       release_date[3])
xmen_apocalypse = media.Movie("X-Men: Apocalypse",
                              "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg", # noqa
                              "https://www.youtube.com/watch?v=Jer8XjMrUB4&spfreload=10", # noqa
                               release_date[4])
logan = media.Movie("Logan",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg", # noqa
                    "https://www.youtube.com/watch?v=Div0iP65aZo",
                     release_date[5])
# Creates a movies array to be accessed from fresh_tomatoes.py
movies = [xmen, xmen_origins_wolverine, xmen_first_class,
          xmen_days_of_future_past, xmen_apocalypse, logan]
# Creates a HTML page by passing in movies
fresh_tomatoes.open_movies_page(movies)
