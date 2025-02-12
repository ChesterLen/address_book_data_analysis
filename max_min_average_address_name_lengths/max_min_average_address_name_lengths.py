from data.data import df

df = df.dropna(subset=['Street Address'])

address_lengths = df['Street Address'].str.len()

max_address_length = address_lengths.max()
min_address_length = address_lengths.min()
average_address_length = round(address_lengths.mean())

print(f"The longest address is {max_address_length} characters long.")
print(f"The shortest address is {min_address_length} characters long.")
print(f"The average address length is {average_address_length} characters.")
