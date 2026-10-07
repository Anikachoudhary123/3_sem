import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    "age": [20, 30, 40, 50],
    "salary": [20000, 40000, 60000, 80000]
})

scaler = MinMaxScaler()

df[["age", "salary"]] = scaler.fit_transform(
    df[["age", "salary"]]
)

print(df)
