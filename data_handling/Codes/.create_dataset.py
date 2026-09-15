import pandas as pd
customers = [
    {
        "customer_id":1,
         "name": "rahul",
         "age": 24,
         "city": "delhi",
    },
    {
        "customer_id":2,
        "name": "priya",
         "age": 28,
         "city": "pune",
    },
    {
    "customer_id":3,
    "name": "amit",
    "age":31,
    "city": "mumbai",
    },
]
df = pd.DataFrame(customers)
print(df)
df.to_csv("customers.csv", index=False)
print("Data saved successfully.")