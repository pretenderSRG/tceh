import json
from flask import Flask, request, json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class PasswordForm(FlaskForm):
    name = StringField(validators=[validators.Length(min=3, max=10)])
    password = PasswordField(validators=[validators.Length(min=6),
                                         validators.InputRequired(),
                                         validators.EqualTo('confirm', message='Passwords must match'),
    ])


app = Flask(__name__)


@app.route('/locales')
def locales():
    lst = {'ru': "mascal", 'en': "english", 'it': "italiano"}
    return json.jsonify(lst)


@app.route('/sum/<int:first>/<int:second>')
def sum_two(first, second):
    return str(first + second)


@app.route('/greet/<user_name>')
def greet(user_name):
    return "Hello, " + user_name


# @app.route('/form/user', method=['POST', 'GET'])
# def my_form():
#     if request.method == 'POST':
#         form = PasswordForm(request.form)
#         if form.validate():
#             return "Form is validate"
#         else:
#             return "Error"


if __name__ == "__main__":
    app.run()
