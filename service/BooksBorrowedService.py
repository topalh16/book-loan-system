from repository.BooksBorrowedRepository import save
import datetime

def save_borrow(borrow):
    return save(borrow)[1]


def lend_book_to_user(isbn, user_id):
    borrow = {}
    borrow['isbn'] = isbn
    borrow['user_id'] = user_id
    borrow['taken_date'] = datetime.date.today()

    return save_borrow(borrow)