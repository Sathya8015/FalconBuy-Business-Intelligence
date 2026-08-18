import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
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

print("="*80)
print("FALCONBUY FINAL DASHBOARD")
print("="*80)

# =====================================================
# LOAD TABLES
# =====================================================

orders = pd.read_sql("SELECT * FROM Orders;", connection)
payments = pd.read_sql("SELECT * FROM Payments;", connection)
shipments = pd.read_sql("SELECT * FROM Shipments;", connection)
returns = pd.read_sql("SELECT * FROM Returns;", connection)
products = pd.read_sql("SELECT * FROM Products;", connection)
inventory = pd.read_sql("SELECT * FROM Inventory;", connection)
stores = pd.read_sql("SELECT * FROM Stores;", connection)
customers = pd.read_sql("SELECT * FROM Customers;", connection)

orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])

# =====================================================
# FIGURE
# =====================================================

plt.figure(figsize=(18,12))

# =====================================================
# Chart 1
# Monthly Revenue
# =====================================================

plt.subplot(2,3,1)

monthly_sales = (
    orders.groupby(
        orders["Order_Date"].dt.to_period("M")
    )["Order_Total"].sum()
)

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Revenue")
plt.xticks(rotation=45)

# =====================================================
# Chart 2
# Payment Method
# =====================================================

plt.subplot(2,3,2)

payment_method = payments["Payment_Method"].value_counts()

plt.pie(
    payment_method,
    labels=payment_method.index,
    autopct="%1.1f%%"
)

plt.title("Payment Methods")

# =====================================================
# Chart 3
# Shipment Status
# =====================================================

plt.subplot(2,3,3)

shipment = shipments["Delivery_Status"].value_counts()

plt.bar(
    shipment.index,
    shipment.values
)

plt.title("Shipment Status")
plt.xticks(rotation=20)

# =====================================================
# Chart 4
# Product Status
# =====================================================

plt.subplot(2,3,4)

product_status = products["Product_Status"].value_counts()

plt.bar(
    product_status.index,
    product_status.values
)

plt.title("Product Status")
plt.xticks(rotation=20)

# =====================================================
# Chart 5
# Inventory Status
# =====================================================

plt.subplot(2,3,5)

inventory_status = inventory["Stock_Status"].value_counts()

plt.pie(
    inventory_status,
    labels=inventory_status.index,
    autopct="%1.1f%%"
)

plt.title("Inventory Status")

# =====================================================
# Chart 6
# Return Status
# =====================================================

plt.subplot(2,3,6)

return_status = returns["Return_Status"].value_counts()

plt.bar(
    return_status.index,
    return_status.values
)

plt.title("Return Status")
plt.xticks(rotation=20)

# =====================================================
# SHOW DASHBOARD
# =====================================================

plt.suptitle(
    "FalconBuy Executive Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.show()

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

print("\n" + "="*80)
print("EXECUTIVE KPI SUMMARY")
print("="*80)

print(f"Customers            : {len(customers)}")
print(f"Orders               : {len(orders)}")
print(f"Stores               : {len(stores)}")
print(f"Products             : {len(products)}")
print(f"Revenue              : ₹{orders['Order_Total'].sum():,.2f}")
print(f"Payments             : ₹{payments['Amount'].sum():,.2f}")
print(f"Refund Amount        : ₹{returns['Refund_Amount'].sum():,.2f}")
print(f"Inventory Quantity   : {inventory['Stock_Quantity'].sum():,}")
print(f"Delivered Orders     : {(shipments['Delivery_Status']=='Delivered').sum()}")
print(f"Successful Payments  : {(payments['Payment_Status']=='Success').sum()}")

print("="*80)
print("FALCONBUY DASHBOARD COMPLETED SUCCESSFULLY")
print("="*80)

connection.close()
