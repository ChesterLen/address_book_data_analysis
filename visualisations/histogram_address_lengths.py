import matplotlib.pyplot as plt

from data.data import df

df = df.dropna(subset=['Street Address'])

address_lengths = df['Street Address'].str.len()

plt.figure(figsize=(10, 5))
plt.hist(address_lengths, bins=10, color='skyblue', edgecolor='black')

plt.xlabel("Address Length (Characters)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram of Address Lengths", fontsize=14)

plt.show()
