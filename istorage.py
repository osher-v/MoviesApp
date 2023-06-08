from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """Returns a dictionary of movies and their information."""
        pass

    @abstractmethod
    def add_movie(self, title, rating, year, poster_url):
        """Adds a movie to the database."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Deletes a movie from the database."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """Updates the rating of a movie in the database."""
        pass
