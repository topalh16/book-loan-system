from .connection import get_db
from model.User import User

db = get_db()


def save(user):
    mkuser = db.prepare(
        "INSERT INTO public.users (email, full_name, department, password, role) VALUES ($1, $2, $3, $4, $5)")
    return mkuser(user['email'], user['full_name'], user['department'], user['password'], int(user['role']))


def get_all():
    get_all = db.prepare("SELECT * FROM public.users")

    with db.xact():
        users = []
        for user_row in get_all.rows():
            users.append(User(user_row))
        return users


def get_user_by_email(email):
    get_by_email = db.prepare("SELECT * FROM public.users WHERE email = $1")

    with db.xact():
        user_row = next(x for x in get_by_email.rows(email))
        return User(user_row)


def get_by_id(user_id):
    get_user_by_id = db.prepare("SELECT * FROM public.users WHERE user_id = $1")

    with db.xact():
        user_row = next(x for x in get_user_by_id.rows(int(user_id)))
        return User(user_row)


def update(user_id, user):
    update_user = db.prepare(
        "UPDATE public.users SET email = $2, full_name = $3, department = $4, password = $5, role = $6 WHERE user_id = $1")
    return update_user(int(user_id), user['email'], user['full_name'], user['department'], user['password'], int(user['role']))

def delete(user_id):
    delete_user = db.prepare("DELETE FROM public.users WHERE user_id = $1")
    return delete_user(int(user_id))
