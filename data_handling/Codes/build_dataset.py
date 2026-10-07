import pandas as pd 
data ={
    "customer_id": [1,2,3,4,5,5],
    "name": ["rahul","priya","amit","ravi","ravi","aaru"],
    "age": [25,28,None,32,29,29],
    "salary": [40000,55000,45000,None,60000,60000],
    "city": ["delhi","mumbai","bangalore","delhi","mumbai","mumbai"],

}
df = pd.DataFrame(data)
print(df)