# Pandas - Fixing Wrong Data
# Replacing Values
import pandas as pd 
df = pd.read_csv('data.csv')
print(df.to_string())

print()
#df.loc[18, 'Transaction Date'] = '\'04/01/2021\''
#print(df.to_string())
#print()

for x in df.index:
    if df.loc[x, 'Value'] > df["Value"].mean():
        df.loc[x, 'Value'] = df["Value"].mean()
print(df.to_string())
print()
