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

    employees = pd.read_sql("SELECT * FROM Employees;", connection)
    stores = pd.read_sql("SELECT * FROM Stores;", connection)

    print("Tables Loaded Successfully\n")

    # =====================================================
    # CONVERT DATE
    # =====================================================

    employees["Hire_Date"] = pd.to_datetime(employees["Hire_Date"])

    # =====================================================
    # MERGE TABLES
    # =====================================================

    employee_df = employees.merge(
        stores[
            [
                "Store_ID",
                "Store_Name",
                "City",
                "Store_Type"
            ]
        ],
        on="Store_ID",
        how="left"
    )

    print("=" * 80)
    print("FALCONBUY EMPLOYEE ANALYSIS")
    print("=" * 80)

    # =====================================================
    # 1 Total Employees
    # =====================================================

    print("\n1. Total Employees")
    print(len(employee_df))

    # =====================================================
    # 2 Employee Status
    # =====================================================

    print("\n2. Employee Status")
    print(employee_df["Status"].value_counts())

    # =====================================================
    # 3 Department-wise Employees
    # =====================================================

    print("\n3. Department-wise Employees")

    department = (
        employee_df
        .groupby("Department_ID")
        .size()
        .sort_values(ascending=False)
    )

    print(department)

    # =====================================================
    # 4 Designation-wise Employees
    # =====================================================

    print("\n4. Designation-wise Employees")

    print(
        employee_df["Designation"]
        .value_counts()
    )

    # =====================================================
    # 5 Store-wise Employees
    # =====================================================

    print("\n5. Store-wise Employees")

    store_emp = (
        employee_df
        .groupby("Store_Name")
        .size()
        .sort_values(ascending=False)
    )

    print(store_emp)

    # =====================================================
    # 6 Salary Analysis
    # =====================================================

    print("\n6. Salary Statistics")

    print(f"Average Salary : ₹{employee_df['Salary'].mean():,.2f}")
    print(f"Maximum Salary : ₹{employee_df['Salary'].max():,.2f}")
    print(f"Minimum Salary : ₹{employee_df['Salary'].min():,.2f}")

    # =====================================================
    # 7 Top 10 Highest Paid Employees
    # =====================================================

    highest_paid = (
        employee_df
        .sort_values(by="Salary", ascending=False)
        .head(10)
    )

    print("\n7. Top 10 Highest Paid Employees")

    print(
        highest_paid[
            [
                "Employee_Code",
                "First_Name",
                "Last_Name",
                "Designation",
                "Salary"
            ]
        ]
    )

    # =====================================================
    # 8 Department Salary Analysis
    # =====================================================

    dept_salary = (
        employee_df
        .groupby("Department_ID")["Salary"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n8. Average Salary by Department")

    print(dept_salary)

    # =====================================================
    # 9 Hiring Trend
    # =====================================================

    hiring = (
        employee_df
        .groupby(employee_df["Hire_Date"].dt.year)
        .size()
    )

    print("\n9. Hiring Trend")

    print(hiring)

    # =====================================================
    # 10 Executive Dashboard
    # =====================================================

    print("\n" + "=" * 80)
    print("EMPLOYEE DASHBOARD SUMMARY")
    print("=" * 80)

    print(f"Total Employees     : {len(employee_df)}")
    print(f"Active Employees    : {(employee_df['Status']=='Active').sum()}")
    print(f"Inactive Employees  : {(employee_df['Status']=='Inactive').sum()}")
    print(f"Departments         : {employee_df['Department_ID'].nunique()}")
    print(f"Stores              : {employee_df['Store_ID'].nunique()}")
    print(f"Average Salary      : ₹{employee_df['Salary'].mean():,.2f}")
    print(f"Highest Salary      : ₹{employee_df['Salary'].max():,.2f}")

    print("=" * 80)
    print("EMPLOYEE ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 80)

    connection.close()

except Exception as e:

    print("\nERROR OCCURRED")
    print(type(e).__name__)
    print(e)
