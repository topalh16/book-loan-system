from repository.BookRepository import get_all, get


def get_all_books():
    return get_all()


def get_book_by_isbn(isbn):
    return get(isbn)
