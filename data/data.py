import pandas as pd

df = pd.read_csv('../addresses.csv')

df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

df.columns = ['First Name', 'Last name', 'Street Address', 'City', 'State', 'Postal Code']

missing_values = df.isna().any().any()

if missing_values:
    df.fillna('None', inplace=True)