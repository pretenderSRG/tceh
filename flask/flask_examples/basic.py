from flask import Flask
from werkzeug.routing import BaseConverter
app = Flask(__name__)


@app.route('/<path:user_name>')
def home(user_name):
    return 'hello user! {}'.format(user_name)



if __name__ == '__main__':
    app.run()




















# @app.route('/<user>')
# def username(user):
#     return 'hello, user: ' + user