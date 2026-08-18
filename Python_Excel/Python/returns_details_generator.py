from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Valid IDs
order_ids = list(range(1, 20001))
product_ids = list(range(1, 501))

# Return reasons
return_reasons = [
    "Damaged product",
    "Wrong item delivered",
    "Quality issue",
    "Product not as described",
    "Late delivery",
    "Changed mind",
    "Defective item",
    "Size mismatch"
]

# Empty list
returns = []

# Generate 3000 returns
for i in range(1, 3001):

    refund_amount = round(
        random.uniform(100, 25000),
        2
    )

    return_record = {

        "Order_ID": random.choice(order_ids),

        "Product_ID": random.choice(product_ids),

        "Return_Date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ).strftime("%Y-%m-%d"),

        "Return_Reason": random.choice(
            return_reasons
        ),

        "Refund_Amount": refund_amount,

        "Return_Status": random.choices(
            [
                "Requested",
                "Approved",
                "Rejected",
                "Completed"
            ],
            weights=[10, 20, 10, 60],
            k=1
        )[0]

    }

    returns.append(return_record)

# Create DataFrame
df = pd.DataFrame(returns)

# Show sample
print(df.head(10))

# Total records
print("\nTotal Returns:", len(df))

# Export CSV
df.to_csv(
    "Returns_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Returns_records.csv generated successfully!"
)
