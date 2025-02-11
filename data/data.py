import pandas as pd

df = pd.read_csv('../addresses.csv')
df.columns = ['First Name', 'Last name', 'Street Address', 'City', 'State', 'Postal Code']

missing_values = df.isna().any().any()

if missing_values:
    df.fillna('None', inplace=True)