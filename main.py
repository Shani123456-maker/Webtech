from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app = Flask(__name__, template_folder='template')



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'webtechpro'
mysql = MySQL(app)


@app.route('/')
def open():
    return render_template('intro.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form
        email = user['email']
        password = user['pwd']
        password_repeat = user['pwd-repeat']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO register VALUES (%s, %s, %s)", (email,password,password_repeat))
        mysql.connection.commit()
        cur.close()
        return render_template('/intro.html')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/course')
def course():
    return render_template('course.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
