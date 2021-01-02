class BooksBorrowed:
    def __init__(self, books_borrowed_row):
        self.borrow_id = books_borrowed_row[0]
        self.user_id = books_borrowed_row[1]
        self.isbn = books_borrowed_row[2]
        self.taken_date = books_borrowed_row[3]
        self.brought_date = books_borrowed_row[4]
