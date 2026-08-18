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

inventory = pd.read_sql("SELECT * FROM Inventory;", connection)
products = pd.read_sql("SELECT * FROM Products;", connection)

# =====================================================
# MERGE TABLES
# =====================================================

inventory_df = inventory.merge(
    products,
    on="Product_ID"
)

print("="*80)
print("FALCONBUY INVENTORY ANALYSIS")
print("="*80)

# =====================================================
# 1 Total Inventory Records
# =====================================================

print("\n1. Total Inventory Records")
print(len(inventory_df))

# =====================================================
# 2 Total Stock Quantity
# =====================================================

print("\n2. Total Stock Available")
print(inventory_df["Stock_Quantity"].sum())

# =====================================================
# 3 Average Stock
# =====================================================

print("\n3. Average Stock Quantity")
print(round(inventory_df["Stock_Quantity"].mean(),2))

# =====================================================
# 4 Stock Status
# =====================================================

print("\n4. Stock Status Distribution")
print(inventory_df["Stock_Status"].value_counts())

# =====================================================
# 5 Products Below Reorder Level
# =====================================================

low_stock = inventory_df[
    inventory_df["Stock_Quantity"] <
    inventory_df["Reorder_Level"]
]

print("\n5. Products Below Reorder Level")
print(low_stock[
    [
        "Product_Name",
        "Stock_Quantity",
        "Reorder_Level"
    ]
])

# =====================================================
# 6 Highest Stock Products
# =====================================================

top_stock = (
    inventory_df
    .sort_values(
        by="Stock_Quantity",
        ascending=False
    )
    .head(10)
)

print("\n6. Top 10 Highest Stock Products")
print(
    top_stock[
        [
            "Product_Name",
            "Stock_Quantity"
        ]
    ]
)

# =====================================================
# 7 Lowest Stock Products
# =====================================================

lowest_stock = (
    inventory_df
    .sort_values(
        by="Stock_Quantity"
    )
    .head(10)
)

print("\n7. Top 10 Lowest Stock Products")
print(
    lowest_stock[
        [
            "Product_Name",
            "Stock_Quantity"
        ]
    ]
)

# =====================================================
# 8 Warehouse-wise Stock
# =====================================================

warehouse_stock = (
    inventory_df
    .groupby("Warehouse_ID")
    ["Stock_Quantity"]
    .sum()
)

print("\n8. Warehouse-wise Stock")
print(warehouse_stock)

# =====================================================
# 9 Inventory Value
# =====================================================

inventory_df["Inventory_Value"] = (
    inventory_df["Stock_Quantity"] *
    inventory_df["Cost_Price"]
)

print("\n9. Total Inventory Value")
print(f"₹{inventory_df['Inventory_Value'].sum():,.2f}")

# =====================================================
# 10 Dashboard Summary
# =====================================================

print("\n10. INVENTORY SUMMARY")

print(f"Inventory Records : {len(inventory_df)}")
print(f"Products          : {inventory_df['Product_ID'].nunique()}")
print(f"Warehouses        : {inventory_df['Warehouse_ID'].nunique()}")
print(f"Stock Quantity    : {inventory_df['Stock_Quantity'].sum()}")
print(f"Inventory Value   : ₹{inventory_df['Inventory_Value'].sum():,.2f}")

print("="*80)
print("INVENTORY ANALYSIS COMPLETED SUCCESSFULLY")
print("="*80)

connection.close()
