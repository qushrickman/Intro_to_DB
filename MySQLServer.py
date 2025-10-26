import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # 1️⃣ Connect to MySQL Server (change user/password as per your system)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Charleskuria99@@',  # <-- change this
            auth_plugin='mysql_native_password'  # ensures compatibility
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # 2️⃣ Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # 3️⃣ Ensure clean close of cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
