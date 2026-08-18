from faker import Faker
import pandas as pd
import random
from datetime import timedelta

# Initialize Faker
fake = Faker('en_IN')

# Valid IDs
order_ids = list(range(1, 20001))
delivery_partner_ids = list(range(1, 11))

# Empty list
shipments = []

# Generate 20,000 shipments
for i in range(1, 20001):

    shipment_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    delivery_status = random.choices(
    [
        "Shipped",
        "In Transit",
        "Delivered",
        "Returned"
    ],
    weights=[15, 15, 65, 5],
    k=1
     )[0]

    # Delivery date logic
    if delivery_status == "Pending":

        delivery_date = None

    else:

        delivery_date = shipment_date + timedelta(
            days=random.randint(1, 10)
        )

    shipment = {

        "Order_ID": random.choice(order_ids),

        "Delivery_Partner_ID": random.choice(
            delivery_partner_ids
        ),

        "Tracking_Number": f"TRK{i:08d}",

        "Shipment_Date": shipment_date.strftime(
            "%Y-%m-%d"
        ),

        "Delivery_Date":
            delivery_date.strftime("%Y-%m-%d")
            if delivery_date
            else None,

        "Delivery_Status": delivery_status

    }

    shipments.append(shipment)

# Create DataFrame
df = pd.DataFrame(shipments)

# Display sample
print(df.head(10))

# Show total count
print("\nTotal Shipments:", len(df))

# Export CSV
df.to_csv(
    "Shipments_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Shipments_records.csv generated successfully!"
)
