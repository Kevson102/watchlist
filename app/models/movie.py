class Movie:
    '''
    Movie class to define Movie objects
    '''
    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        '''
        id: The movie id
        Title: The name of the movie
        Overview: A short description of the movie
        poster: The poster image of the movie
        vote_average: Average rating of the movie
        vote_count: How many people have rated the movie.
        '''
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count