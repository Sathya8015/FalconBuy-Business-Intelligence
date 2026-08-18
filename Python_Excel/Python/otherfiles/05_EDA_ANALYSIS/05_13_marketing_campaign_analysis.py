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
    # LOAD TABLE
    # =====================================================

    campaigns = pd.read_sql(
        "SELECT * FROM Marketing_Campaigns;",
        connection
    )

    print("Marketing Campaigns Loaded Successfully\n")

    # =====================================================
    # DATE CONVERSION
    # =====================================================

    campaigns["Start_Date"] = pd.to_datetime(campaigns["Start_Date"])
    campaigns["End_Date"] = pd.to_datetime(campaigns["End_Date"])

    # =====================================================
    # CAMPAIGN DURATION
    # =====================================================

    campaigns["Campaign_Duration"] = (
        campaigns["End_Date"] -
        campaigns["Start_Date"]
    ).dt.days

    print("=" * 80)
    print("FALCONBUY MARKETING CAMPAIGN ANALYSIS")
    print("=" * 80)

    # =====================================================
    # 1 Total Campaigns
    # =====================================================

    print("\n1. Total Campaigns")
    print(len(campaigns))

    # =====================================================
    # 2 Campaign Status
    # =====================================================

    print("\n2. Campaign Status")

    print(
        campaigns["Status"].value_counts()
    )

    # =====================================================
    # 3 Campaign Type
    # =====================================================

    print("\n3. Campaign Type")

    print(
        campaigns["Campaign_Type"].value_counts()
    )

    # =====================================================
    # 4 Total Budget
    # =====================================================

    print("\n4. Total Marketing Budget")

    print(f"₹{campaigns['Budget'].sum():,.2f}")

    # =====================================================
    # 5 Total Revenue
    # =====================================================

    print("\n5. Total Revenue Generated")

    print(f"₹{campaigns['Revenue_Generated'].sum():,.2f}")

    # =====================================================
    # 6 Average ROI
    # =====================================================

    print("\n6. Average ROI")

    print(f"{campaigns['ROI'].mean():.2f}%")

    # =====================================================
    # 7 Top ROI Campaigns
    # =====================================================

    print("\n7. Top 10 ROI Campaigns")

    top_roi = (
        campaigns
        .sort_values(
            by="ROI",
            ascending=False
        )
        .head(10)
    )

    print(
        top_roi[
            [
                "Campaign_Name",
                "Campaign_Type",
                "Budget",
                "Revenue_Generated",
                "ROI"
            ]
        ]
    )

    # =====================================================
    # 8 Budget vs Revenue
    # =====================================================

    print("\n8. Budget vs Revenue")

    comparison = campaigns[
        [
            "Campaign_Name",
            "Budget",
            "Revenue_Generated"
        ]
    ]

    print(comparison)

    # =====================================================
    # 9 Campaign Duration
    # =====================================================

    print("\n9. Campaign Duration")

    print(
        campaigns[
            [
                "Campaign_Name",
                "Campaign_Duration"
            ]
        ]
    )

    # =====================================================
    # 10 Dashboard Summary
    # =====================================================

    print("\n" + "=" * 80)
    print("MARKETING DASHBOARD SUMMARY")
    print("=" * 80)

    print(f"Total Campaigns      : {len(campaigns)}")
    print(f"Total Budget         : ₹{campaigns['Budget'].sum():,.2f}")
    print(f"Revenue Generated    : ₹{campaigns['Revenue_Generated'].sum():,.2f}")
    print(f"Average ROI          : {campaigns['ROI'].mean():.2f}%")
    print(f"Highest ROI          : {campaigns['ROI'].max():.2f}%")
    print(f"Average Duration     : {campaigns['Campaign_Duration'].mean():.2f} Days")

    print("=" * 80)
    print("MARKETING ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 80)

    connection.close()

except Exception as e:

    print("\nERROR OCCURRED")
    print(type(e).__name__)
    print(e)
