#import Libraries 
import requests
import pandas as pd 
from   datetime import datetime 
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

# EXTRACT
# API endpoint for fetching all current rates
url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
headers = {'X-CoinAPI-Key': '0A4EC419-E056-44E2-B22B-CEDDB3C09AC0'}
response = requests.get(url, headers=headers)
    
if response.status_code == 200:
    
    # TRANSFROM
    data = response.json()
    dt   = datetime.strptime(data['time'], "%Y-%m-%dT%H:%M:%S.%f0Z")
    
    #Load
    #Create a database connection
    conn = create_connection("pricedata.db")
    
    if conn is not None:
        # Step 2: Create the table if it doesn't exist
        create_table(conn)
        #Insert data
        insert_data(conn, dt.date(), data['rate'], dt.hour, dt.minute)
        #Close the connection
        conn.close()
    else:
        print("Error: Unable to connect to the database.")
    
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")

























































