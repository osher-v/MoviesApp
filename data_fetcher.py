import requests

API_KEY = "8167fd8a"


def load_data(movie_name):
    try:
        """ Loads movie data from an API for a given movie name"""
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "False":
            print("Movie not found.")
            return None
        else:
            return response.json()
    except requests.exceptions.ConnectionError:
        print("API is not accessible. Please check your internet connection.")


