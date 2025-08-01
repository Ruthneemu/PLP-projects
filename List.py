# 1. Create an empty list called my_list.
my_list = []

print(f"Initial empty list: {my_list}")

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"After appending 10, 20, 30, 40: {my_list}")

# 3. Insert the value 15 at the second position in the list.
# (Index 1, as lists are 0-indexed)
my_list.insert(1, 15)

print(f"After inserting 15 at second position: {my_list}")

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

print(f"After extending with [50, 60, 70]: {my_list}")

# 5. Remove the last element from my_list.
my_list.pop() # pop() without an argument removes the last item

print(f"After removing the last element: {my_list}")

# 6. Sort my_list in ascending order.
my_list.sort() # Sorts the list in-place

print(f"After sorting in ascending order: {my_list}")

# 7. Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)

print(f"The index of value 30 is: {index_of_30}")