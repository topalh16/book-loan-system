from .connection import insert
from model.CommentRating import CommentRating


def save(comment_rating):
    sql_raw = "INSERT INTO public.comment_rating (user_id, isbn, comment, rating) VALUES ({0}, '{1}', '{2}', {3})"
    sql = sql_raw.format(comment_rating['user_id'], comment_rating['isbn'], comment_rating['comment'], comment_rating['rating'])
    return insert(sql)
