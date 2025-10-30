from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection Config
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="rootpassword",
    database="flaskdb"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_record():
    name = request.form['name']
    email = request.form['email']
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return redirect('/records')

@app.route('/records')
def show_records():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template('records.html', records=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
