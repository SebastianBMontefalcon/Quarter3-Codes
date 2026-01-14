import numpy as np

names = ["Me", "Lia", "Jake"]
steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

total_per_day = steps.sum(axis=0)

print("Total steps per day:")
for i in range(len(days)):
    print(days[i] + ":", total_per_day[i])

most_active_index = total_per_day.argmax()
print("Most active day overall:", days[most_active_index])

