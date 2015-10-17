import hashlib
from models import *
from flask import request, redirect, flash
from flask_login import login_user, login_required, logout_user


login_manager.login_view = 'signin'


@app.route('/')
@login_required
def index():
    return app.send_static_file('index.html')


@app.route('/signin')
def signin():
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

        login_user(user)
        flash('Successfully logged in')
        return redirect('/')

    except Exception as e:
        return redirect('/signin?error_something_unknown_went_wrong')


@app.route('/getUserId')
@login_required
def get_user_id():
    return str(session.get('user_id'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/signin')

if __name__ == '__main__':
    app.run()
