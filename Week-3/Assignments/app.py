from flask import Flask, request, render_template, make_response
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
def name():
    userName = request.cookies.get('userID')
    if userName is None:
        return set_cookie_html()
    else:
        return get_cookie_html()


@app.route("/setcookie.html")
def set_cookie_html():
    return render_template("setcookie.html")


@app.route("/setcookie", methods=['POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('getcookie.html'))
        resp.set_cookie('userID', user)
    return resp


@app.route("/getcookie.html", methods=['GET'])
def get_cookie_html():
    return render_template('getcookie.html')


@app.route("/getcookie", methods=['GET'])
def getcookie():
    userName = request.cookies.get('userID')
    return f"<h1>{userName}</h1>"


if __name__ == '__main__':
    app.run(port=3000)
