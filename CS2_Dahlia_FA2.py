import numpy as np 

steps = np.array([
    [4500, 5200, 4800, 5000, 5300], 
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

print("Jake's steps on monday:", steps[2, 2])  

my_steps = steps[0]
print("My steps...", my_steps)

print("Updating my steps on Thurstday to 5500.")

steps[0, 3] = 5500
print("My updated steps:", steps[0])