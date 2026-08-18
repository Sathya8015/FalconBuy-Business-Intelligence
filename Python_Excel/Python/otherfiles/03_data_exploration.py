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
customers_df = pd.read_sql("SELECT * FROM Customers;", connection)

print("=" * 60)
print("CUSTOMERS DATASET EXPLORATION")
print("=" * 60)

# Shape
print("\n1. Dataset Shape")
print(customers_df.shape)

# Columns
print("\n2. Column Names")
print(customers_df.columns.tolist())

# Information
print("\n3. Dataset Information")
customers_df.info()

# Missing Values
print("\n4. Missing Values")
print(customers_df.isnull().sum())

# Duplicate Rows
print("\n5. Duplicate Rows")
print(customers_df.duplicated().sum())

# Statistical Summary
print("\n6. Statistical Summary")
print(customers_df.describe())

# Data Types
print("\n7. Data Types")
print(customers_df.dtypes)

# First 5 Rows
print("\n8. First Five Records")
print(customers_df.head())

# Last 5 Rows
print("\n9. Last Five Records")
print(customers_df.tail())
