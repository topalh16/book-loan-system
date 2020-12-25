class Book:
    def __init__(self, book_row):
        self.isbn = book_row[0]
        self.author = book_row[6] + ' ' + book_row[7]
        self.page_count = book_row[2]
        self.count = book_row[3]
        self.title = book_row[4]
