from repository.UserRepository import get_user_by_email


def attempt_login(email, password):
    user = get_user_by_email(email)
    if user.password == password:
        return user
    else:
        return False
