from src.functions import create_connection, create_table, insert_data
import pandas as pd

def load(data, dt):
    #Create a database connection
    conn = create_connection("pricedata.db")

    if conn is not None:
        # Step 2: Create the table if it doesn't exist
        create_table(conn)
        #Insert data
        insert_data(conn, dt.date().__str__(), data['rate'], dt.hour, dt.minute)
        #Close the connection
        conn.close()
    else:
        print("Error: Unable to connect to the database.")

def load_to_csv(data, dt):
    dict = {
        'Date': [dt.date().__str__()],
        'Price': [data['rate']],
        'Hour': [dt.hour],
        'Minute': [dt.minute]
    }
    Df = pd.DataFrame(dict)
    Df.to_csv('price_data', mode='a', header=True, index= False)
    print('Data loading successful')