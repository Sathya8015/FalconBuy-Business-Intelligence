import pandas as pd
import mysql.connector

# Database Connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="sathya123",
    database="falconbuy"
)

# Load Customers Table
customers_df = pd.read_sql("select * from customers", connection)

# Display First 5 Rows
print(customers_df.head())
