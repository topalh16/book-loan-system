from .connection import get_db
from model.CommentRating import CommentRating

db = get_db()


def save(comment_rating):
    mkcr = db.prepare(
        "INSERT INTO public.comment_rating (user_id, isbn, comment, rating) VALUES ($1, $2, $3, $4)")
    return mkcr(int(comment_rating['user_id']), comment_rating['isbn'], comment_rating['comment'],
                int(comment_rating['rating']))
