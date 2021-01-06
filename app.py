from flask import Flask, render_template, request, session, redirect, flash
from service.UserService import attempt_login, get_all_users, save_user, get_user_by_id, update_user, delete_user, \
    get_users_by_name
from service.BookService import get_all_books, get_book_by_isbn, save_book, update_book, delete_book
from service.AuthorService import get_all_authors, save_author
from service.BooksBorrowedService import lend_book_to_user, get_borrows_by_user_id, return_books, \
    get_not_returned_borrows_by_user_id
from service.CommentRatingService import save_comment_rating
from model.Role import Role
from helper import serialize, deserialize

app = Flask(__name__)
app.secret_key = b'czf_36./jsfmc'


@app.route('/')
def home():
    if 'user' in session:
        user = deserialize(session['user'])
        return render_template('home.html', title="Home", user=user)
    return redirect("/login")


@app.route('/login')
def login():
    if 'user' in session:
        return redirect("/")
    return render_template('login.html')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    user = attempt_login(request.form['email'], request.form['password'])
    if not user:
        return redirect('/login')

    session['user'] = serialize(user)
    return redirect('/')


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/login')


# ---------- User Operations ---------- #

@app.route('/users', methods=['GET', 'POST'])
def users():
    affected_rows = 0
    if request.method == 'POST':
        affected_rows = save_user(request.form)
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect("/")
        users = get_all_users()
        return render_template('users.html', title="Users", user=user, users=users, saved_users=affected_rows)
    return redirect("/login")


# Editing existing user
@app.route('/user/edit/<user_id>', methods=['GET'])
def edit_user(user_id):
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect("/")
        selected_user = get_user_by_id(user_id)
        users = get_all_users()
        return render_template('user_edit.html', title=selected_user.full_name, user=user, users=users,
                               selected_user=selected_user)
    return redirect("/login")


# Updating existing user
@app.route('/user/update/<user_id>', methods=['POST'])
def user_update(user_id):
    if 'user' in session:
        user = deserialize(session['user'])
        update_user(user_id, request.form)
        return redirect("/users")
    return redirect("/login")


# Delete existing user
@app.route('/user/delete/<user_id>', methods=['GET'])
def user_delete(user_id):
    if 'user' in session:
        user = deserialize(session['user'])
        delete_user(user_id)
        return redirect("/users")
    return redirect("/login")


# ------------------------------ #


@app.route('/authors', methods=['GET', 'POST'])
def authors():
    affected_rows = 0
    if request.method == 'POST':
        affected_rows = save_author(request.form)
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect("/")
        authors = get_all_authors()
        return render_template('authors.html', title="Authors", user=user, authors=authors, saved_authors=affected_rows)
    return redirect("/login")


# ---------- Book Operations ---------- #

# Listing
@app.route('/books', methods=['GET', 'POST'])
def books():
    affected_rows = 0
    if request.method == 'POST':
        affected_rows = save_book(request.form)
    if 'user' in session:
        user = deserialize(session['user'])
        books = get_all_books()
        return render_template('books.html', title="Books", user=user, books=books)
    return redirect("/login")


# Viewing one book
@app.route('/book/<isbn>', methods=['GET'])
def view_book(isbn):
    if 'user' in session:
        user = deserialize(session['user'])
        book = get_book_by_isbn(isbn)
        searched_user = request.args.get('user')
        users = []
        if searched_user:
            users = get_users_by_name(searched_user)
        return render_template('book.html', title=book.title, user=user, book=book, searched_users=users)
    return redirect("/login")


# Creating new book
@app.route('/book/new', methods=['GET'])
def add_book():
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect("/")
        return render_template('book_edit.html', title="New Book", user=user)
    return redirect("/login")


# Editing existing book
@app.route('/book/edit/<isbn>', methods=['GET'])
def edit_book(isbn):
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect("/")
        book = get_book_by_isbn(isbn)
        return render_template('book_edit.html', title=book.title, user=user, book=book)
    return redirect("/login")


# Updating existing book
@app.route('/book/update/<isbn>', methods=['POST'])
def book_update(isbn):
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect(request.referrer)
        update_book(isbn, request.form)
        return redirect("/books")
    return redirect("/login")


# Lending book
@app.route('/book/lend/<isbn>/<user_id>', methods=['GET'])
def lend_book(isbn, user_id):
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect(request.referrer)
        affected_rows = lend_book_to_user(isbn, user_id)
        if affected_rows == 1:
            lended_user = get_user_by_id(user_id)
            flash('You successfully lended the book to ' + lended_user.full_name)
        return redirect("/book/" + isbn)
    return redirect("/login")


# Delete existing book
@app.route('/book/delete/<isbn>', methods=['GET'])
def book_delete(isbn):
    if 'user' in session:
        user = deserialize(session['user'])
        delete_book(isbn)
        return redirect("/books")
    return redirect("/login")


# ------------------------------ #


# ---------- Book Return Operations ---------- #

@app.route('/book-return', methods=['GET', 'POST'])
def book_return():
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.ADMIN.value:
            return redirect("/")

        if request.method == 'POST':
            return_books(request.form.getlist('borrow'))

        searched_user = request.args.get('user')
        users = []
        if searched_user:
            users = get_users_by_name(searched_user)

        searched_user_id = request.args.get('user_id')
        borrows = []
        if searched_user_id:
            borrows = get_borrows_by_user_id(searched_user_id)
        return render_template('book_return.html', title="Book Return", user=user, searched_users=users,
                               borrows=borrows)
    return redirect("/login")


# ------------------------------ #

# ---------- Comment & Rating Operations ---------- #
@app.route('/borrow-history', methods=['GET'])
def borrow_history():
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.USER.value:
            return redirect("/")
        borrows = get_not_returned_borrows_by_user_id(user.user_id)
        return render_template('borrow_history.html', title="Borrow History", user=user, borrows=borrows)
    return redirect("/login")


@app.route('/comment-rating/<isbn>', methods=['GET', 'POST'])
def comment_rating(isbn):
    if 'user' in session:
        user = deserialize(session['user'])
        if user.role is not Role.USER.value:
            return redirect("/")
        if request.method == 'POST':
            save_comment_rating(request.form, user.user_id, isbn)
            flash('You successfully added comment and rating')
            return redirect("/borrow-history")
        book = get_book_by_isbn(isbn)
        return render_template('comment_rating.html', title="Borrow History", user=user, book=book)
    return redirect("/login")

# ------------------------------ #

if __name__ == '__main__':
    app.run()
