from faker import Faker
import pandas as pd
import random
from datetime import timedelta

# Initialize Faker
fake = Faker('en_IN')

# Valid Customer IDs
customer_ids = list(range(1, 5001))

# Empty list
loyalty_records = []

# Generate 5000 loyalty records
for i, customer_id in enumerate(customer_ids, start=1):

    join_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )

    expiry_date = join_date + timedelta(
        days=365
    )

    membership_level = random.choices(
        [
            "Bronze",
            "Silver",
            "Gold",
            "Platinum"
        ],
        weights=[50, 30, 15, 5],
        k=1
    )[0]

    loyalty = {

        "Customer_ID": customer_id,

        "Membership_Level": membership_level,

        "Reward_Points": random.randint(
            100,
            50000
        ),

        "Join_Date": join_date.strftime(
            "%Y-%m-%d"
        ),

        "Expiry_Date": expiry_date.strftime(
            "%Y-%m-%d"
        ),

        "Status": random.choices(
            [
                "Active",
                "Inactive"
            ],
            weights=[90,10],
            k=1
        )[0]

    }

    loyalty_records.append(loyalty)


# Convert DataFrame
df = pd.DataFrame(loyalty_records)

# Display sample
print(df.head(10))

# Total records
print("\nTotal Loyalty Records:", len(df))


# Export CSV
df.to_csv(
    "Loyalty_Program_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Loyalty_Program_records.csv generated successfully!"
)
