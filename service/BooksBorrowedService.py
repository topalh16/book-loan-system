from repository.BooksBorrowedRepository import save, get_by_user_id, update_brought_date_by_ids
import datetime


def save_borrow(borrow):
    return save(borrow)


def lend_book_to_user(isbn, user_id):
    borrow = {'isbn': isbn, 'user_id': user_id, 'taken_date': datetime.date.today()}

    return save_borrow(borrow)


def get_remaining_days(past_date):
    today = datetime.date.today()
    day_diff = today - past_date
    return 30 - day_diff.days


def get_borrows_by_user_id(user_id):
    borrows = get_by_user_id(user_id)
    for borrow in borrows:
        borrow.remaining_days = get_remaining_days(borrow.taken_date)
    return borrows


def get_not_returned_borrows_by_user_id(user_id):
    return get_by_user_id(user_id, False)


def return_books(ids):
    update_brought_date_by_ids(ids, datetime.date.today())
