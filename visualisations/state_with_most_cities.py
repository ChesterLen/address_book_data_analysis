from data.data import df
import matplotlib.pyplot as plt

state_counts = df['State'].value_counts()

top_5_states = state_counts.head(5)

plt.figure(figsize=(10, 5))
top_5_states.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Top 5 Most Frequent States by Address Count", fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Number of Addresses', fontsize=12)
plt.xticks(rotation=45)

plt.show()
