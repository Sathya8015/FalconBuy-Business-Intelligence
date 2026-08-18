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
# LOAD PAYMENTS TABLE
# =====================================================

payments = pd.read_sql(
    "SELECT * FROM Payments;",
    connection
)

payments["Payment_Date"] = pd.to_datetime(payments["Payment_Date"])

print("="*80)
print("FALCONBUY PAYMENT ANALYSIS")
print("="*80)

# =====================================================
# 1 Total Payments
# =====================================================

print("\n1. Total Payments")
print(payments.shape[0])

# =====================================================
# 2 Total Payment Amount
# =====================================================

print("\n2. Total Payment Amount")
print(f"₹{payments['Amount'].sum():,.2f}")

# =====================================================
# 3 Average Payment Amount
# =====================================================

print("\n3. Average Payment Amount")
print(f"₹{payments['Amount'].mean():,.2f}")

# =====================================================
# 4 Payment Method Distribution
# =====================================================

print("\n4. Payment Method Distribution")
print(payments["Payment_Method"].value_counts())

# =====================================================
# 5 Payment Status Distribution
# =====================================================

print("\n5. Payment Status Distribution")
print(payments["Payment_Status"].value_counts())

# =====================================================
# 6 Successful Payment Amount
# =====================================================

success_amount = payments[
    payments["Payment_Status"]=="Success"
]["Amount"].sum()

print("\n6. Successful Payment Amount")
print(f"₹{success_amount:,.2f}")

# =====================================================
# 7 Refunded Amount
# =====================================================

refund_amount = payments[
    payments["Payment_Status"]=="Refunded"
]["Amount"].sum()

print("\n7. Refunded Amount")
print(f"₹{refund_amount:,.2f}")

# =====================================================
# 8 Monthly Payment Trend
# =====================================================

monthly_payment = (
    payments
    .groupby(payments["Payment_Date"].dt.to_period("M"))
    ["Amount"]
    .sum()
)

print("\n8. Monthly Payment Trend")
print(monthly_payment)

# =====================================================
# 9 Top 10 Highest Payments
# =====================================================

top_payments = (
    payments
    .sort_values(
        by="Amount",
        ascending=False
    )
    .head(10)
)

print("\n9. Top 10 Highest Payments")

print(
    top_payments[
        [
            "Transaction_ID",
            "Payment_Method",
            "Amount"
        ]
    ]
)

# =====================================================
# 10 Payment Summary
# =====================================================

print("\n10. PAYMENT SUMMARY")

print(f"Total Transactions : {payments.shape[0]}")
print(f"Total Amount       : ₹{payments['Amount'].sum():,.2f}")
print(f"Average Amount     : ₹{payments['Amount'].mean():,.2f}")
print(f"Highest Payment    : ₹{payments['Amount'].max():,.2f}")
print(f"Lowest Payment     : ₹{payments['Amount'].min():,.2f}")

print("="*80)
print("PAYMENT ANALYSIS COMPLETED SUCCESSFULLY")
print("="*80)

connection.close()
