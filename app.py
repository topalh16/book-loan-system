from flask import Flask, render_template, request, session, redirect, escape
from service.UserService import attempt_login
from helper import serialize, deserialize

app = Flask(__name__)
app.secret_key = b'czf_36./jsfmc'


@app.route('/')
def home():
    if 'user' in session:
        user = deserialize(session['user'])
        return render_template('home.html')
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


if __name__ == '__main__':
    app.run()
