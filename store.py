import hashlib
from flask import Flask, request, redirect, flash, render_template
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import backref, relationship

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/store'
app.config['SECRET_KEY'] = 'as34k32223wsSS0rD34qCe3f034tq3oj'
app.config['DEBUG'] = True
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Items(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=False)
    price = Column(Float, unique=False)
    user_id = Column(Integer, ForeignKey('users.id'))


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=False)
    password = Column(Text, unique=False)
    firstName = Column(Text, unique=False)
    lastName = Column(Text, unique=False)
    items = relationship('Items', backref=backref('user'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Users, methods=['GET', 'POST', 'DELETE', 'PUT'],
                       include_columns=['id', 'email', 'firstName', 'lastName', 'items'])
api_manager.create_api(Items, methods=['GET', 'POST', 'DELETE', 'PUT'])
login_manager.login_view = 'login'


@app.before_request
def before_request():
    if '/api/' in str(request.url_rule):
        try:
            current_user.id
        except Exception as e:
            return redirect('/login')


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/validateLogin', methods=['POST'])
def validate_login():
    try:
        user = Users.query.filter_by(email=request.form['email']).first()
        salt = "812d47da9c414432360e3307495020a1wWa2"
        hashed_password = hashlib.sha512(request.form['password'] + salt).hexdigest()

        if (user is None) or (hashed_password != user.password):
            flash(u'Wrong email or password', 'danger')
            return redirect('/login')

        login_user(user)
        flash(u'Successfully logged in', 'success')
        return redirect('/')

    except Exception as e:
        flash(u'Something went terribly wrong', 'danger')
        return redirect('/login')


@app.route('/getUserId')
@login_required
def get_user_id():
    return str(current_user.id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'Successfully logged out', 'success')
    return redirect('/login')


if __name__ == '__main__':
    app.run()
