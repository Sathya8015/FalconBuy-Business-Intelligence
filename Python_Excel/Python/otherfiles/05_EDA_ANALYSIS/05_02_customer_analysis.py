import pandas as pd
import mysql.connector

# ============================================
# DATABASE CONNECTION
# ============================================

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="sathya123",
    database="falconbuy"
)

# ============================================
# LOAD CUSTOMERS TABLE
# ============================================

customers = pd.read_sql(
    "SELECT * FROM Customers;",
    connection
)

print("="*70)
print("FALCONBUY CUSTOMER ANALYSIS")
print("="*70)

# ============================================
# 1. Total Customers
# ============================================

print("\n1. Total Customers")
print(customers.shape[0])

# ============================================
# 2. Active vs Inactive Customers
# ============================================

print("\n2. Customer Status")
print(customers["Customer_Status"].value_counts())

# ============================================
# 3. Gender Distribution
# ============================================

print("\n3. Gender Distribution")
print(customers["Gender"].value_counts())

# ============================================
# 4. Customer Segment
# ============================================

print("\n4. Customer Segment")
print(customers["Customer_Segment"].value_counts())

# ============================================
# 5. Marital Status
# ============================================

print("\n5. Marital Status")
print(customers["Marital_Status"].value_counts())

# ============================================
# 6. Preferred Sales Channel
# ============================================

print("\n6. Preferred Channel")
print(customers["Preferred_Channel"].value_counts())

# ============================================
# 7. Preferred Payment Method
# ============================================

print("\n7. Preferred Payment Method")
print(customers["Preferred_Payment_Method"].value_counts())

# ============================================
# 8. Top 10 Cities
# ============================================

print("\n8. Top 10 Cities")

top_cities = customers["City"].value_counts().head(10)

print(top_cities)

# ============================================
# 9. Top 10 States
# ============================================

print("\n9. Top 10 States")

top_states = customers["State"].value_counts().head(10)

print(top_states)

# ============================================
# 10. Customer Join Trend
# ============================================

customers["Join_Date"] = pd.to_datetime(customers["Join_Date"])

join_trend = (
    customers
    .groupby(customers["Join_Date"].dt.to_period("M"))
    .size()
)

print("\n10. Monthly Customer Join Trend")

print(join_trend)

print("\n" + "="*70)
print("CUSTOMER ANALYSIS COMPLETED SUCCESSFULLY")
print("="*70)

connection.close()
