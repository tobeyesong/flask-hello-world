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

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://lab10_db_97vf_user:F2SHYRLNi59nqfsfJ7PpMp0aXmyMzsjn@dpg-csm2r1bqf0us73frn24g-a/lab10_db_97vf")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Toan', 'Lam', 'CU Boulder', 'Team 1', 3308),
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://lab10_db_97vf_user:F2SHYRLNi59nqfsfJ7PpMp0aXmyMzsjn@dpg-csm2r1bqf0us73frn24g-a/lab10_db_97vf")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    response = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    for row in records:
        response += "<tr>"
        for cell in row:
            response += f"<td>{cell}</td>"
        response += "</tr>"
    response += "</table>"
    cur.close()
    conn.close()
    return response

