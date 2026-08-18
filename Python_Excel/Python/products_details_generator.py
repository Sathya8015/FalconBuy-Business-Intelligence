from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Valid IDs
category_ids = list(range(1, 21))
supplier_ids = list(range(1, 11))

# Brands
brands = [
    "Samsung",
    "Apple",
    "Sony",
    "LG",
    "HP",
    "Dell",
    "Lenovo",
    "Puma",
    "Nike",
    "Adidas",
    "Boat",
    "OnePlus",
    "Mi",
    "Philips",
    "Tata"
]

# Empty list
products = []

# Generate 500 products
for i in range(1, 501):

    cost_price = round(
        random.uniform(100, 50000),
        2
    )

    profit_margin = round(
        random.uniform(10, 40),
        2
    )

    selling_price = round(
        cost_price * (1 + profit_margin / 100),
        2
    )

    product = {

        "Product_Code": f"PROD{i:05d}",

        "Product_Name": fake.word().title() + " " +
                        random.choice(
                            [
                                "Phone",
                                "Laptop",
                                "Headphones",
                                "Shirt",
                                "Watch",
                                "Speaker",
                                "TV",
                                "Bag",
                                "Shoes",
                                "Keyboard"
                            ]
                        ),

        "Category_ID": random.choice(
            category_ids
        ),

        "Supplier_ID": random.choice(
            supplier_ids
        ),

        "Brand": random.choice(
            brands
        ),

        "Cost_Price": cost_price,

        "Selling_Price": selling_price,

        "Profit_Margin": profit_margin,

        "Product_Status": random.choices(
            [
                "Available",
                "Out of Stock",
                "Discontinued"
            ],
            weights=[80, 15, 5],
            k=1
        )[0],

        "Launch_Date": fake.date_between(
            start_date="-5y",
            end_date="today"
        ).strftime("%Y-%m-%d"),

        "Warranty_Months": random.choice(
            [6, 12, 18, 24, 36]
        )

    }

    products.append(product)

# Create DataFrame
df = pd.DataFrame(products)

# Show first records
print(df.head(10))

# Show total records
print("\nTotal Products:", len(df))

# Export CSV
df.to_csv(
    "Products_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Products_records.csv generated successfully!"
)
