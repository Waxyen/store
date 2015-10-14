from models import *


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/signin')
def signin():
    return app.send_static_file('signin.html')


app.debug = True

if __name__ == '__main__':
    app.run()
