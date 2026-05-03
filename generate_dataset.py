import pandas as pd
import random
from datetime import datetime, timedelta

rows = 15000

locations = ["Delhi","Mumbai","Bangalore","Hyderabad","Chennai"]
merchants = ["Amazon","Flipkart","Swiggy","Zomato","Paytm"]

data = []

for i in range(rows):

    transaction_id = f"T{i+1}"
    user_id = f"U{random.randint(1,2000)}"
    amount = random.randint(50,50000)

    start_date = datetime(2024,1,1)
    transaction_time = start_date + timedelta(minutes=random.randint(0,500000))

    location = random.choice(locations)
    device_id = f"D{random.randint(1,500)}"
    merchant = random.choice(merchants)

    fraud_flag = 1 if random.random() < 0.04 else 0

    data.append([
        transaction_id,
        user_id,
        amount,
        transaction_time,
        location,
        device_id,
        merchant,
        fraud_flag
    ])

df = pd.DataFrame(data, columns=[
"transaction_id",
"user_id",
"amount",
"transaction_time",
"location",
"device_id",
"merchant",
"fraud_flag"
])

df.to_csv("dataset/transactions.csv", index=False)

print("Dataset generated successfully!")