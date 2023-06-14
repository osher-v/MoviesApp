import sys
from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <storage_format>")
        return

    storage_format = sys.argv[1]
    if storage_format == 'json':
        storage = StorageJson('movies_data_base.json')
    elif storage_format == 'csv':
        storage = StorageCsv('movies_data_base.csv')
    else:
        print("Invalid storage format. Supported formats: json, csv")
        return

    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()