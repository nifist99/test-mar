from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mar'

mysql = MySQL(app)

# mysql.init_app(app)

def create_table_user():
    CS = mysql.connection.cursor()
    CS.execute('''CREATE TABLE user (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) , date_of_birth DATE, gender VARCHAR(20))''')

    CS.execute('''INSERT INTO user VALUES ('Rakhmat','1997-01-12','M')''')
    CS.execute('''INSERT INTO user VALUES ('Revin','1998-02-16','M')''')
    CS.execute('''INSERT INTO user VALUES ('Rifat','1996-06-22','M')''')
    CS.execute('''INSERT INTO user VALUES ('Devina','1998-11-10','F')''')
    CS.execute('''INSERT INTO user VALUES ('Elsa','1997-10-30','F')''')
    CS.execute('''INSERT INTO user VALUES ('Yuli','1997-01-12','F')''')
    mysql.connection.commit()
    return 'Executed successfully create users'

def create_table_branch():
    CS = mysql.connection.cursor()
    CS.execute('''CREATE TABLE branch (id int PRIMARY KEY, location VARCHAR(20) , position VARCHAR(20))''')

    CS.execute('''INSERT INTO branch VALUES ('001','Bandung','Head Office')''')
    CS.execute('''INSERT INTO branch VALUES ('002','Solo')''')
    CS.execute('''INSERT INTO branch VALUES ('003','Surabaya')''')


    mysql.connection.commit()
    return 'Executed successfully create branch'

def create_table_employee():
    CS = mysql.connection.cursor()
    CS.execute('''CREATE TABLE employee (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, department VARCHAR(20) , join_date DATE, status VARCHAR(20), branch INTEGER)''')

    CS.execute('''INSERT INTO employee VALUES ('Finance','2020-09-22','Employee','001')''')
    CS.execute('''INSERT INTO employee VALUES ('IT','2019-12-17','Contract','001')''')
    CS.execute('''INSERT INTO employee VALUES ('HR','2021-08-02','Employee','001')''')
    CS.execute('''INSERT INTO employee VALUES ('Finance','2016-12-30','Contract','002')''')
    CS.execute('''INSERT INTO employee VALUES ('IT','2020-12-01','Employee','002')''')
    CS.execute('''INSERT INTO employee VALUES ('HR','2018-10-25','Contract','003')''')
    mysql.connection.commit()
    return 'Executed successfully create employees'

@app.route("/migrate")
def main():
    create_table_user()
    create_table_branch()
    create_table_employee()

if __name__=='__main__':
    app.run(debug=True)