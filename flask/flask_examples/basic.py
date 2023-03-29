from flask import Flask, request
from werkzeug.routing import BaseConverter
app = Flask(__name__)
app.config.update({
    'DEBUG': 'True',
    'SECRET_KEY': 'Secret',
    'WTF_CSRF_ENABLED': 'False'
})


@app.route('/<path:user_name>')
def home(user_name):
    return 'hello user! {}'.format(user_name)


with app.test_request_context('/'):
    print(request, type(request), request.method, sep='*')

if __name__ == '__main__':
    app.run()




















# @app.route('/<user>')
# def username(user):
#     return 'hello, user: ' + user