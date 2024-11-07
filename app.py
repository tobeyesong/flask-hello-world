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
        ('Toan', 'Lam', 'CU Boulder', 'Team 1', 3308)
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Populated"


@app.route('/db_select')
def db_select():
    # Establish a connection to the PostgreSQL database using the connection URL (replace "your_db_url_here" with actual URL).
    conn = psycopg2.connect("your_db_url_here")
    # Create a cursor object to interact with the database.
    cur = conn.cursor()
    
    # Execute a SQL query to select all columns and rows from the 'Basketball' table.
    cur.execute("SELECT * FROM Basketball;")
    # Fetch all rows from the executed query and store them in 'records'.
    records = cur.fetchall()
    
    # Initialize a variable 'response' with an HTML table header, specifying column headers.
    response = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    
    # Loop through each row in the fetched records.
    for row in records:
        # Start a new row in the HTML table.
        response += "<tr>"
        # Loop through each cell in the current row.
        for cell in row:
            # Add each cell's value as a table data cell in the HTML table.
            response += f"<td>{cell}</td>"
        # Close the current row in the HTML table.
        response += "</tr>"
    
    # Close the HTML table.
    response += "</table>"
    
    # Close the cursor to free up database resources.
    cur.close()
    # Close the database connection.
    conn.close()
    
    # Return the response containing the HTML table to display in the browser.
    return response


