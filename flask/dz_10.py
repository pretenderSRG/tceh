import json
from flask import Flask, request, json
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError


def confirm_password(form, field):
    if form.data['password'] != form.data['confirm_password']:
        raise ValidationError("Пароли не совпадают")


class PasswordForm(FlaskForm):
    email = StringField(validators=[validators.Length(min=3, max=10),
                                    validators.Email()
                                    ])
    password = StringField(validators=[validators.Length(min=6, max=12)
                                       ])
    confirm_password = StringField(validators=[
        validators.Length(min=6, max=20), confirm_password
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret key',
    WTF_CSRF_ENABLED=False
)


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


@app.route('/form/user', methods=['GET', 'POST'])
def post_form():
    if request.method == 'POST':
        form = PasswordForm(request.form)
        status_output = {0: 'Проверка пройдена', 1: 'Ошибка валидации'}
        if form.validate():
            status_check = json.jsonify(status_output[0])
            return status_check
        else:
            status_check = json.jsonify(status_output[1])
            error_list = json.jsonify(form.errors)
            return status_check and error_list
    return "Done"


if __name__ == "__main__":
    app.run()
