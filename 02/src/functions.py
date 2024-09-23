import sqlite3

# Function to create database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

# Function to create the table if it doesn't exist
def create_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS price_data (
                Date    DATE,
                Price   FLOAT,
                Hour    INTEGER,
                Minute  INTEGER
            ) ''')

# Function to insert data
def insert_data(conn, date, price, hour, minute):
    with conn:
        try:
            conn.execute('''
                INSERT INTO price_data (Date, Price, Hour, Minute) 
                VALUES (?, ?, ?, ?)
            ''', (date, price, hour, minute))
        except sqlite3.Error as e:
            print(f"Failed to insert data: {e}")
        else:
            print("Data successfully inserted into the database.")