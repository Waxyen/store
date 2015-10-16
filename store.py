import hashlib
from models import *
from flask import request, redirect, session, flash


@app.route('/')
def index():
    if session.get('user_id'):
        return app.send_static_file('index.html')
    else:
        return redirect('/signin?not_authorized')


@app.route('/signin')
def signin():
    if session.get('user_id'):
        return redirect('/')
    else:
        return app.send_static_file('signin.html')


@app.route('/validateLogin', methods=['POST'])
def validate_login():
    try:
        salt = "812d47da9c414432360e3307495020a1wWa2"
        email = request.form['email']
        hashed_password = hashlib.sha512(request.form['password'] + salt).hexdigest()

        user = Users.query.filter_by(email=email).first()

        if user is None:
            return redirect('/signin?no_user_by_that_email')

        if hashed_password != user.password:
            return redirect('/signin?wrong_password')

        session['user_id'] = user.id
        return redirect('/')

    except Exception as e:
        return redirect('/signin?error_something_unknown_went_wrong')


@app.route('/getUserId')
def get_user_id():
    if session.get('user_id'):
        return str(session.get('user_id'))


@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect('/signin')

if __name__ == '__main__':
    app.run()
