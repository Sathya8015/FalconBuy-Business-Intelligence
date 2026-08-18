import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import mysql.connector

# =====================================================
# FALCONBUY - SHIPMENT ANALYSIS
# =====================================================

try:

    print("=" * 80)
    print("CONNECTING TO DATABASE...")
    print("=" * 80)

    # =====================================================
    # DATABASE CONNECTION
    # =====================================================

    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="sathya123",      # Replace with your MySQL password
        database="falconbuy"
    )

    print("✅ Database Connected Successfully\n")

    # =====================================================
    # LOAD TABLES
    # =====================================================

    print("Loading Shipments Table...")
    shipments = pd.read_sql("SELECT * FROM Shipments;", connection)

    print("Loading Orders Table...")
    orders = pd.read_sql("SELECT * FROM Orders;", connection)

    print("✅ Tables Loaded Successfully\n")

    # =====================================================
    # CONVERT DATE COLUMNS
    # =====================================================

    shipments["Shipment_Date"] = pd.to_datetime(shipments["Shipment_Date"])
    shipments["Delivery_Date"] = pd.to_datetime(shipments["Delivery_Date"])

    # =====================================================
    # MERGE TABLES
    # =====================================================

    shipment_df = pd.merge(
        shipments,
        orders[["Order_ID", "Order_Total"]],
        on="Order_ID",
        how="left"
    )

    print("✅ Tables Merged Successfully\n")

    # =====================================================
    # DELIVERY DAYS
    # =====================================================

    shipment_df["Delivery_Days"] = (
        shipment_df["Delivery_Date"] -
        shipment_df["Shipment_Date"]
    ).dt.days

    print("=" * 80)
    print("FALCONBUY SHIPMENT ANALYSIS")
    print("=" * 80)

    # =====================================================
    # 1 Total Shipments
    # =====================================================

    print("\n1. Total Shipments")
    print(len(shipment_df))

    # =====================================================
    # 2 Shipment Status Distribution
    # =====================================================

    print("\n2. Shipment Status Distribution")

    print(
        shipment_df["Delivery_Status"].value_counts()
    )

    # =====================================================
    # 3 Delivered Shipments
    # =====================================================

    delivered = shipment_df[
        shipment_df["Delivery_Status"] == "Delivered"
    ]

    print("\n3. Delivered Shipments")
    print(len(delivered))

    # =====================================================
    # 4 Returned Shipments
    # =====================================================

    returned = shipment_df[
        shipment_df["Delivery_Status"] == "Returned"
    ]

    print("\n4. Returned Shipments")
    print(len(returned))

    # =====================================================
    # 5 Average Delivery Time
    # =====================================================

    print("\n5. Average Delivery Time")

    print(
        round(
            shipment_df["Delivery_Days"].mean(),
            2
        ),
        "Days"
    )

    # =====================================================
    # 6 Monthly Shipments
    # =====================================================

    print("\n6. Monthly Shipment Trend")

    monthly_shipments = (
        shipment_df
        .groupby(
            shipment_df["Shipment_Date"].dt.to_period("M")
        )
        .size()
    )

    print(monthly_shipments)

    # =====================================================
    # 7 Revenue by Delivery Status
    # =====================================================

    print("\n7. Revenue by Delivery Status")

    revenue_status = (
        shipment_df
        .groupby("Delivery_Status")["Order_Total"]
        .sum()
    )

    print(revenue_status)

    # =====================================================
    # 8 Top 10 Longest Deliveries
    # =====================================================

    print("\n8. Top 10 Longest Deliveries")

    longest = (
        shipment_df
        .sort_values(
            by="Delivery_Days",
            ascending=False
        )
        .head(10)
    )

    print(
        longest[
            [
                "Shipment_ID",
                "Tracking_Number",
                "Delivery_Days"
            ]
        ]
    )

    # =====================================================
    # 9 Delivery Partner Performance
    # =====================================================

    print("\n9. Delivery Partner Performance")

    partner = (
        shipment_df
        .groupby("Delivery_Partner_ID")
        .agg(
            Total_Shipments=("Shipment_ID", "count"),
            Average_Delivery_Days=("Delivery_Days", "mean")
        )
        .sort_values(
            by="Total_Shipments",
            ascending=False
        )
    )

    print(partner)

    # =====================================================
    # 10 Dashboard Summary
    # =====================================================

    print("\n" + "=" * 80)
    print("SHIPMENT DASHBOARD SUMMARY")
    print("=" * 80)

    print(f"Total Shipments        : {len(shipment_df)}")
    print(f"Delivered Shipments    : {len(delivered)}")
    print(f"Returned Shipments     : {len(returned)}")
    print(f"Average Delivery Days  : {shipment_df['Delivery_Days'].mean():.2f}")
    print(f"Highest Order Value    : ₹{shipment_df['Order_Total'].max():,.2f}")
    print(f"Lowest Order Value     : ₹{shipment_df['Order_Total'].min():,.2f}")
    print(f"Total Shipment Revenue : ₹{shipment_df['Order_Total'].sum():,.2f}")

    print("=" * 80)
    print("SHIPMENT ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 80)

    connection.close()

except Exception as e:

    print("\n❌ ERROR OCCURRED")
    print(type(e).__name__)
    print(e)
