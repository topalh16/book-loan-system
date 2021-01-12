from repository.AuthorRepository import get_all, save, update, get_by_id


def save_author(author):
    return save(author)


def get_all_authors():
    return get_all()


def get_author_by_id(author_id):
    return get_by_id(author_id)


def update_author(author_id, author):
    return update(author_id, author)
