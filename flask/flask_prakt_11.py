import os
import random
from flask import Flask, request

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret',
    WTF_CSRF_ENABLED='False',
    FLASK_RANDOM_SEED=os.environ['s']
)


def random_number(sd):
    random.seed(sd)
    number = random.randint(0, 100)
    return number


NUMBER = random_number(os.environ['s'])


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'Число загадане'


@app.route('/<int:guess>', methods=['GET', 'POST'])
def guess_num(guess):
    if request.method == 'POST':
        if guess > NUMBER:
            return '>'
        elif guess < NUMBER:
            return '<'
    return '='
