from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Valid IDs
order_ids = list(range(1, 20001))
product_ids = list(range(1, 501))

# Empty list
order_details = []

# Generate 80,000 records
for i in range(1, 80001):

    quantity = random.randint(1, 5)

    unit_price = round(
        random.uniform(100, 50000),
        2
    )

    discount = round(
        random.uniform(0, 20),
        2
    )

    line_total = round(
        (quantity * unit_price) - discount,
        2
    )

    order_detail = {

        "Order_ID": random.choice(order_ids),

        "Product_ID": random.choice(product_ids),

        "Quantity": quantity,

        "Unit_Price": unit_price,

        "Discount": discount,

        "Line_Total": line_total

    }

    order_details.append(order_detail)

# Create DataFrame
df = pd.DataFrame(order_details)

# Display sample
print(df.head(10))

# Show total records
print("\nTotal Order Details:", len(df))

# Export CSV
df.to_csv(
    "Order_Details_records.csv",
    index=False,
    encoding="utf-8"
)

print("\n✅ Order_Details_records.csv generated successfully!")
