from flask import Flask

app = Flask(__name__)


@app.route('/hello/<user>')
def home(user):
    return "hello user: " + user


@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return "sun of two numbers = " + str(x + y)


@app.route('/len/<s1>/<s2>/<s3>')
def mx_len(s1, s2, s3):
    max_len = sorted([s1, s2, s3], key=len, reverse=True)
    return "Max leb str is = " + max_len[0]


@app.route('/<path:pt>')
def path_exists(pt):
    import os
    check_path = os.path.exists(pt)
    # return "yes" if check_path else "no"
    return os.listdir(pt)


if __name__ == '__main__':
    app.run()
