from src.functions import create_connection, create_table, insert_data

def load(data, dt):
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