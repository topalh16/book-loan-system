from flask import Flask, render_template, request, session, redirect
from service.UserService import attempt_login, get_all_users, save_user
from service.BookService import get_all_books, get_book_by_isbn, save_book, update_book
from service.AuthorService import get_all_authors, save_author
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
    print(user)
    if not user:
        return redirect('/login')

    session['user'] = serialize(user)
    return redirect('/')


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/login')


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
        return render_template('book.html', title=book.title, user=user, book=book)
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
        update_book(isbn, request.form)
        return redirect("/books")
    return redirect("/login")


# ------------------------------ #


if __name__ == '__main__':
    app.run()
