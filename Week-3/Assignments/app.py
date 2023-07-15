from flask import (Flask, request, render_template,
                   make_response, redirect, url_for)
app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello, My Server!</h1>'


@app.route("/data")
def data():
    number = request.args.get('number')
    if number is None:
        return '<h1>Lack of Parameter<h1>'
    elif not number.isdigit():
        return '<h1>Wrong Parameter</h1>'
    else:
        number = int(number)
        result = sum(range(1, number + 1))
        return f'<h1>Result: {result}</h1>'


@app.route("/sum.html")
def sum_page():
    return render_template("sum.html")


@app.route("/myName")
def myName():
    userName = request.cookies.get('userID')
    if userName is None:
        return render_template("setcookie.html")
    else:
        return f"<h1>{userName}</h1>"


@app.route("/clearCookie")
def clear_cookie():
    resp = make_response("<h1>success</h1>")
    resp.set_cookie('userID', '', expires=0)
    return resp


@app.route("/trackName", methods=['GET', 'POST'])
def track_name():
    user_name = request.args.get('name')
    print(user_name)
    if user_name:
        resp = make_response(redirect(url_for('myName')))
        resp.set_cookie('userID', user_name)
        return resp


if __name__ == '__main__':
    app.run(port=3000)
