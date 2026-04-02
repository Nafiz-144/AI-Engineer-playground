# Tuples are used to store multiple and duplicate items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data.
# The other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# asscess tuple item
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. 
# Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list,
#  change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)