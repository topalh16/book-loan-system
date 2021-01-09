from .connection import query, insert, update
from model.BooksBarrowed import BooksBorrowed


def save(borrow):
    sql_raw = "INSERT INTO public.books_borrowed (user_id, isbn, taken_date) VALUES ({0}, '{1}', '{2}')"
    sql = sql_raw.format(borrow['user_id'], borrow['isbn'], borrow['taken_date'])
    return insert(sql)


def get_by_user_id(user_id, is_null=True):
    suffix = "null" if is_null else "not null"
    sql_raw = "SELECT * FROM public.books_borrowed T JOIN books B ON T.isbn=B.isbn WHERE user_id = {0} and brought_date is {1}"
    sql = sql_raw.format(user_id, suffix)
    result = query(sql)

    borrows = []
    for borrow_row in result:
        borrow = BooksBorrowed(borrow_row)
        borrow.book_title = borrow_row[9]
        borrows.append(borrow)
    return borrows


def update_brought_date_by_ids(ids, brought_date):
    ids_string = ','.join(ids)
    sql_raw = "UPDATE public.books_borrowed SET brought_date='{1}' WHERE borrow_id IN ({0})"
    sql = sql_raw.format(ids_string, brought_date)
    update(sql)
