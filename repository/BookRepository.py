from .connection import get_db
from model.Book import Book

db = get_db()


def get_all():
    get_all = db.prepare("SELECT * FROM public.books B JOIN authors A ON B.author_id=A.author_id")

    with db.xact():
        books = []
        for book_row in get_all.rows():
            books.append(Book(book_row))
        return books


def get(isbn):
    get_by_isbn = db.prepare("SELECT * FROM public.books B JOIN authors A ON B.author_id=A.author_id WHERE isbn=$1")

    with db.xact():
        book_row = next(book for book in get_by_isbn.rows(isbn))
        return Book(book_row)
