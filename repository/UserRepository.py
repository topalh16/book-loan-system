from .connection import get_db


def get_user_by_email(email):
    db = get_db()
    get_by_email = db.prepare("SELECT * FROM public.users WHERE email = $1")

    # Streaming, in a transaction.
    with db.xact():
        return next(x for x in get_by_email.rows(email))
