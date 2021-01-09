from .connection import insert, query
from model.Author import Author


def save(author):
    sql_raw = "INSERT INTO public.authors (name, surname) VALUES ('{0}', '{1}')"
    sql = sql_raw.format(author['name'], author['surname'])
    return insert(sql)


def get_all():
    sql = "SELECT * FROM public.authors"
    result = query(sql)

    authors = []
    for author_row in result:
        authors.append(Author(author_row))
    return authors
