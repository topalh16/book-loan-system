from repository.CommentRatingRepository import save


def save_comment_rating(form, user_id, isbn):
    comment_rating = {'isbn': isbn, 'user_id': user_id, 'comment': form['comment'], 'rating': form['rating']}
    return save(comment_rating)[1]
