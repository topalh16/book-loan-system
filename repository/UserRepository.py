from .connection import get_db
from model.User import User

def save(user):
    db = get_db()
    mkuser = db.prepare("INSERT INTO public.users (email, full_name, department, password, role) VALUES ($1, $2, $3, $4, $5)")
    return mkuser(user['email'], user['full_name'], user['department'], user['password'], int(user['role']))


def get_all():
    db = get_db()
    get_all = db.prepare("SELECT * FROM public.users")

    with db.xact():
        users = []
        for user_row in get_all.rows():
            users.append(User(user_row))
        return users

def get_user_by_email(email):
    db = get_db()
    get_by_email = db.prepare("SELECT * FROM public.users WHERE email = $1")

    with db.xact():
        user_row = next(x for x in get_by_email.rows(email))
        return User(user_row)
