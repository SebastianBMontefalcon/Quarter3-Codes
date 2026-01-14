import numpy as np

steps = np.array([
    [5000, 5200, 4800, 5500, 5100],
    [4000, 4200, 4100, 4600, 4100],
    [6000, 5800, 6200, 6000, 6000]
])

for i, friend_steps in enumerate(steps, start=1):
    total = np.sum(friend_steps)
    average = np.mean(friend_steps)
    min_steps = np.min(friend_steps)
    max_steps = np.max(friend_steps)
    print(f"Friend {i} - Total Steps: {total} | Average: {average:.1f} | Min: {min_steps} | Max: {max_steps}")

overall_min = np.min(steps)
overall_max = np.max(steps)
print(f"\nOverall Min Steps: {overall_min}")
print(f"Overall Max Steps: {overall_max}")

