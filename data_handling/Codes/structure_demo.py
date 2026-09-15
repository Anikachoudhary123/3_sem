import pandas as pd 
import json 
structured_data = {
    "id":[1,2,3],
    "name": ["rahul","priya","amit"],
    "age": [25,28,30]
}
df = pd.DataFrame(structured_data)
print("structured data:")
print(df)
json_data = {
    "customers": [
        {"id":1, "name": "rahul","age":25},
        {"id":2, "name": "priya", "age":28},
        {"id":3, "name": "amit", "age":30}
    ]
}
with open("customers.json", "w") as file:
    json.dump(json_data, file,indent=4)
    print("\njson file created.")