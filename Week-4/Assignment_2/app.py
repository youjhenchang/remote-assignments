from flask import (Flask, request, render_template)
app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello, My Server!</h1>'


@app.route("/home.html")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(port=3000)
