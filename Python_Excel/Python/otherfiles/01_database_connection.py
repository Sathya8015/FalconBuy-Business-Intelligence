import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="sathya123"
    )

    print("✅ Connected!")

except mysql.connector.Error as err:
    print(err)
