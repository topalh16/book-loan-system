from repository.AuthorRepository import get_all, save


def save_author(author):
    return save(author)[1]


def get_all_authors():
    return get_all()
