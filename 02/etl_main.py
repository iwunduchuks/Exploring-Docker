#import Libraries 
import requests
import pandas as pd 
from   datetime import datetime 
from src.functions import create_connection, create_table, insert_data

if __name__ == '__main__':
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

























































