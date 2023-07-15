from flask import Flask, request, render_template
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


if __name__ == '__main__':
    app.run(port=3000)
