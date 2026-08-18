from faker import Faker
import pandas as pd
import random
from datetime import timedelta

# Initialize Faker
fake = Faker('en_IN')

# Empty list
campaigns = []

# Campaign Types
campaign_types = [
    "Email Marketing",
    "Social Media",
    "Google Ads",
    "Influencer Marketing",
    "TV Advertisement",
    "Festival Offer",
    "Seasonal Sale",
    "Referral Program",
    "Flash Sale",
    "SMS Marketing"
]

# Generate 100 Campaigns
for i in range(1, 101):

    start_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )

    end_date = start_date + timedelta(
        days=random.randint(15, 90)
    )

    budget = round(
        random.uniform(50000, 2000000),
        2
    )

    revenue_generated = round(
        budget * random.uniform(0.8, 5.5),
        2
    )

    roi = round(
        ((revenue_generated - budget) / budget) * 100,
        2
    )

    campaign = {

        "Campaign_Name": f"Campaign {i}",

        "Campaign_Type": random.choice(
            campaign_types
        ),

        "Start_Date": start_date.strftime(
            "%Y-%m-%d"
        ),

        "End_Date": end_date.strftime(
            "%Y-%m-%d"
        ),

        "Budget": budget,

        "Revenue_Generated": revenue_generated,

        "ROI": roi,

        "Status": random.choices(
            [
                "Planned",
                "Active",
                "Completed"
            ],
            weights=[15,25,60],
            k=1
        )[0]

    }

    campaigns.append(campaign)

# Create DataFrame
df = pd.DataFrame(campaigns)

# Display sample
print(df.head(10))

# Display total records
print("\nTotal Campaigns:", len(df))

# Export CSV
df.to_csv(
    "Marketing_Campaigns_records.csv",
    index=False,
    encoding="utf-8"
)

print("\n✅ Marketing_Campaigns_records.csv generated successfully!")
