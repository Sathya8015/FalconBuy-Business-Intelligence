import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import mysql.connector

# =====================================================
# DATABASE CONNECTION
# =====================================================

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

    returns = pd.read_sql("SELECT * FROM Returns;", connection)
    products = pd.read_sql("SELECT * FROM Products;", connection)
    orders = pd.read_sql("SELECT * FROM Orders;", connection)

    print("Tables Loaded Successfully\n")

    # =====================================================
    # CONVERT DATE
    # =====================================================

    returns["Return_Date"] = pd.to_datetime(returns["Return_Date"])

    # =====================================================
    # MERGE TABLES
    # =====================================================

    return_df = (
        returns
        .merge(products[["Product_ID","Product_Name"]],
               on="Product_ID",
               how="left")
        .merge(orders[["Order_ID","Order_Total"]],
               on="Order_ID",
               how="left")
    )

    print("="*80)
    print("FALCONBUY RETURN ANALYSIS")
    print("="*80)

    # =====================================================
    # 1 Total Returns
    # =====================================================

    print("\n1. Total Returns")
    print(len(return_df))

    # =====================================================
    # 2 Total Refund Amount
    # =====================================================

    print("\n2. Total Refund Amount")
    print(f"₹{return_df['Refund_Amount'].sum():,.2f}")

    # =====================================================
    # 3 Return Status
    # =====================================================

    print("\n3. Return Status Distribution")
    print(return_df["Return_Status"].value_counts())

    # =====================================================
    # 4 Return Reasons
    # =====================================================

    print("\n4. Return Reasons")
    print(return_df["Return_Reason"].value_counts())

    # =====================================================
    # 5 Monthly Returns
    # =====================================================

    monthly_returns = (
        return_df
        .groupby(return_df["Return_Date"].dt.to_period("M"))
        .size()
    )

    print("\n5. Monthly Returns Trend")
    print(monthly_returns)

    # =====================================================
    # 6 Top Returned Products
    # =====================================================

    top_products = (
        return_df
        .groupby("Product_Name")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n6. Top Returned Products")
    print(top_products)

    # =====================================================
    # 7 Refund Amount by Product
    # =====================================================

    refund_product = (
        return_df
        .groupby("Product_Name")["Refund_Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n7. Refund Amount by Product")
    print(refund_product)

    # =====================================================
    # 8 Return Percentage
    # =====================================================

    total_orders = len(orders)
    total_returns = len(return_df)

    return_rate = (total_returns / total_orders) * 100

    print("\n8. Return Percentage")
    print(f"{return_rate:.2f}%")

    # =====================================================
    # 9 Highest Refunds
    # =====================================================

    highest_refunds = (
        return_df
        .sort_values(by="Refund_Amount", ascending=False)
        .head(10)
    )

    print("\n9. Highest Refunds")

    print(
        highest_refunds[
            [
                "Order_ID",
                "Product_Name",
                "Refund_Amount"
            ]
        ]
    )

    # =====================================================
    # 10 Executive Summary
    # =====================================================

    print("\n" + "="*80)
    print("RETURN DASHBOARD SUMMARY")
    print("="*80)

    print(f"Total Returns        : {total_returns}")
    print(f"Refund Amount        : ₹{return_df['Refund_Amount'].sum():,.2f}")
    print(f"Average Refund       : ₹{return_df['Refund_Amount'].mean():,.2f}")
    print(f"Highest Refund       : ₹{return_df['Refund_Amount'].max():,.2f}")
    print(f"Return Percentage    : {return_rate:.2f}%")

    print("="*80)
    print("RETURN ANALYSIS COMPLETED SUCCESSFULLY")
    print("="*80)

    connection.close()

except Exception as e:

    print("\nERROR OCCURRED")
    print(type(e).__name__)
    print(e)
