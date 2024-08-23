import mysql.connector

def create_schema_and_insert_data():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="bbutvbd370vbqsdhzmg4-mysql.services.clever-cloud.com",
        user="username",
        password="mysqlpass",
        database="db",
        port="3306",
    )
    
    try:
        cursor = connection.cursor()
        cursor.execute("""SELECT message_text, sender_type FROM Messages WHERE session_id = 45 AND user_id = 51 ORDER BY created_at ASC;""")
        # cursor.execute("""SELECT * FROM Sessions;""")
        user = cursor.fetchall()
        print(user)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()


    

    # Close the connection
    cursor.close()
    connection.close()

# Call the function to create schema and insert data
create_schema_and_insert_data()
