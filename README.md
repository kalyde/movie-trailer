# Movie Trailer
movie-trailer creates a website to display a movie's poster and trailer.

## Usage
To create movies, `media.Movie` takes in 4 arguments: title, poster URL, YouTube trailer URL and Release Date (from API).

To use data from API, go to https://www.themoviedb.org/, search for a movie and find the Movie ID in the URL and enter it in the `movie_id` array.

`your_movie1 = media.Movie("Title", "Poster URL", "YouTube URL", release_date[i])`

Then add each instance into the `movies` array.

`movies = [your_movie1, your_movie2]`

## License

The content of this repository is licensed under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/) **except** for the file, fresh_tomatoes.py, which can be found in this [repository](https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py).