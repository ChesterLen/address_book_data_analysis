from data.data import df
from math import ceil

max_len_address = max([len(address) for address in df['Street Address']])
min_len_address = min([len(address) for address in df['Street Address']])

addresses_lengths = [len(address) for address in df['Street Address']]
average_address_length = ceil(sum(addresses_lengths) / len(addresses_lengths))

print(f'The longest Street Address name is long: {max_len_address}')
print(f'The shortest Street Address name is long: {min_len_address}')
print(f'The average address name length is: {average_address_length}')