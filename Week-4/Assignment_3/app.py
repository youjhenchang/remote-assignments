from flask import (Flask, flash, request, render_template,
                   make_response, redirect, url_for)
import pymysql
import pymysql.cursors
app = Flask(__name__)


def connect_to_server():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='CCUEsql78562',
                                 database='assignment')
    cursor = connection.cursor()
    return (connection, cursor)


@app.route("/")
def index():
    return '<h1>Hello, My Server!</h1>'


@app.route("/homepage")
def homepage():
    return render_template('homepage.html')


@app.route("/memberpage")
def memberpage():
    return render_template('memberpage.html')


@app.route("/signin", methods=["POST", "GET"])
def sign_in():
    email = request.form['email']
    password = request.form['password']
    sql = "SELECT * FROM `user` WHERE `email`= %s AND `password`= %s"
    cursor.execute(sql, (email, password))
    if (cursor.rowcount == 0):
        flash("Login fail")
        resp = make_response(redirect(url_for('homepage')))
        return resp
    else:
        flash("Login Success")
        resp = make_response(redirect(url_for('memberpage')))
        return resp


@app.route("/signup", methods=["POST", "GET"])
def sign_up():
    email = request.form['email']
    password = request.form['password']
    sql = "SELECT * FROM `user` WHERE `email`=%s"
    cursor.execute(sql, (email))
    if (cursor.rowcount == 0):
        sql_2 = "INSERT INTO `user`(`email`,`password`) VALUES (%s,%s)"
        cursor.execute(sql_2, (email, password))
        resp = make_response(redirect(url_for('memberpage')))
        flash("Welcome,new member!")
        return resp

    else:
        flash("Account already exists.")
        resp = make_response(redirect(url_for('homepage')))
        return resp


@app.route("/test_read")
def test_read():
    # Read a single record
    sql = "SELECT * FROM `user` WHERE `id`=1"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    return "<h1>success</h1>"


@app.route("/test_write")
def test_write():
    # write a single record
    sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, ('e', 'f'))
    connection.commit()
    return "<h1>success</h1>"


if __name__ == '__main__':
    (connection, cursor) = connect_to_server()
    app.secret_key = 'super secret key'
    app.run(port=3000, debug=True)
