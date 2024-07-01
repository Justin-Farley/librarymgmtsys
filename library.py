class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.borrowed = False  # Initially, book is not borrowed


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
