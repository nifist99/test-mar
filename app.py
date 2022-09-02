from multiprocessing.sharedctypes import Value
from flask import Flask, render_template , url_for, redirect, request, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "mar2022"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mar'
mysql = MySQL(app)

def create_table():
    CS = mysql.connection.cursor()
    CS.execute('''CREATE TABLE user (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) , date_of_birth DATE, gender VARCHAR(20))''')
    CS.execute('''CREATE TABLE branch (id int PRIMARY KEY, location VARCHAR(20) , position VARCHAR(20))''')
    CS.execute('''CREATE TABLE employee (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, department VARCHAR(20) , join_date DATE, status VARCHAR(20), branch INTEGER)''')

    mysql.connection.commit()
    return 'Executed successfully create users'

@app.route("/migrate")
def main():
    migrate = create_table()
    return migrate

@app.route("/")
def index():
    link = 'home'
    return render_template("index.html", menu=link)

@app.route("/case1")
def case1():
    link = 'case1'
    name = 'users'
    return render_template("case1.html", menu=link,value=name)

@app.route("/case2")
def case2():
    link = 'case2'
    name = 'employee'
    return render_template("case2.html", menu=link,value=name)

@app.route("/case3")
def case3():
    link = 'case3'
    name = 'branch'
    return render_template("case3.html", menu=link,value=name)



if __name__ == "__main__":
    app.run(debug=True)

