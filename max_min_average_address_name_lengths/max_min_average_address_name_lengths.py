from data.data import df
import numpy as np

max_address_length = df['Street Address'].str.len().max()
min_address_length = df['Street Address'].str.len().min()

address_length_sum = df['Street Address'].str.len().sum()
address_series_length = df['Street Address'].size
average_address_length = int(np.ceil(address_length_sum / address_series_length))

print(f'The longest address name string is: {max_address_length} long')
print(f'The shortest address name string is: {min_address_length} long')
print(f'The average address name length is: {average_address_length} long')