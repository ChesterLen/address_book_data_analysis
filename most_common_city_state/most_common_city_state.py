from data.data import df

duplicated_cities_counts = df['City'].value_counts()

duplicated_cities = duplicated_cities_counts[duplicated_cities_counts > 1]

if duplicated_cities.sum():
    print(f'Most frequently appearing cities are:')

    for key, value in duplicated_cities.items():
        print(f'City: {key}: repeat {value} times')

duplicated_states_count = df['State'].value_counts()

duplicated_states = duplicated_states_count[duplicated_states_count > 1]

if duplicated_states.sum():
    print(f'Most frequently appearing states are:')

    for key, value in duplicated_cities.items():
        print(f'State: {key}: repeat {value} times')