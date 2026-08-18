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
# LOAD ORDERS TABLE
# =====================================================

orders = pd.read_sql(
    "SELECT * FROM Orders;",
    connection
)

# Convert Order_Date to datetime
orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])

print("=" * 70)
print("FALCONBUY ORDER ANALYSIS")
print("=" * 70)

# =====================================================
# 1. Total Orders
# =====================================================

print("\n1. Total Orders")
print(orders.shape[0])

# =====================================================
# 2. Order Status
# =====================================================

print("\n2. Order Status Distribution")
print(orders["Order_Status"].value_counts())

# =====================================================
# 3. Payment Status
# =====================================================

print("\n3. Payment Status Distribution")
print(orders["Payment_Status"].value_counts())

# =====================================================
# 4. Total Revenue
# =====================================================

print("\n4. Total Revenue")
print(f"₹{orders['Order_Total'].sum():,.2f}")

# =====================================================
# 5. Average Order Value
# =====================================================

print("\n5. Average Order Value")
print(f"₹{orders['Order_Total'].mean():,.2f}")

# =====================================================
# 6. Highest Order Value
# =====================================================

print("\n6. Highest Order Value")
print(f"₹{orders['Order_Total'].max():,.2f}")

# =====================================================
# 7. Lowest Order Value
# =====================================================

print("\n7. Lowest Order Value")
print(f"₹{orders['Order_Total'].min():,.2f}")

# =====================================================
# 8. Daily Orders
# =====================================================

print("\n8. Daily Orders")

daily_orders = orders.groupby(
    orders["Order_Date"].dt.date
).size()

print(daily_orders)

# =====================================================
# 9. Monthly Orders
# =====================================================

print("\n9. Monthly Orders")

monthly_orders = orders.groupby(
    orders["Order_Date"].dt.to_period("M")
).size()

print(monthly_orders)

# =====================================================
# 10. Monthly Revenue
# =====================================================

print("\n10. Monthly Revenue")

monthly_revenue = orders.groupby(
    orders["Order_Date"].dt.to_period("M")
)["Order_Total"].sum()

print(monthly_revenue)

print("\n" + "=" * 70)
print("ORDER ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

connection.close()
