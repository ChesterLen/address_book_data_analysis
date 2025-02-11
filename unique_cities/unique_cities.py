from data.data import df

unique_cities = df['City'].unique()

print('The unique cities are:', ', '.join(map(str, unique_cities)), end='')
