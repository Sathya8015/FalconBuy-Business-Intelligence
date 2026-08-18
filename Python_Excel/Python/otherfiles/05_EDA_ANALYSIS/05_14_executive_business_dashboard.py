import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import mysql.connector

# =====================================================
# FALCONBUY EXECUTIVE BUSINESS DASHBOARD
# =====================================================

try:

    print("="*90)
    print("CONNECTING TO FALCONBUY DATABASE...")
    print("="*90)

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

    customers = pd.read_sql("SELECT * FROM Customers;", connection)
    orders = pd.read_sql("SELECT * FROM Orders;", connection)
    products = pd.read_sql("SELECT * FROM Products;", connection)
    categories = pd.read_sql("SELECT * FROM Categories;", connection)
    suppliers = pd.read_sql("SELECT * FROM Suppliers;", connection)
    stores = pd.read_sql("SELECT * FROM Stores;", connection)
    employees = pd.read_sql("SELECT * FROM Employees;", connection)
    inventory = pd.read_sql("SELECT * FROM Inventory;", connection)
    payments = pd.read_sql("SELECT * FROM Payments;", connection)
    shipments = pd.read_sql("SELECT * FROM Shipments;", connection)
    returns = pd.read_sql("SELECT * FROM Returns;", connection)
    campaigns = pd.read_sql("SELECT * FROM Marketing_Campaigns;", connection)

    print("All Tables Loaded Successfully\n")

    print("="*90)
    print("FALCONBUY EXECUTIVE BUSINESS DASHBOARD")
    print("="*90)

    # =====================================================
    # CUSTOMER KPIs
    # =====================================================

    print("\nCUSTOMER KPIs")
    print("-"*90)

    print(f"Total Customers          : {len(customers)}")
    print(f"Active Customers         : {(customers['Customer_Status']=='Active').sum()}")
    print(f"Inactive Customers       : {(customers['Customer_Status']=='Inactive').sum()}")

    # =====================================================
    # SALES KPIs
    # =====================================================

    print("\nSALES KPIs")
    print("-"*90)

    print(f"Total Orders             : {len(orders)}")
    print(f"Total Revenue            : ₹{orders['Order_Total'].sum():,.2f}")
    print(f"Average Order Value      : ₹{orders['Order_Total'].mean():,.2f}")
    print(f"Maximum Order Value      : ₹{orders['Order_Total'].max():,.2f}")

    # =====================================================
    # PRODUCT KPIs
    # =====================================================

    print("\nPRODUCT KPIs")
    print("-"*90)

    print(f"Total Products           : {len(products)}")
    print(f"Available Products       : {(products['Product_Status']=='Available').sum()}")
    print(f"Out of Stock             : {(products['Product_Status']=='Out of Stock').sum()}")
    print(f"Discontinued             : {(products['Product_Status']=='Discontinued').sum()}")

    # =====================================================
    # INVENTORY KPIs
    # =====================================================

    print("\nINVENTORY KPIs")
    print("-"*90)

    print(f"Inventory Records        : {len(inventory)}")
    print(f"Total Stock Quantity     : {inventory['Stock_Quantity'].sum()}")
    print(f"Average Stock Quantity   : {inventory['Stock_Quantity'].mean():.2f}")

    # =====================================================
    # PAYMENT KPIs
    # =====================================================

    print("\nPAYMENT KPIs")
    print("-"*90)

    print(f"Total Payments           : {len(payments)}")
    print(f"Payment Amount           : ₹{payments['Amount'].sum():,.2f}")
    print(f"Successful Payments      : {(payments['Payment_Status']=='Success').sum()}")
    print(f"Failed Payments          : {(payments['Payment_Status']=='Failed').sum()}")

    # =====================================================
    # SHIPMENT KPIs
    # =====================================================

    print("\nSHIPMENT KPIs")
    print("-"*90)

    print(f"Total Shipments          : {len(shipments)}")
    print(f"Delivered Shipments      : {(shipments['Delivery_Status']=='Delivered').sum()}")
    print(f"Returned Shipments       : {(shipments['Delivery_Status']=='Returned').sum()}")

    # =====================================================
    # RETURN KPIs
    # =====================================================

    print("\nRETURN KPIs")
    print("-"*90)

    print(f"Total Returns            : {len(returns)}")
    print(f"Refund Amount            : ₹{returns['Refund_Amount'].sum():,.2f}")

    # =====================================================
    # STORE KPIs
    # =====================================================

    print("\nSTORE KPIs")
    print("-"*90)

    print(f"Total Stores             : {len(stores)}")
    print(f"Open Stores              : {(stores['Status']=='Open').sum()}")

    # =====================================================
    # EMPLOYEE KPIs
    # =====================================================

    print("\nEMPLOYEE KPIs")
    print("-"*90)

    print(f"Total Employees          : {len(employees)}")
    print(f"Average Salary           : ₹{employees['Salary'].mean():,.2f}")

    # =====================================================
    # SUPPLIER KPIs
    # =====================================================

    print("\nSUPPLIER KPIs")
    print("-"*90)

    print(f"Total Suppliers          : {len(suppliers)}")
    print(f"Average Rating           : {suppliers['Supplier_Rating'].mean():.2f}")

    # =====================================================
    # MARKETING KPIs
    # =====================================================

    print("\nMARKETING KPIs")
    print("-"*90)

    print(f"Campaigns                : {len(campaigns)}")
    print(f"Marketing Budget         : ₹{campaigns['Budget'].sum():,.2f}")
    print(f"Revenue Generated        : ₹{campaigns['Revenue_Generated'].sum():,.2f}")
    print(f"Average ROI              : {campaigns['ROI'].mean():.2f}%")

    # =====================================================
    # CATEGORY KPIs
    # =====================================================

    print("\nCATEGORY KPIs")
    print("-"*90)

    print(f"Total Categories         : {len(categories)}")
    print(f"Active Categories        : {(categories['Status']=='Active').sum()}")

    # =====================================================
    # OVERALL BUSINESS HEALTH
    # =====================================================

    print("\n" + "="*90)
    print("OVERALL BUSINESS HEALTH")
    print("="*90)

    print(f"Customers                : {len(customers)}")
    print(f"Orders                   : {len(orders)}")
    print(f"Products                 : {len(products)}")
    print(f"Revenue                  : ₹{orders['Order_Total'].sum():,.2f}")
    print(f"Payments                 : ₹{payments['Amount'].sum():,.2f}")
    print(f"Refunds                  : ₹{returns['Refund_Amount'].sum():,.2f}")
    print(f"Inventory Stock          : {inventory['Stock_Quantity'].sum()}")
    print(f"Marketing ROI            : {campaigns['ROI'].mean():.2f}%")

    print("="*90)
    print("EXECUTIVE DASHBOARD COMPLETED SUCCESSFULLY")
    print("="*90)

    connection.close()

except Exception as e:

    print("\nERROR OCCURRED")
    print(type(e).__name__)
    print(e)
