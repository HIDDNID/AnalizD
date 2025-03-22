import pandas as pd

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

print(df.head())

print(df.info())
print(df.describe())