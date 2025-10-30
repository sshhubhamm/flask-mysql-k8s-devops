from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

DB_CONFIG = {
    'host': os.getenv('DB_HOST','localhost'),
    'user': os.getenv('DB_USER','root'),
    'password': os.getenv('DB_PASS','rootpassword'),
    'database': os.getenv('DB_NAME','flaskdb')
}

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users")
    rows = [{'id':r[0],'name':r[1],'email':r[2]} for r in cur.fetchall()]
    cur.close(); conn.close()
    return jsonify(rows)

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name'); email = data.get('email')
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name,email) VALUES (%s,%s)", (name,email))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({'status':'ok'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
