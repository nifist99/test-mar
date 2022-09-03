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
    cursor = mysql.connection.cursor()
    cursor.execute(''' 
        SELECT employee.status,user.name, branch.location
        FROM employee 
        INNER JOIN branch ON employee.branch = branch.id
        INNER JOIN user ON employee.id = user.id
        WHERE branch.location ='Bandung'
    ''')
    soal1 = cursor.fetchall()
    cursor.close()
    cursor2 = mysql.connection.cursor()
    cursor2.execute(''' 
        SELECT employee.department,user.name,user.gender,employee.join_date
        FROM user 
        INNER JOIN employee ON user.id = employee.id
        WHERE month(employee.join_date) =12
    ''')
    soal2 = cursor2.fetchall()
    cursor.close()
    cursor3 = mysql.connection.cursor()
    cursor3.execute(''' 
        SELECT COUNT(date_of_birth)
        FROM user
        WHERE year(date_of_birth) > 1990
    ''')
    soal3 = cursor3.fetchone()
    cursor.close()
    link = 'home'
    return render_template("index.html", menu=link , solusi1=soal1,solusi2=soal2,solusi3=soal3)

@app.route("/case1")
def case1():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM user''')
    user = cursor.fetchall()
    cursor.close()
    link = 'case1'
    name = 'users'
    return render_template("case1.html", menu=link,value=name,data=user)

@app.route("/case2")
def case2():
    cursor = mysql.connection.cursor()
    cursor.execute(''' 
        SELECT employee.*, branch.id as branch_id, branch.location, branch.position
        FROM employee
        INNER JOIN branch ON employee.branch = branch.id
    ''')
    employee = cursor.fetchall()
    cursor.close()
    link = 'case2'
    name = 'employee'
    return render_template("case2.html", menu=link,value=name,data=employee)

@app.route("/case3")
def case3():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM branch''')
    branch = cursor.fetchall()
    cursor.close()
    link = 'case3'
    name = 'branch'
    return render_template("case3.html", menu=link,value=name,data=branch)



if __name__ == "__main__":
    app.run(debug=True)

