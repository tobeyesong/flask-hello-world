import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World from --Toan Lam-- in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab10_db_97vf_user:F2SHYRLNi59nqfsfJ7PpMp0aXmyMzsjn@dpg-csm2r1bqf0us73frn24g-a/lab10_db_97vf")
    conn.close()
    return "Database connection successful!"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://lab10_db_97vf_user:F2SHYRLNi59nqfsfJ7PpMp0aXmyMzsjn@dpg-csm2r1bqf0us73frn24g-a/lab10_db_97vf")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Created"
