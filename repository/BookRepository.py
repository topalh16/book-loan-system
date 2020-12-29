from .connection import get_db
from model.Book import Book

db = get_db()


def get_all():
    get_all = db.prepare("SELECT * FROM public.books B JOIN authors A ON B.author_id=A.author_id")

    with db.xact():
        books = []
        for book_row in get_all.rows():
            books.append(Book(book_row))
        return books


def get(isbn):
    get_by_isbn = db.prepare("SELECT * FROM public.books B JOIN authors A ON B.author_id=A.author_id WHERE isbn=$1")

    with db.xact():
        book_row = next(book for book in get_by_isbn.rows(isbn))
        return Book(book_row)


def save(book):
    mkbook = db.prepare("INSERT INTO public.books (isbn, title, author_id, page_count, count, image_url) VALUES ($1, $2, $3, $4, $5, $6)")
    return mkbook(book['isbn'], book['title'], int(book['author_id']), int(book['page_count']), int(book['count']), book['image_url'])

def update(isbn, book):
    update_book = db.prepare("UPDATE public.books SET count=$2, image_url=$3 WHERE isbn = $1")
    return update_book(isbn, int(book['count']), book['image_url'])