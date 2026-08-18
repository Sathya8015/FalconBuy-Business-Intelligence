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

products = pd.read_sql("SELECT * FROM Products;", connection)
categories = pd.read_sql("SELECT * FROM Categories;", connection)
order_details = pd.read_sql("SELECT * FROM Order_Details;", connection)

print("="*80)
print("FALCONBUY SALES ANALYSIS")
print("="*80)

# =====================================================
# MERGE TABLES
# =====================================================

sales = (
    order_details
    .merge(products, on="Product_ID")
    .merge(categories, on="Category_ID")
)

# =====================================================
# 1 Total Quantity Sold
# =====================================================

print("\n1. Total Quantity Sold")

print(sales["Quantity"].sum())

# =====================================================
# 2 Total Sales Revenue
# =====================================================

print("\n2. Total Sales Revenue")

print(f"₹{sales['Line_Total'].sum():,.2f}")

# =====================================================
# 3 Average Quantity Per Order
# =====================================================

print("\n3. Average Quantity Per Order")

print(round(sales["Quantity"].mean(),2))

# =====================================================
# 4 Top 10 Best Selling Products
# =====================================================

print("\n4. Top 10 Best Selling Products")

best_products = (
    sales
    .groupby("Product_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(best_products)

# =====================================================
# 5 Top Revenue Products
# =====================================================

print("\n5. Top Revenue Products")

top_revenue = (
    sales
    .groupby("Product_Name")["Line_Total"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_revenue)

# =====================================================
# 6 Category Revenue
# =====================================================

print("\n6. Category Revenue")

category_revenue = (
    sales
    .groupby("Category_Name")["Line_Total"]
    .sum()
    .sort_values(ascending=False)
)

print(category_revenue)

# =====================================================
# 7 Category Quantity
# =====================================================

print("\n7. Category Quantity Sold")

category_qty = (
    sales
    .groupby("Category_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print(category_qty)

# =====================================================
# 8 Top 10 Orders by Revenue
# =====================================================

print("\n8. Top Orders")

top_orders = (
    sales
    .groupby("Order_ID")["Line_Total"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_orders)

# =====================================================
# 9 Average Selling Price
# =====================================================

print("\n9. Average Selling Price")

print(f"₹{sales['Selling_Price'].mean():,.2f}")

# =====================================================
# 10 Overall Summary
# =====================================================

print("\n10. SALES SUMMARY")

print(f"Products Sold      : {sales['Product_ID'].nunique()}")

print(f"Categories         : {sales['Category_ID'].nunique()}")

print(f"Orders             : {sales['Order_ID'].nunique()}")

print(f"Revenue            : ₹{sales['Line_Total'].sum():,.2f}")

print(f"Quantity Sold      : {sales['Quantity'].sum()}")

print("="*80)
print("SALES ANALYSIS COMPLETED SUCCESSFULLY")
print("="*80)

connection.close()
