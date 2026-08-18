import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import mysql.connector

try:

    print("="*80)
    print("CONNECTING TO DATABASE...")
    print("="*80)

    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="sathya123",
        database="falconbuy"
    )

    print("Database Connected Successfully\n")

    # =====================================================
    # LOAD TABLES
    # =====================================================

    stores = pd.read_sql("SELECT * FROM Stores;", connection)
    employees = pd.read_sql("SELECT * FROM Employees;", connection)
    orders = pd.read_sql("SELECT * FROM Orders;", connection)

    print("Tables Loaded Successfully\n")

    # =====================================================
    # MERGE TABLES
    # =====================================================

    orders_store = orders.merge(
        stores[["Store_ID", "Store_Name", "Store_Type", "City"]],
        on="Store_ID",
        how="left"
    )

    print("="*80)
    print("FALCONBUY STORE ANALYSIS")
    print("="*80)

    # =====================================================
    # 1 Total Stores
    # =====================================================

    print("\n1. Total Stores")
    print(len(stores))

    # =====================================================
    # 2 Store Type Distribution
    # =====================================================

    print("\n2. Store Type Distribution")
    print(stores["Store_Type"].value_counts())

    # =====================================================
    # 3 Store Status
    # =====================================================

    print("\n3. Store Status")
    print(stores["Status"].value_counts())

    # =====================================================
    # 4 City-wise Stores
    # =====================================================

    print("\n4. City-wise Stores")
    print(stores["City"].value_counts())

    # =====================================================
    # 5 Region-wise Stores
    # =====================================================

    print("\n5. Region-wise Stores")

    region = (
        stores.groupby("Region_ID")
        .size()
    )

    print(region)

    # =====================================================
    # 6 Employees Per Store
    # =====================================================

    print("\n6. Employees Per Store")

    emp_store = (
        employees.groupby("Store_ID")
        .size()
        .sort_values(ascending=False)
    )

    print(emp_store)

    # =====================================================
    # 7 Orders Per Store
    # =====================================================

    print("\n7. Orders Per Store")

    order_store = (
        orders_store.groupby("Store_Name")
        .size()
        .sort_values(ascending=False)
    )

    print(order_store)

    # =====================================================
    # 8 Revenue Per Store
    # =====================================================

    print("\n8. Revenue Per Store")

    revenue = (
        orders_store.groupby("Store_Name")["Order_Total"]
        .sum()
        .sort_values(ascending=False)
    )

    print(revenue)

    # =====================================================
    # 9 Top 10 Performing Stores
    # =====================================================

    print("\n9. Top 10 Performing Stores")

    top_store = (
        orders_store.groupby("Store_Name")["Order_Total"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_store)

    # =====================================================
    # 10 Executive Summary
    # =====================================================

    print("\n" + "="*80)
    print("STORE DASHBOARD SUMMARY")
    print("="*80)

    print(f"Total Stores          : {len(stores)}")
    print(f"Open Stores           : {(stores['Status']=='Open').sum()}")
    print(f"Employees             : {len(employees)}")
    print(f"Orders                : {len(orders)}")
    print(f"Revenue               : ₹{orders['Order_Total'].sum():,.2f}")
    print(f"Average Order Value   : ₹{orders['Order_Total'].mean():,.2f}")

    print("="*80)
    print("STORE ANALYSIS COMPLETED SUCCESSFULLY")
    print("="*80)

    connection.close()

except Exception as e:

    print("\nERROR OCCURRED")
    print(type(e).__name__)
    print(e)
