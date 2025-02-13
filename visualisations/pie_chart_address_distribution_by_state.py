import matplotlib.pyplot as plt
from data.data import df

state_counts = df['State'].value_counts()

filtered_states = state_counts[state_counts > 1]

plt.figure(figsize=(8, 8))
plt.pie(filtered_states, labels=filtered_states.index, autopct='%1.1f%%', startangle=140)

plt.title("Address Distribution by State", fontsize=14)

plt.show()
