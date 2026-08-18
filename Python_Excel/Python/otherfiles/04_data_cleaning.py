import pandas as pd
import mysql.connector

# ======================================================
# DATABASE CONNECTION
# ======================================================

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="sathya123",
    database="falconbuy"
)

# ======================================================
# LOAD ALL TABLES
# ======================================================

tables = {
    "Customers": pd.read_sql("SELECT * FROM Customers;", connection),
    "Categories": pd.read_sql("SELECT * FROM Categories;", connection),
    "Products": pd.read_sql("SELECT * FROM Products;", connection),
    "Suppliers": pd.read_sql("SELECT * FROM Suppliers;", connection),
    "Inventory": pd.read_sql("SELECT * FROM Inventory;", connection),
    "Stores": pd.read_sql("SELECT * FROM Stores;", connection),
    "Employees": pd.read_sql("SELECT * FROM Employees;", connection),
    "Orders": pd.read_sql("SELECT * FROM Orders;", connection),
    "Order_Details": pd.read_sql("SELECT * FROM Order_Details;", connection),
    "Payments": pd.read_sql("SELECT * FROM Payments;", connection),
    "Shipments": pd.read_sql("SELECT * FROM shipments;", connection),
    "Returns": pd.read_sql("SELECT * FROM Returns;", connection),
    "Product_Reviews": pd.read_sql("SELECT * FROM Product_Reviews;", connection),
    "Marketing_Campaigns": pd.read_sql("SELECT * FROM Marketing_Campaigns;", connection),
    "Delivery_Partners": pd.read_sql("SELECT * FROM Delivery_Partners;", connection),
    "Regions": pd.read_sql("SELECT * FROM Regions;", connection),
    "Warehouses": pd.read_sql("SELECT * FROM Warehouses;", connection),
    "Departments": pd.read_sql("SELECT * FROM Departments;", connection),
    "Coupons": pd.read_sql("SELECT * FROM Coupons;", connection),
    "Loyalty_Program": pd.read_sql("SELECT * FROM Loyalty_Program;", connection),
}

# ======================================================
# CLEANING FUNCTION
# ======================================================

def clean_dataframe(df, table_name):

    print("\n" + "=" * 70)
    print(f"CLEANING TABLE : {table_name}")
    print("=" * 70)

    # -------------------------------
    # Dataset Shape
    # -------------------------------
    print("\nDataset Shape:")
    print(df.shape)

    # -------------------------------
    # Missing Values
    # -------------------------------
    print("\nMissing Values")
    print(df.isnull().sum())

    # -------------------------------
    # Duplicate Records
    # -------------------------------
    duplicates = df.duplicated().sum()

    print(f"\nDuplicate Records Before : {duplicates}")

    df.drop_duplicates(inplace=True)

    print(f"Duplicate Records After  : {df.duplicated().sum()}")

    # -------------------------------
    # Convert Date Columns
    # -------------------------------
    for column in df.columns:

        if "date" in column.lower() or "created" in column.lower() or "updated" in column.lower():

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    # -------------------------------
    # Standardize Text Columns
    # -------------------------------
    for column in df.select_dtypes(include="object").columns:

        df[column] = df[column].astype(str).str.strip()

    # Email → lowercase
    for column in df.columns:

        if "email" in column.lower():

            df[column] = df[column].str.lower()

    # Name Columns → Title Case
    for column in df.columns:

        if "name" in column.lower():

            df[column] = df[column].str.title()

    # -------------------------------
    # Data Types
    # -------------------------------
    print("\nData Types")
    print(df.dtypes)

    # -------------------------------
    # Statistical Summary
    # -------------------------------
    print("\nStatistical Summary")
    print(df.describe(include="all"))

    # -------------------------------
    # Preview
    # -------------------------------
    print("\nFirst 5 Records")
    print(df.head())

    print("\nLast 5 Records")
    print(df.tail())

    print(f"\n✅ {table_name} Cleaning Completed Successfully")

    return df

# ======================================================
# CLEAN EVERY TABLE
# ======================================================

cleaned_tables = {}

for table_name, dataframe in tables.items():

    cleaned_tables[table_name] = clean_dataframe(
        dataframe,
        table_name
    )

print("\n" + "=" * 70)
print("ALL TABLES CLEANED SUCCESSFULLY")
print("=" * 70)

connection.close()
