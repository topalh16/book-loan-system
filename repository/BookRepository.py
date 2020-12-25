from .connection import get_db
from model.Book import Book


def get_all():
    db = get_db()
    get_all = db.prepare("SELECT * FROM public.books B JOIN authors A ON B.author_id=A.author_id")

    with db.xact():
        books = []
        for book_row in get_all.rows():
            books.append(Book(book_row))
        return books
