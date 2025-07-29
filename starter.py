import pandas as pd

df = pd.read_csv("files/net_users_num.csv")
print(df.head())

rows_with_nan = df[df.isnull().any(axis=1)]

print(rows_with_nan)