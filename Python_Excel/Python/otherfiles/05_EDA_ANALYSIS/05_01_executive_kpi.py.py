import pandas as pd
import mysql.connector

# =====================================================
# DATABASE CONNECTION
# =====================================================

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="sathya123",
    database="falconbuy"
)

# =====================================================
# LOAD TABLES
# =====================================================

customers = pd.read_sql("SELECT * FROM Customers;", connection)
orders = pd.read_sql("SELECT * FROM Orders;", connection)
products = pd.read_sql("SELECT * FROM Products;", connection)
categories = pd.read_sql("SELECT * FROM Categories;", connection)
suppliers = pd.read_sql("SELECT * FROM Suppliers;", connection)
stores = pd.read_sql("SELECT * FROM Stores;", connection)
employees = pd.read_sql("SELECT * FROM Employees;", connection)

# =====================================================
# KPI CALCULATIONS
# =====================================================

total_customers = customers.shape[0]
total_orders = orders.shape[0]
total_products = products.shape[0]
total_categories = categories.shape[0]
total_suppliers = suppliers.shape[0]
total_stores = stores.shape[0]
total_employees = employees.shape[0]

total_revenue = orders["Order_Total"].sum()

average_order_value = orders["Order_Total"].mean()

# =====================================================
# DISPLAY RESULTS
# =====================================================

print("="*60)
print("        FALCONBUY EXECUTIVE KPI SUMMARY")
print("="*60)

print(f"Total Customers      : {total_customers}")
print(f"Total Orders         : {total_orders}")
print(f"Total Products       : {total_products}")
print(f"Total Categories     : {total_categories}")
print(f"Total Suppliers      : {total_suppliers}")
print(f"Total Stores         : {total_stores}")
print(f"Total Employees      : {total_employees}")

print("-"*60)

print(f"Total Revenue        : ₹{total_revenue:,.2f}")
print(f"Average Order Value  : ₹{average_order_value:,.2f}")

print("="*60)

connection.close()
