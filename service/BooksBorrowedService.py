from repository.BooksBorrowedRepository import save, get_by_user_id, update_brought_date_by_ids
import datetime


def save_borrow(borrow):
    return save(borrow)[1]


def lend_book_to_user(isbn, user_id):
    borrow = {'isbn': isbn, 'user_id': user_id, 'taken_date': datetime.date.today()}

    return save_borrow(borrow)


def get_borrows_by_user_id(user_id):
    return get_by_user_id(user_id)


def return_books(ids):
    update_brought_date_by_ids(ids, datetime.date.today())
