from repository.BookRepository import get_all, get, save, update, delete


def get_all_books():
    return get_all()


def get_book_by_isbn(isbn):
    return get(isbn)


def save_book(book):
    return save(book)


def update_book(isbn, book):
    return update(isbn, book)[1]


def delete_book(isbn):
    return delete(isbn)[1]
