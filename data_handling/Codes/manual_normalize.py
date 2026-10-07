import pandas as pd 
df = pd.DataFrame({
"age": [20,30,40,50],
"salary": [20000,40000,60000,80000],
})
df["age_normalized"] = (
    (df["age"] -df["age"].min())
    / (df["age"].max() - df["age"].min())
)
df["salary_normalized"] = (
    (df["salary"] - df["salary"].min())
    / (df["salary"].max()-df["salary"].min())
)
print(df)