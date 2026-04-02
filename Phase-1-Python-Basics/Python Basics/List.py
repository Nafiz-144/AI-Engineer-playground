list = ["Apple", "Banana", "Cherry", "Mango", "Pinaaple"]
print(list)
# negative index
print(list[-1])
# range of index
print(list[2:4]) #The search will start at index 2 (included) and end at index 5 (not included).
print(list[2:])
print(list[:4])
# item check in list
if 'Goat' in list:
    print("YES!")
else:
    print("NO")
list[1]="Jackefruit"
print(list)
# Change a Rnage Of Item Value
list[1:3]=["Blackcurrant", "Watermelon"]
print(list)
# intsert item and add item at the specified index
list.insert(2,"Cat")
print(list)
list.insert(0, 'Coconut')
print("Add item defore index 0:",list[1])
#add item
list.append("Guava")
#List EXtend
tropical = ["Crow", "Cow", "Dog"]
list.extend(tropical)
print(list)
#Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)
# Remove Specified Index
list.pop(1)
print(list)
# Remove the first item
del(list(0))
print(list)
# Loop Through the Index Numbers (For loop)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#while loop
list=["Sadman","Islam","Nafiz"]
i=0
while i<len(list):
   print(list[i])
   i=i+1

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
  if "ap" in i:
    newlist.append(i)

print(newlist)
newlist=[x for x in fruits if "a" in x]#newlist = [expression for item in iterable if condition == True]
print(newlist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)