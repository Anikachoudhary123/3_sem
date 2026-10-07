import pandas as pd

df = pd.DataFrame({
    "salary": [20000, 30000, 40000, 50000, 60000]
})

mean = df["salary"].mean()
std = df["salary"].std()

df["salary_standardized"] = (
    (df["salary"] - mean) / std
)

print(df)
