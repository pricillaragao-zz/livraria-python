import json
from typing import List


class Book:
    def __init__(
        self, title: str, genre: str, subgenre: str, publisher: str, price: float
    ):
        self.title = title
        self.genre = genre
        self.subgenre = subgenre
        self.publisher = publisher
        self.price = price

    def __repr__(self):
        return json.dumps(self.__dict__)


class Library:
    def __init__(self):
        self.collection = {}

    def add(self, book: Book):
        if book.genre not in self.collection:
            self.collection[book.genre] = {}
        if book.subgenre not in self.collection[book.genre]:
            self.collection[book.genre][book.subgenre] = []
        self.collection[book.genre][book.subgenre].append(book)

    def get_books(self, title: str, genre: str, subgenre: str) -> List[Book]:
        result = []
        for book in self.collection[genre][subgenre]:
            if book.title == title:
                result.append(book)
        return result

    def display(self):
        genres = self.collection.keys()
        for genre in sorted(genres):
            print(f"--- Gênero {genre} ---")
            subgenres = self.collection[genre].keys()
            for subgenre in sorted(subgenres):
                print(f"------ Subgênero {subgenre} ------")
                titles = sorted(
                    self._get_distinct_titles(genre, subgenre),
                    reverse=True,
                    key=lambda t: len(self.get_books(t, genre, subgenre)),
                )
                for title in titles:
                    units = len(self.get_books(title, genre, subgenre))
                    print(f"{title} - {units} {'unidades' if units > 1 else 'unidade'}")

    def _get_distinct_titles(self, genre: str, subgenre: str) -> List[str]:
        return list(set([book.title for book in self.collection[genre][subgenre]]))

    def __repr__(self):
        return str(self.collection)
