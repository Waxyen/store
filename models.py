from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, Text
from flask_restless import APIManager

app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/store'
db = SQLAlchemy(app)


class Items(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=False)
    price = Column(Float, unique=False)


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=False)
    password = Column(Text, unique=False)
    firstName = Column(Text, unique=False)
    lastName = Column(Text, unique=False)


api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Users, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Items, methods=['GET', 'POST', 'DELETE', 'PUT'])
