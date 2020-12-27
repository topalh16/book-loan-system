class Author:
    def __init__(self, author_row):
        self.author_id = author_row[0]
        self.name = author_row[1]
        self.surname = author_row[2]
