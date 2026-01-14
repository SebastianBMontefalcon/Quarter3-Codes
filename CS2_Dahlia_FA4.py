import numpy as np

names = ["Me", "Lia", "Jake"]
steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  
    [4000, 4100, 3900, 4200, 4600],  
    [6000, 5800, 5900, 6100, 6200]   
])

total_steps = steps.sum(axis=1)

print("Total steps for each person:")
for i in range(len(names)):
    print(names[i] + ":", total_steps[i])

max_index = total_steps.argmax()
print("Person with highest steps:", names[max_index], "with", total_steps[max_index], "steps")

difference = total_steps.max() - total_steps.min()
print("Difference between highest and lowest total:", difference)

