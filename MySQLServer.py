import mysql.connector

def create_database():
    try:
        # Establish a connection to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abuubaida002@"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Create the database
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Print success message
        print("Database 'alx_book_store' created successfully!")

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        # Print error message
        print(f"Failed to create database: {err}")

if __name__ == "__main__":
    create_database()
