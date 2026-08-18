from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Valid Order IDs
order_ids = list(range(1, 20001))

# Payment methods
payment_methods = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Wallet"
]

# Empty list
payments = []

# Generate 20,000 payments
for i in range(1, 20001):

    payment_status = random.choices(
        [
            "Success",
            "Pending",
            "Failed",
            "Refunded"
        ],
        weights=[85, 8, 4, 3],
        k=1
    )[0]

    amount = round(
        random.uniform(500, 30000),
        2
    )

    payment = {

        "Order_ID": i,

        "Transaction_ID": f"TXN{i:08d}",

        "Payment_Method": random.choice(
            payment_methods
        ),

        "Payment_Date": fake.date_time_between(
            start_date="-2y",
            end_date="now"
        ).strftime("%Y-%m-%d %H:%M:%S"),

        "Amount": amount,

        "Payment_Status": payment_status

    }

    payments.append(payment)

# Create DataFrame
df = pd.DataFrame(payments)

# Show first 10 rows
print(df.head(10))

# Show total records
print("\nTotal Payments:", len(df))

# Export CSV
df.to_csv(
    "Payments_records.csv",
    index=False,
    encoding="utf-8"
)

print("\n✅ Payments_records.csv generated successfully!")
