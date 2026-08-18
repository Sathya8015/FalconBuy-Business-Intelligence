import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import mysql.connector

try:

    print("=" * 80)
    print("CONNECTING TO DATABASE...")
    print("=" * 80)

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

    suppliers = pd.read_sql("SELECT * FROM Suppliers;", connection)
    products = pd.read_sql("SELECT * FROM Products;", connection)

    print("Tables Loaded Successfully\n")

    # =====================================================
    # MERGE TABLES
    # =====================================================

    supplier_df = suppliers.merge(
        products[
            [
                "Supplier_ID",
                "Product_ID",
                "Product_Name",
                "Selling_Price"
            ]
        ],
        on="Supplier_ID",
        how="left"
    )

    print("=" * 80)
    print("FALCONBUY SUPPLIER ANALYSIS")
    print("=" * 80)

    # =====================================================
    # 1 Total Suppliers
    # =====================================================

    print("\n1. Total Suppliers")
    print(len(suppliers))

    # =====================================================
    # 2 Supplier Status
    # =====================================================

    print("\n2. Supplier Status")
    print(suppliers["Status"].value_counts())

    # =====================================================
    # 3 Supplier Rating Distribution
    # =====================================================

    print("\n3. Supplier Rating Distribution")
    print(suppliers["Supplier_Rating"].value_counts().sort_index())

    # =====================================================
    # 4 Average Supplier Rating
    # =====================================================

    print("\n4. Average Supplier Rating")
    print(round(suppliers["Supplier_Rating"].mean(), 2))

    # =====================================================
    # 5 City-wise Suppliers
    # =====================================================

    print("\n5. City-wise Suppliers")
    print(suppliers["City"].value_counts())

    # =====================================================
    # 6 State-wise Suppliers
    # =====================================================

    print("\n6. State-wise Suppliers")
    print(suppliers["State"].value_counts())

    # =====================================================
    # 7 Country-wise Suppliers
    # =====================================================

    print("\n7. Country-wise Suppliers")
    print(suppliers["Country"].value_counts())

    # =====================================================
    # 8 Products per Supplier
    # =====================================================

    products_per_supplier = (
        supplier_df
        .groupby("Supplier_Name")
        .agg(
            Total_Products=("Product_ID", "count"),
            Average_Selling_Price=("Selling_Price", "mean")
        )
        .sort_values(
            by="Total_Products",
            ascending=False
        )
    )

    print("\n8. Products per Supplier")
    print(products_per_supplier)

    # =====================================================
    # 9 Top 10 Suppliers
    # =====================================================

    print("\n9. Top 10 Suppliers")

    print(products_per_supplier.head(10))

    # =====================================================
    # 10 Dashboard Summary
    # =====================================================

    print("\n" + "=" * 80)
    print("SUPPLIER DASHBOARD SUMMARY")
    print("=" * 80)

    print(f"Total Suppliers        : {len(suppliers)}")
    print(f"Active Suppliers       : {(suppliers['Status']=='Active').sum()}")
    print(f"Inactive Suppliers     : {(suppliers['Status']=='Inactive').sum()}")
    print(f"Average Rating         : {suppliers['Supplier_Rating'].mean():.2f}")
    print(f"Highest Rating         : {suppliers['Supplier_Rating'].max():.1f}")
    print(f"Products Managed       : {len(products)}")

    print("=" * 80)
    print("SUPPLIER ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 80)

    connection.close()

except Exception as e:

    print("\nERROR OCCURRED")
    print(type(e).__name__)
    print(e)
