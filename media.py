import webbrowser


class Movie():
    """ This class provides a way to store movie related information. """

    # Constructor that creates the instance variables
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Method that loads a YouTube trailer of the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
