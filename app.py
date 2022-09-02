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

@app.route("/")
def index():
    nilai = 100
    return render_template("index.html", value=nilai)

@app.route("/loop")
def loop():
    hari = ["senin","selasa","rabu","kamis","jum'at","sabtu"]
    return render_template("loop.html", value=hari)

@app.route("/parsing/<int:nilai>")
def parsing(nilai):
    return render_template("index.html", value=nilai)

@app.route("/parsingargs")
def parsingargs():
    data = request.args.get("nilai")
    return "nilai {}".format(data)

if __name__ == "__main__":
    app.run(debug=True)

