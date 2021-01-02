from repository.UserRepository import get_user_by_email, get_all, save, update, get_by_id, delete, get_all_by_name


def attempt_login(email, password):
    user = get_user_by_email(email)
    if user.password == password:
        return user
    else:
        return False


def save_user(user):
    return save(user)[1]


def get_all_users():
    return get_all()


def get_user_by_id(user_id):
    return get_by_id(user_id)


def update_user(user_id, user):
    return update(user_id, user)


def delete_user(user_id):
    return delete(user_id)[1]


def get_users_by_name(full_name):
    return get_all_by_name(full_name)
