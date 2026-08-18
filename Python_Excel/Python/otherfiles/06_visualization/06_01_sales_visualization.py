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

# =====================================================
# LOAD ORDERS
# =====================================================

orders = pd.read_sql("SELECT * FROM Orders;", connection)

orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])

# =====================================================
# MONTHLY SALES
# =====================================================

monthly_sales = (
    orders
    .groupby(orders["Order_Date"].dt.to_period("M"))
    ["Order_Total"]
    .sum()
)

# =====================================================
# BAR CHART
# =====================================================

plt.figure(figsize=(12,6))

plt.bar(
    monthly_sales.index.astype(str),
    monthly_sales.values
)

plt.title("Monthly Revenue")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# =====================================================
# LINE CHART
# =====================================================

plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

connection.close()
