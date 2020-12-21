from flask import Flask, render_template, request, session, redirect, escape
from service.UserService import attempt_login
from helper import serialize, deserialize

app = Flask(__name__)
app.secret_key = b'czf_36./jsfmc'


@app.route('/')
def home():
    if 'user' in session:
        user = deserialize(session['user'])
        return 'Logged in as %s' % escape(user.full_name)
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


if __name__ == '__main__':
    app.run()
