from .connection import insert, query, update as update_db, delete as delete_db
from model.User import User


def save(user):
    sql_raw = "INSERT INTO public.users (email, full_name, department, password, role) VALUES ({0}, {1}, {2}, {3}, {4})"
    sql = sql_raw.format(user['email'], user['full_name'], user['department'], user['password'], int(user['role']))
    return insert(sql)


def get_all():
    sql = "SELECT * FROM public.users"
    result = query(sql)

    users = []
    for user_row in result:
        users.append(User(user_row))
    return users


def get_user_by_email(email):
    sql_raw = "SELECT * FROM public.users WHERE email = '{0}'"
    sql = sql_raw.format(email)
    print(query(sql))
    user_row = query(sql)[0]
    return User(user_row)


def get_by_id(user_id):
    sql_raw = "SELECT * FROM public.users WHERE user_id = {0}"
    sql = sql_raw.format(user_id)
    user_row = query(sql)[0]
    return User(user_row)


def get_all_by_name(full_name):
    sql_raw = "SELECT * FROM public.users WHERE  LOWER( full_name ) like '{0}'"
    sql = sql_raw.format('%' + full_name.lower() + '%')
    result = query(sql)
    users = []
    for user_row in result:
        users.append(User(user_row))
    return users


def update(user_id, user):
    sql_raw = "UPDATE public.users SET email = '{1}', full_name = '{2}', department = '{3}', password = '{4}', role = {5} WHERE user_id = {0}"
    sql = sql_raw.format(user_id, user['email'], user['full_name'], user['department'], user['password'], user['role'])
    return update_db(sql)


def delete(user_id):
    sql_raw = "DELETE FROM public.users WHERE user_id = {0}"
    sql = sql_raw.format(user_id)
    return delete_db(sql)
