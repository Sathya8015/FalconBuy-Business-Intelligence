import pandas as pd
import mysql.connector

# ==========================================
# DATABASE CONNECTION
# ==========================================

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="sathya123",
    database="falconbuy"
)

# ==========================================
# LOAD TABLES
# ==========================================

products = pd.read_sql("SELECT * FROM Products;", connection)
categories = pd.read_sql("SELECT * FROM Categories;", connection)
suppliers = pd.read_sql("SELECT * FROM Suppliers;", connection)

print("="*70)
print("FALCONBUY PRODUCT ANALYSIS")
print("="*70)

# ==========================================
# 1 Total Products
# ==========================================

print("\n1. Total Products")
print(products.shape[0])

# ==========================================
# 2 Product Status
# ==========================================

print("\n2. Product Status")
print(products["Product_Status"].value_counts())

# ==========================================
# 3 Products by Category
# ==========================================

category_summary = (
    products
    .merge(categories, on="Category_ID")
    .groupby("Category_Name")
    .size()
    .sort_values(ascending=False)
)

print("\n3. Products by Category")
print(category_summary)

# ==========================================
# 4 Products by Supplier
# ==========================================

supplier_summary = (
    products
    .merge(suppliers, on="Supplier_ID")
    .groupby("Supplier_Name")
    .size()
    .sort_values(ascending=False)
)

print("\n4. Products by Supplier")
print(supplier_summary)

# ==========================================
# 5 Average Selling Price
# ==========================================

print("\n5. Average Selling Price")
print(f"₹{products['Selling_Price'].mean():,.2f}")

# ==========================================
# 6 Highest Selling Price
# ==========================================

print("\n6. Highest Selling Price")
print(f"₹{products['Selling_Price'].max():,.2f}")

# ==========================================
# 7 Lowest Selling Price
# ==========================================

print("\n7. Lowest Selling Price")
print(f"₹{products['Selling_Price'].min():,.2f}")

# ==========================================
# 8 Average Cost Price
# ==========================================

print("\n8. Average Cost Price")
print(f"₹{products['Cost_Price'].mean():,.2f}")

# ==========================================
# 9 Profit Margin Per Product
# ==========================================

products["Profit"] = (
    products["Selling_Price"] -
    products["Cost_Price"]
)

print("\n9. Average Profit")
print(f"₹{products['Profit'].mean():,.2f}")

# ==========================================
# 10 Top 10 Expensive Products
# ==========================================

top_products = (
    products[
        ["Product_Name", "Selling_Price"]
    ]
    .sort_values(
        by="Selling_Price",
        ascending=False
    )
    .head(10)
)

print("\n10. Top 10 Expensive Products")
print(top_products)

print("\n" + "="*70)
print("PRODUCT ANALYSIS COMPLETED SUCCESSFULLY")
print("="*70)

connection.close()
