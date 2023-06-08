import statistics
import random
import matplotlib.pyplot as plt
import movie_storage
import data_fetcher


# Function to display all movies and their ratings in the database
def display_movies():
    """Function to display all movies and their ratings in the database """
    movies = movie_storage.list_movies()
    print(f"We have {len(movies)} movies in total:")
    for movie_name, movie_info in movies.items():
        print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")


# Function to add a new movie and rating to the database
def add_movie():
    """Function to add a new movie and rating to the database """

    data = data_fetcher.load_data(input("Please enter the movie name:\n"))
    if data is not None:
        title = data["Title"]
        year = data["Year"]
        rating = data["imdbRating"]
        poster_url = data["Poster"]
        movie_storage.add_movie(title, rating, year, poster_url)


# Function to delete a movie from the database
def delete_movie():
    """Function to delete a movie from the database """
    movie_storage.delete_movie(input("pls enter the movie name:\n"))


# Function to update the rating of a movie in the database
def update_movie():
    """Function to update the rating of a movie in the database """
    movies = movie_storage.list_movies()
    movie_name = input("pls enter the movie name:\n")
    if movie_name in movies:
        rating = float(input("Please enter the updated movie rating:\n"))
        movie_storage.update_movie(movie_name, rating)
    else:
        print("the name you entered is an correct or not in the database")


# Function to get statistics on the movie ratings in the database
def get_statistics():
    """Function to get statistics on the movie ratings in the database """
    movies = movie_storage.list_movies()
    # Average rating in the database using statistics method.
    ratings = [float(movie_info['Rating']) for movie_info in movies.values()]
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


# Function to choose a random movie from the database
def choose_random_movie():
    movies = movie_storage.list_movies()
    random_key = random.choice(list(movies.keys()))
    random_movie = movies[random_key]
    print(f"Your random movie is: {random_key} ({random_movie['Year of release']}) with a rating of"
          f" {random_movie['Rating']}")


# Function to search for a movie in the database
def search_movie():
    """Function to search for a movie in the database"""
    movies = movie_storage.list_movies()
    choice = input("enter your search:")
    for movie_name, movie_info in movies.items():
        if choice in movie_name:
            print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")


# Function to sort the movies in the database by rating
def sort_movies_by_rating():
    """Function to sort the movies in the database by rating"""
    movies = movie_storage.list_movies()
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]['Rating'], reverse=True)
    for movie_name, movie_info in sorted_movies:
        print(f"{movie_name} ({movie_info['Year of release']}): {movie_info['Rating']}")


def create_rating_histogram():
    """create_rating_histogram """
    movies = movie_storage.list_movies()
    ratings = [movie['Rating'] for movie in movies.values()]
    plt.hist(ratings, bins=10, range=(0, 10), edgecolor='black')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title('Rating Histogram')
    file_path = input("Enter file path to save the histogram: ")
    plt.savefig(file_path)
    plt.show()


def generate_website():
    data = movie_storage.list_movies()
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
    with open("../../../OneDrive/שולחן העבודה/project-part-2 (2)/index.html", 'w') as f:
        f.write(html)
    print("Website was generated successfully.\n")


# Main function to run the program and handle user input
def main():
    # Display the main menu and get user input
    print("********** My Movies Database  **********\n")
    while True:
        chosen = input("""
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


    Enter choice (1-10):  """)

        match chosen:
            case "1":
                display_movies()
            case "2":
                add_movie()
            case "3":
                delete_movie()
            case "4":
                update_movie()
            case "5":
                get_statistics()
            case "6":
                choose_random_movie()
            case "7":
                search_movie()
            case "8":
                sort_movies_by_rating()
            case "9":
                create_rating_histogram()
            case "10":
                generate_website()
            case "0":
                print("Goodbye!")
                return
            case _:
                print("Invalid choice, please choose a number between 1-10")


if __name__ == "__main__":
    main()
