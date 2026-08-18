from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')

# Valid IDs
department_ids = list(range(1, 11))
store_ids = list(range(1, 26))

# Designations
designations = [
    "Store Manager",
    "Assistant Manager",
    "Sales Executive",
    "Cashier",
    "Inventory Manager",
    "HR Executive",
    "Accountant",
    "Marketing Executive",
    "Customer Support",
    "Supervisor"
]

# Empty list
employees = []

# Generate 250 employees
for i in range(1, 251):

    designation = random.choice(designations)

    salary = round(
        random.uniform(20000, 120000),
        2
    )

    employee = {

        "Employee_Code": f"EMP{i:05d}",

        "First_Name": fake.first_name(),

        "Last_Name": fake.last_name(),

        "Department_ID": random.choice(
            department_ids
        ),

        "Store_ID": random.choice(
            store_ids
        ),

        "Email": fake.unique.email(),

        "Phone_Number": fake.numerify(
            "9#########"
        ),

        "Designation": designation,

        "Salary": salary,

        "Hire_Date": fake.date_between(
            start_date="-8y",
            end_date="today"
        ).strftime("%Y-%m-%d"),

        "Status": random.choices(
            ["Active", "Inactive"],
            weights=[90, 10],
            k=1
        )[0]

    }

    employees.append(employee)

# Create DataFrame
df = pd.DataFrame(employees)

# Show first 10 records
print(df.head(10))

# Show total records
print("\nTotal Employees:", len(df))

# Export CSV
df.to_csv(
    "Employees_records.csv",
    index=False,
    encoding="utf-8"
)

print(
    "\n✅ Employees_records.csv generated successfully!"
)
