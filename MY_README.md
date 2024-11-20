# **Assessment and Documentation for Flask Application**

## **Description of the Project and Sources**

This Flask application connects to a PostgreSQL database and provides endpoints for basic database operations such as creating, inserting, selecting, and dropping a table. It also includes a root route that serves a static HTML page with user information.

---

## **Project Details**

- **URL**: The application would be hosted locally or on a web server; no deployment URL is provided.
- **Database**: PostgreSQL.
- **Purpose**: Demonstrates CRUD (Create, Read, Update, Delete) operations using Flask and psycopg2.
- **Documentation Format**: Primarily Python **docstrings** for route documentation and HTML strings within responses.

---

## **Good Examples of Comments and Documentation**

### **Good Section**

The `db_select` route has comprehensive inline comments explaining the flow of database interaction. Example:

```python
# Execute a SQL query to select all columns and rows from the 'Basketball' table.
cur.execute("SELECT * FROM Basketball;")

# Fetch all rows from the executed query and store them in 'records'.
records = cur.fetchall()

# Initialize a variable 'response' with an HTML table header, specifying column headers.
response = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
```

### **Good Practice**

The use of `try...except...finally` in `db_select` ensures that errors are handled gracefully and resources are cleaned up. This is good for robustness and debugging.

---

## **Issues With Current Documentation**

### **1. Missing Docstrings**

- The routes lack **docstrings** to explain their purpose, input, and output.

### **2. Security Concerns**

- Hardcoding sensitive database credentials (e.g., connection strings) is a bad practice. These should be stored in environment variables.

### **3. Lack of Reusability**

- Repeated code for creating database connections and cursors across routes makes the application harder to maintain and debug.

---

## **Improved Code With Docstrings**

Below is the revised Flask application with **docstrings** for each route, improvements to security (using environment variables), and reusable database functions.

---

### **Revised Code**

```python
import os
import psycopg2
from flask import Flask

app = Flask(__name__)

# Retrieve database credentials from environment variables for security
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://your_default_db_url")


def get_db_connection():
    """Create and return a new connection to the PostgreSQL database."""
    return psycopg2.connect(DATABASE_URL)


@app.route('/')
def index():
    """
    Root route that displays personal information.

    Returns:
        str: Static HTML containing the author's name, CU ID, and GitHub username.
    """
    return """
    <html>
        <body>
            <p>Name: Toan Lam</p>
            <p>CU ID: tola6570</p>
            <p>GitHub Username: tobeyesong</p>
        </body>
    </html>
    """


@app.route('/db_test')
def db_test():
    """
    Test the database connection.

    Returns:
        str: Success message if the database connection is established.
    """
    conn = get_db_connection()
    conn.close()
    return "Database connection successful!"


@app.route('/db_create')
def db_create():
    """
    Create the Basketball table in the database if it does not exist.

    Returns:
        str: Success message after table creation.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First VARCHAR(255),
            Last VARCHAR(255),
            City VARCHAR(255),
            Name VARCHAR(255),
            Number INT
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Created"


@app.route('/db_insert')
def db_insert():
    """
    Populate the Basketball table with predefined data.

    Returns:
        str: Success message after inserting data into the table.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Toan', 'Lam', 'CU Boulder', 'Team 1', 3308)
    ON CONFLICT DO NOTHING;  -- Prevent duplicate entries
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Populated"


@app.route('/db_select')
def db_select():
    """
    Select and display all rows from the Basketball table in an HTML table format.

    Returns:
        str: HTML table with data from the Basketball table.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Basketball;")
        records = cur.fetchall()
        response = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        for row in records:
            response += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
        response += "</table>"
        return response
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


@app.route('/db_drop')
def db_drop():
    """
    Drop the Basketball table from the database.

    Returns:
        str: Success message after dropping the table.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DROP TABLE Basketball;")
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Dropped"
```

---

## **Key Improvements Made**

### **1. Added Docstrings**

- **Before**: Routes had no explanations.
- **After**: Added detailed docstrings describing the purpose, inputs, and outputs for all routes.

---

### **2. Improved Security**

- **Before**: Database credentials were hardcoded in the code.
- **After**: Used `os.getenv` to retrieve the credentials from environment variables.

---

### **3. Reusability**

- **Before**: Each route created a database connection manually, leading to repetitive code.
- **After**: Added a reusable `get_db_connection` function.

---

## **Summary of Documentation and Code**

### **Good Aspects**

- The routes cover a wide range of operations, showcasing CRUD functionality.
- Inline comments in `db_select` clearly explain database logic.
- The use of `try...except...finally` ensures robustness.

### **Areas for Improvement**

1. **Security**: Using hardcoded credentials was a major issue.
2. **Docstrings**: Their absence made it difficult to understand the purpose of each route.
3. **Reusability**: Repeated code for database connections added unnecessary complexity.

---

### **What Was Changed**

1. **Added docstrings** to all routes.
2. **Replaced hardcoded credentials** with environment variables.
3. Refactored the code to include a **reusable database connection function**.

---

### **What Needs to Be Added**

1. **Unit Tests**: Test cases for each route to ensure robustness.
2. **Configuration Management**: Use a `.env` file for storing environment variables.
3. **Error Logging**: Add a logging mechanism to capture and debug database issues.
