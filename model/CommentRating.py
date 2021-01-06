class CommentRating:
    def __init__(self, comment_rating_row):
        self.comment_id = comment_rating_row[0]
        self.user_id = comment_rating_row[1]
        self.isbn = comment_rating_row[2]
        self.comment = comment_rating_row[3]
        self.rating = comment_rating_row[4]
