import csv
import pandas as pd
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.filename = file_path

    def list_movies(self):
        data = {}
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row['Movie']
                rating = row['Rating']
                year = row['Year of release']
                poster_url = row['Poster']
                data[title] = {'Rating': rating, 'Year of release': year, 'Poster': poster_url}
        return data

    def add_movie(self, title, rating, year, poster_url):
        fieldnames = ['Movie', 'Rating', 'Year of Release', 'Poster']
        movie_data = {'Movie': title, 'Rating': rating, 'Year of Release': year, 'Poster': poster_url}

        # Load existing data
        with open(self.filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(movie_data)

    def delete_movie(self, title):
        df = pd.read_csv(self.filename)
        df = df[df['Movie'] != title]
        df.to_csv(self.filename, index=False)

    def update_movie(self, title, rating):
        df = pd.read_csv(self.filename)
        df.loc[df['Movie'] == title, 'Rating'] = rating
        df.to_csv(self.filename, index=False)
