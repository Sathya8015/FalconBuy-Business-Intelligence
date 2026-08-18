from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Popular delivery partners
partner_names = [
    "Blue Dart",
    "Delhivery",
    "DTDC",
    "Ekart",
    "Ecom Express",
    "Xpressbees",
    "India Post",
    "Shadowfax",
    "FedEx",
    "DHL"
]

# Service areas
service_areas = [
    "North India",
    "South India",
    "East India",
    "West India",
    "Tamil Nadu",
    "Karnataka",
    "Kerala",
    "Maharashtra",
    "Pan India",
    "Hyderabad"
]

# Empty list
delivery_partners = []

# Generate 10 records
for i in range(10):

    partner = {

        "Partner_Name": partner_names[i],

        "Contact_Number": fake.numerify(
            "9#########"
        ),

        "Email": fake.company_email(),

        "Service_Area": random.choice(
            service_areas
        ),

        "Rating": round(
            random.uniform(3.5, 5.0),
            1
        ),

        "Status": random.choices(
            ["Active", "Inactive"],
            weights=[90, 10],
            k=1
        )[0]

    }

    delivery_partners.append(partner)

# Create DataFrame
df = pd.DataFrame(delivery_partners)

# Show sample
print(df)

# Export CSV
df.to_csv(
    "Delivery_Partners_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Delivery_Partners_records.csv generated successfully!"
)
