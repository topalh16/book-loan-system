from .connection import get_db
from model.BooksBarrowed import BooksBorrowed

db = get_db()


def save(borrow):
    mkborrow = db.prepare(
        "INSERT INTO public.books_borrowed (user_id, isbn, taken_date) VALUES ($1, $2, $3)")
    return mkborrow(int(borrow['user_id']), borrow['isbn'], borrow['taken_date'])
