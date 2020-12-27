from .connection import get_db
from model.Author import Author

db = get_db()


def save(author):
    mkauthor = db.prepare("INSERT INTO public.authors (name, surname) VALUES ($1, $2)")
    return mkauthor(author['name'], author['surname'])


def get_all():
    get_all = db.prepare("SELECT * FROM public.authors")

    with db.xact():
        authors = []
        for author_row in get_all.rows():
            authors.append(Author(author_row))
        return authors
