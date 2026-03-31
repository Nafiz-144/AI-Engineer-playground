name = "Nafiz"

# 1. len() returns the total number of characters (5)
print("Length of name:", len(name))

# 2. Slicing from index 0 to 5 (0, 1, 2, 3, 4)
# Since the string only has 5 characters, this prints the whole name
print("Full slice [0:5]:", name[0:5])

# 3. Negative slicing: -3 is 'f', -1 is 'z'
# It starts at 'f' and stops BEFORE 'z'
print("Negative slice [-3:-1]:", name[-3:-1])

# 4. Slicing from index 1 ('a') to 3 ('i')
# It stops BEFORE index 3
print("Middle slice [1:3]:", name[1:3])

# 5. Leaving the start empty [:4] defaults to the beginning (index 0)
print("Start to index 4:", name[:4])

# 6. Leaving the end empty [3:] defaults to the very end of the string
print("Index 3 to end:", name[3:])