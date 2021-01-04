from .connection import get_db
from model.BooksBarrowed import BooksBorrowed

db = get_db()


def save(borrow):
    mkborrow = db.prepare(
        "INSERT INTO public.books_borrowed (user_id, isbn, taken_date) VALUES ($1, $2, $3)")
    return mkborrow(int(borrow['user_id']), borrow['isbn'], borrow['taken_date'])


def get_by_user_id(user_id):
    find_by_user_id = db.prepare(
        "SELECT * FROM public.books_borrowed T JOIN books B ON T.isbn=B.isbn WHERE user_id = $1 and brought_date is null")

    with db.xact():
        borrows = []
        for borrow_row in find_by_user_id.rows(int(user_id)):
            borrow = BooksBorrowed(borrow_row)
            borrow.book_title = borrow_row[9]
            borrows.append(borrow)
        return borrows


def update_brought_date_by_ids(ids, brought_date):
    update_borrows = db.prepare("UPDATE public.books_borrowed SET brought_date=$2 WHERE borrow_id = $1 ")
    for id in ids:
        update_borrows(int(id), brought_date)