from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Valid IDs
product_ids = list(range(1, 501))
warehouse_ids = list(range(1, 11))

# Empty list
inventory = []

# Generate inventory for each product in each warehouse
for product_id in product_ids:

    for warehouse_id in warehouse_ids:

        stock_quantity = random.randint(0, 1000)

        reorder_level = random.randint(50, 200)

        maximum_stock = random.randint(
            reorder_level + 100,
            1500
        )

        # Stock status logic
        if stock_quantity == 0:

            stock_status = "Out of Stock"

        elif stock_quantity <= reorder_level:

            stock_status = "Low Stock"

        else:

            stock_status = "In Stock"

        record = {

            "Product_ID": product_id,

            "Warehouse_ID": warehouse_id,

            "Stock_Quantity": stock_quantity,

            "Reorder_Level": reorder_level,

            "Maximum_Stock": maximum_stock,

            "Stock_Status": stock_status,

            "Last_Stock_Update": fake.date_between(
                start_date="-1y",
                end_date="today"
            ).strftime("%Y-%m-%d")

        }

        inventory.append(record)

# Create DataFrame
df = pd.DataFrame(inventory)

# Show first 10 rows
print(df.head(10))

# Show total records
print("\nTotal Inventory Records:", len(df))

# Export CSV
df.to_csv(
    "Inventory_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Inventory_records.csv generated successfully!"
)
