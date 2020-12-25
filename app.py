from flask import Flask, render_template, request, session, redirect, escape
from service.UserService import attempt_login, get_all_users, save_user
from service.BookService import get_all_books
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


@app.route('/books')
def books():
    if 'user' in session:
        user = deserialize(session['user'])
        books = get_all_books()
        return render_template('books.html', title="Books", user=user, books=books)
    return redirect("/login")

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

if __name__ == '__main__':
    app.run()
