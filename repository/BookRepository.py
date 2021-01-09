from .connection import query, insert, update as update_db, delete as delete_db
from model.Book import Book


def get_all():
    sql = "SELECT * FROM public.books B JOIN authors A ON B.author_id=A.author_id"
    result = query(sql)

    books = []
    for book_row in result:
        books.append(Book(book_row))
    return books


def get(isbn):
    sql_raw = "SELECT * FROM public.books B JOIN authors A ON B.author_id=A.author_id WHERE isbn='{0}'"
    sql = sql_raw.format(isbn)
    book_row = query(sql)
    return Book(book_row)


def save(book):
    sql_raw = "INSERT INTO public.books (isbn, title, author_id, page_count, count, image_url) VALUES ('{0}', '{1}', {2}, {3}, {4}, '{5}')"
    sql = sql_raw.format(book['isbn'], book['title'], book['author_id'], book['page_count'], book['count'], book['image_url'])
    return insert(sql)


def update(isbn, book):
    sql_raw = "UPDATE public.books SET count={1}, image_url='{2}' WHERE isbn = '{0}'"
    sql = sql_raw.format(isbn, book['count'], book['image_url'])
    return update_db(sql)


def delete(isbn):
    sql_raw = "DELETE FROM public.books WHERE isbn = '{0}'"
    sql = sql_raw.format(isbn)
    return delete_db(sql)
