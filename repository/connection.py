import postgresql
import os

url = os.environ.get("DATABASE_URL")
connection_string = 'pq://' + url[11:]


def get_db():
    if url is None:
        return postgresql.open('pq://postgres:Gandalf01@127.0.0.1:5432/book_loan')
    else:
        return postgresql.open(url)
