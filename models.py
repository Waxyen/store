from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from flask_restless import APIManager
from sqlalchemy.orm import backref, relationship

app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/store'
app.config['SECRET_KEY'] = 'as34k32223wsSS0rD34qCe3f034tq3oj'
app.config['DEBUG'] = True
db = SQLAlchemy(app)


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


api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Users, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Items, methods=['GET', 'POST', 'DELETE', 'PUT'])
