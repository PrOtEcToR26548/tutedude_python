#

# Task 2: Demonstrate List Slicing

# Step 1: create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: extract the first five elements
first_five = numbers[:5]

# Step 3: reverse these extracted elements
reversed_list = first_five[::-1]

# Step 4: print results
print("Original list:", numbers)
print("First five extracted:", first_five)
print("Reversed extracted:", reversed_list)
