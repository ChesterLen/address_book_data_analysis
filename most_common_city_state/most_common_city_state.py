from data.data import df

city_counts = df['City'].value_counts()
most_common_cities = city_counts[city_counts > 1]

if not most_common_cities.empty:
    print("Most frequently appearing cities:")
    for city, count in most_common_cities.items():
        print(f"City: {city}, repeats {count} times")

state_counts = df['State'].value_counts()
most_common_states = state_counts[state_counts > 1]

if not most_common_states.empty:
    print("\nMost frequently appearing states:")
    for state, count in most_common_states.items():
        print(f"State: {state}, repeats {count} times")