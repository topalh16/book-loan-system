from repository.UserRepository import get_user_by_email, get_all, save


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
