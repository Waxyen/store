import hashlib
from flaskext.mysql import MySQL
from models import *
from flask import request, redirect, session

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'store'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

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
def validateLogin():
    try:
        email = request.form['email']
        password = request.form['password']

        salt = "812d47da9c414432360e3307495020a1wWa2"
        hashed_password = hashlib.sha512(password + salt).hexdigest()

        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from users where email='" + email + "' and password='" + hashed_password + "'")
        data = cursor.fetchone()
        if data is None:
            cursor.close()
            return redirect('/signin?error_wrong_email_or_password')
        else:
            cursor.close()
            session['user_id'] = data[0]
            return redirect('/')

    except Exception as e:
        return redirect('/signin?error_something_unknown_went_wrong')


@app.route('/getUserId')
def getUserId():
    if session.get('user_id'):
        return str(session.get('user_id'))


@app.route('/signout')
def logout():
    session.pop('user_id',None)
    return redirect('/signin')


app.debug = True

if __name__ == '__main__':
    app.secret_key = 'A0Zr45j/3yX R~DDH!skN]LZX/,?RT'
    app.run()
