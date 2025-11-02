from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# ---------- Database Connection ----------
db = mysql.connector.connect(
    host=os.environ.get("MYSQL_HOST", "localhost"),
    user=os.environ.get("MYSQL_USER", "root"),
    password=os.environ.get("MYSQL_PASSWORD", "root"),
    database=os.environ.get("MYSQL_DB", "flaskdb")
)
cursor = db.cursor(dictionary=True)

# ---------- API Routes ----------
@app.route('/api/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    db.commit()
    return jsonify({'message': 'User added successfully'})

# --------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
