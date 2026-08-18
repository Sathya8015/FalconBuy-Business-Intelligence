from faker import Faker
import pandas as pd
import random

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Empty list to store customer data
customers = []

# Generate 5000 customers
for i in range(1, 5001):

    customer = {

        # For reference in CSV only (don't import this column into MySQL)
        "Customer_ID": i,

        "Customer_Code": f"CUST{i:05d}",

        "First_Name": fake.first_name(),

        "Last_Name": fake.last_name(),

        "Gender": random.choice(["Male", "Female"]),

        "Date_of_Birth": fake.date_of_birth(
            minimum_age=18,
            maximum_age=70
        ).strftime("%Y-%m-%d"),

        "Email": fake.email(),

        "Phone_Number": fake.numerify("9#########"),

        "Address": fake.street_address().replace("\n", ", "),

        "City": fake.city(),

        "State": fake.state(),

        "Postal_Code": fake.postcode(),

        "Country": "India",

        "Region_ID": random.randint(1, 10),

        "Occupation": fake.job().replace(",", " -"),

        "Annual_Income": random.randint(200000, 2500000),

        "Marital_Status": random.choice([
            "Single",
            "Married",
            "Divorced",
            "Widowed"
        ]),

        "Join_Date": fake.date_between(
            start_date='-5y',
            end_date='today'
        ).strftime("%Y-%m-%d"),

        "Customer_Status": "Active",

        "Preferred_Channel": random.choice([
            "Website",
            "Mobile App",
            "Store"
        ]),

        "Preferred_Payment_Method": random.choice([
            "UPI",
            "Credit Card",
            "Debit Card",
            "Net Banking",
            "Cash on Delivery"
        ]),

        "Customer_Segment": random.choice([
            "Bronze",
            "Silver",
            "Gold",
            "Platinum"
        ]),

        "Referral_Source": random.choice([
            "Google",
            "Facebook",
            "Instagram",
            "LinkedIn",
            "Friend",
            "YouTube",
            "Advertisement"
        ]),

        "Last_Login_Date": fake.date_time_between(
            start_date='-30d',
            end_date='now'
        ).strftime("%Y-%m-%d %H:%M:%S")

    }

    customers.append(customer)

# Convert to DataFrame
df = pd.DataFrame(customers)

# Display first few rows
print(df.head())

# Save to CSV
df.to_csv("Customers_records.csv", index=False, encoding="utf-8")

print(f"\n✅ {len(df)} customer records generated successfully!")
