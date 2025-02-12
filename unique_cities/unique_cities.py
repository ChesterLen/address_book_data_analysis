from data.data import df

unique_cities = df['City'].unique()
num_unique_cities = len(unique_cities)

unique_states = df['State'].unique()
num_unique_states = len(unique_states)

print(f"Number of unique cities: {num_unique_cities}")
print(f"Number of unique states: {num_unique_states}")
print("Unique cities:", ', '.join(map(str, unique_cities)))
print("Unique states:", ', '.join(map(str, unique_states)))
