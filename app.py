from flask import Flask, render_template, request, session, redirect, escape
from service.UserService import attempt_login

app = Flask(__name__)
app.secret_key = b'czf_36./jsfmc'


@app.route('/')
def home():
    if 'user' in session:
        return 'Logged in as %s' % escape(session['user'][2])
    return redirect("/login")


@app.route('/login')
def login():
    if 'user' in session:
        return redirect("/")
    return render_template('login.html')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    user = attempt_login(request.form['email'], request.form['password'])
    if user == False:
        return redirect('/login')

    session['user'] = user
    return redirect('/')


if __name__ == '__main__':
    app.run()
