#[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

num_list = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# Find the minimum value of each individual array
x = 0
for i in num_list:
    x += min(i)
print(x)

# Assign a varible and continue to add to the varible, return the variable 