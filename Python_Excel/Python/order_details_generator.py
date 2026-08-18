from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Read existing IDs from CSV files
customer_ids = pd.read_csv("Customer_IDs.csv")["Customer_ID"].tolist()
store_ids = pd.read_csv("Store_IDs.csv")["Store_ID"].tolist()
coupon_ids = pd.read_csv("Coupon_IDs.csv")["Coupon_ID"].tolist()

# Empty list to store order records
orders = []

# Generate 20,000 Orders
for i in range(1, 20001):

    # Generate Order Total
    order_total = round(random.uniform(500, 25000), 2)

    # Calculate GST (18%)
    tax_amount = round(order_total * 0.18, 2)

    # Shipping Charge
    if order_total >= 1000:
        shipping_charge = 0
    else:
        shipping_charge = 50

    # Net Amount
    net_amount = round(order_total + tax_amount + shipping_charge, 2)

    # Order Status
    order_status = random.choices(
        ["Delivered", "Shipped", "Confirmed", "Pending", "Cancelled", "Returned"],
        weights=[60, 15, 10, 8, 5, 2],
        k=1
    )[0]

    # Payment Status
    if order_status in ["Delivered", "Shipped", "Confirmed"]:
        payment_status = "Paid"
    elif order_status == "Pending":
        payment_status = "Pending"
    elif order_status == "Cancelled":
        payment_status = random.choice(["Failed", "Refunded"])
    else:
        payment_status = "Refunded"

    # Create Order Record
    order = {

        "Order_Number": f"ORD{i:06d}",

        "Customer_ID": random.choice(customer_ids),

        "Store_ID": random.choice(store_ids),

        "Coupon_ID": random.choice(coupon_ids),

        "Order_Date": fake.date_time_between(
            start_date='-2y',
            end_date='now'
        ).strftime("%Y-%m-%d %H:%M:%S"),

        "Order_Status": order_status,

        "Payment_Status": payment_status,

        "Order_Total": order_total,

        "Tax_Amount": tax_amount,

        "Shipping_Charge": shipping_charge,

        "Net_Amount": net_amount

    }

    orders.append(order)

# Convert to DataFrame
df = pd.DataFrame(orders)

# Display Sample
print(df.head())

# Total Records
print("\nTotal Orders Generated:", len(df))

# Export CSV
df.to_csv("Orders records.csv", index=False, encoding="utf-8")

print("\n✅ Orders records.csv generated successfully!")
