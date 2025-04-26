from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

# Database connection details (will be injected via ENV)
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'P@ssw0rd!!')

def log_to_db(ip_address):
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS access_log (id SERIAL PRIMARY KEY, ip VARCHAR(50));")
    cur.execute("INSERT INTO access_log (ip) VALUES (%s);", (ip_address,))
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def home():
    ip = request.remote_addr
    log_to_db(ip)
    return f"Successfully connect to the DB from IP Address: {ip}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
