import statistics
import random
import matplotlib.pyplot as plt
from MoviesApp import data_fetcher


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """Function to display all movies and their ratings in the database """
        movies = self._storage.list_movies()
        print(f"We have {len(movies)} movies in total:")
        for movie_name, movie_info in movies.items():
            print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")

    def _command_add_movie(self):
        """Function to add a new movie and rating to the database """
        data = data_fetcher.load_data(input("Please enter the movie name:\n"))
        if data is not None:
            title = data["Title"]
            year = data["Year"]
            if data["imdbRating"] != 'N/A':
                rating = data["imdbRating"]
            else:
                rating = '0'
            if data["Poster"] != 'N/A':
                poster_url = data["Poster"]
            else:
                poster_url = "image-not-found-icon.png"
            self._storage.add_movie(title, rating, year, poster_url)

    def _command_delete_movie(self):
        """Function to delete a movie from the database """
        self._storage.delete_movie(input("pls enter the movie name:\n"))

    def _command_update_movie(self):
        """Function to update the rating of a movie in the database """
        movies = self._storage.list_movies()
        movie_name = input("pls enter the movie name:\n")
        if movie_name in movies:
            rating = float(input("Please enter the updated movie rating:\n"))
            self._storage.update_movie(movie_name, rating)
        else:
            print("the name you entered is an correct or not in the database")

    def _command_stats(self):
        """Function to get statistics on the movie ratings in the database """
        movies = self._storage.list_movies()
        # Average rating in the database using statistics method.
        ratings = []
        for movie_info in movies.values():
            try:
                rating = float(movie_info['Rating'])
            except ValueError:
                rating = 0
            ratings.append(rating)

        print("The average rating is: {:.1f}".format(statistics.mean(ratings)))
        print("The median rating is:", statistics.median(ratings))
        # Find and print the most highly rated movies
        max_rating = max(ratings)
        print("The most rated movies are:")
        for movie_name, movie_info in movies.items():
            if float(movie_info['Rating']) == max_rating:
                print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")

        # Find and print the least highly rated movies
        min_rating = min(ratings)
        print("The last rated movies are:")
        for movie_name, movie_info in movies.items():
            if float(movie_info['Rating']) == min_rating:
                print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")

    def _command_random_movie(self):
        movies = self._storage.list_movies()
        random_key = random.choice(list(movies.keys()))
        random_movie = movies[random_key]
        print(f"Your random movie is: {random_key} ({random_movie['Year of release']}) with a rating of"
              f" {random_movie['Rating']}")

    def _command_search_movie(self):
        """Function to search for a movie in the database"""
        movies = self._storage.list_movies()
        choice = input("enter your search:")
        for movie_name, movie_info in movies.items():
            if choice in movie_name:
                print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")

    def _command_sorted_by_rating(self):
        """Function to sort the movies in the database by rating"""
        movies = self._storage.list_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['Rating'], reverse=True)
        for movie_name, movie_info in sorted_movies:
            print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")

    def _command_create_rating_histogram(self):
        """create_rating_histogram """
        movies = self._storage.list_movies()
        ratings = [movie['Rating'] for movie in movies.values()]
        plt.hist(ratings, bins=10, range=(0, 10), edgecolor='black')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.title('Rating Histogram')
        file_path = input("Enter file path to save the histogram: ")
        plt.savefig(file_path)
        plt.show()

    def _command_generate_website(self):
        data = self._storage.list_movies()
        # Generate the HTML code
        html = f'''<html>
           <head>
               <title>My Movie App</title>
               <link rel="stylesheet" href="style.css"/>
           </head>
           <body>
           <div class="list-movies-title">
               <h1>Osher's Movie App</h1>
           </div>
           <div>
               <ol class="movie-grid">
           '''

        for title, movie in data.items():
            html += f'''
                   <li>
                       <div class="movie">
                           <div class="card-container">
                               <div class="card">
                                   <div class="card-front">
                                       <img class="movie-poster" src="{movie['Poster']}" title=""/>
                                       <div class="movie-title">{title}</div>
                                       <div class="movie-description">{movie['Year of release']}</div>
                                   </div>
                                   <div class="card-back">
                                        <div class="movie-rating">rating {movie['Rating']}</div>
                                   </div>
                               </div>
                           </div>
                       </div>
                   </li>
               '''

        html += '''
               </ol>
           </div>
           </body>
           </html>
           '''
        # Write the HTML code to file
        with open("index.html", 'w') as f:
            f.write(html)
        print("Website was generated successfully.\n")

    def run(self):
        print("********** My Movies Database **********\n")
        while True:
            choice = input("""
Menu:
0. EXIT
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create rating histogram
10. Generate website


Enter choice (1-10): """)

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_stats()
            elif choice == "6":
                self._command_random_movie()
            elif choice == "7":
                self._command_search_movie()
            elif choice == "8":
                self._command_sorted_by_rating()
            elif choice == "9":
                self._command_create_rating_histogram()
            elif choice == "10":
                self._command_generate_website()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

