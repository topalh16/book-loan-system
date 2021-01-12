from .connection import insert, query, update as update_db
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


def get_by_id(author_id):
    sql_raw = "SELECT * FROM public.authors WHERE author_id = {0}"
    sql = sql_raw.format(author_id)
    result = query(sql)
    if len(result) == 0:
        return None
    author_row = result[0]
    return Author(author_row)


def update(author_id, author):
    sql_raw = "UPDATE public.authors SET name = '{1}', surname = '{2}' WHERE author_id = {0}"
    sql = sql_raw.format(author_id, author['name'], author['surname'])
    return update_db(sql)
