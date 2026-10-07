import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 30000, 40000, 50000, 60000]
})

scaler = StandardScaler()

df[["age", "salary"]] = scaler.fit_transform(
    df[["age", "salary"]]
)

print(df)
