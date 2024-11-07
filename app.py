import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World from --your name-- in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab10_db_97vf_user:F2SHYRLNi59nqfsfJ7PpMp0aXmyMzsjn@dpg-csm2r1bqf0us73frn24g-a/lab10_db_97vf")
    conn.close()
    return "Database connection successful!"
