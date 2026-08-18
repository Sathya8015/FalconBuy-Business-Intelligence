from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Valid IDs
customer_ids = list(range(1, 5001))
product_ids = list(range(1, 501))

# Review titles
review_titles = [
    "Excellent Product",
    "Very Good",
    "Worth the Money",
    "Average Quality",
    "Highly Recommended",
    "Not Satisfied",
    "Good Value",
    "Amazing Experience",
    "Poor Packaging",
    "Fantastic Purchase"
]

# Empty list
reviews = []

# Generate 10,000 reviews
for i in range(1, 10001):

    rating = random.choices(
        [1, 2, 3, 4, 5],
        weights=[5, 10, 20, 30, 35],
        k=1
    )[0]

    review = {

        "Customer_ID": random.choice(customer_ids),

        "Product_ID": random.choice(product_ids),

        "Rating": rating,

        "Review_Title": random.choice(
            review_titles
        ),

        "Review_Text": fake.paragraph(
            nb_sentences=3
        ),

        "Review_Date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ).strftime("%Y-%m-%d")

    }

    reviews.append(review)

# Create DataFrame
df = pd.DataFrame(reviews)

# Show sample
print(df.head(10))

# Show total count
print("\nTotal Reviews:", len(df))

# Export CSV
df.to_csv(
    "Product_Reviews_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Product_Reviews_records.csv generated successfully!"
)
