from movie_app import MovieApp
from storage_json import StorageJson


def main():
    storage = StorageJson('movies_data_base.json')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
