import json


def list_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    with open('movies_data_base.json', 'r') as f:
        data = json.load(f)
    return data


def add_movie(title, rating, year, poster_url):
    """
    Adds a movie to the movies' database.
    Loads the information from the JSON file, adds the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # Load existing data
    with open('../../../OneDrive/שולחן העבודה/project-part-2 (2)/movies_data_base.json', 'r') as f:
        data = json.load(f)

    # Add new movie
    data[title] = {'Rating': rating, 'Year of release': year, 'Poster': poster_url}

    # Save updated data
    with open('../../../OneDrive/שולחן העבודה/project-part-2 (2)/movies_data_base.json', 'w') as f:
        json.dump(data, f)


def delete_movie(title):
    """
    Deletes a movie from the movies' database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # Load existing data
    with open('../../../OneDrive/שולחן העבודה/project-part-2 (2)/movies_data_base.json', 'r') as f:
        data = json.load(f)

    # Delete movie
    if title in data:
        del data[title]

    # Save updated data
    with open('../../../OneDrive/שולחן העבודה/project-part-2 (2)/movies_data_base.json', 'w') as f:
        json.dump(data, f)


def update_movie(title, rating):
    """
    Updates a movie from the movies' database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # Load existing data
    with open('../../../OneDrive/שולחן העבודה/project-part-2 (2)/movies_data_base.json', 'r') as f:
        data = json.load(f)

    # Update movie rating
    if title in data:
        data[title]['Rating'] = rating
    else:
        return 0
    # Save updated data
    with open('../../../OneDrive/שולחן העבודה/project-part-2 (2)/movies_data_base.json', 'w') as f:
        json.dump(data, f)
