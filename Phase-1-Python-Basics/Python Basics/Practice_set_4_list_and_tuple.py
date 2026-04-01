#list and tuple
'''
1. Write a program to store seven fruits in a list entered by the user.
2. Write a program to accept marks of 6 students and display them in a sorted manner.
3. Check that a tuple cannot be changed in python.
4. Write a program to sum a list with 4 numbers.
5. Write a program to count the number of zeros in the following tuple:  `a = (7, 0, 8, 0, 0, 9)`'''
# Problem-1
fruit=[]
for i in range(7):
    f1=input("Enter the Fruit:")
    fruit.append(f1)
print(fruit)

# problem-2
student=[]
for i in range(6):
    s=int(input(f"Enter the Student {i+1} Marks:"))
    student.append(s)
print(sorted(student))

# problem-3
tuple=("sadman","islam","nafiz")
print(type(tuple))
tuple.insert(0,"can't")
# Problem-4
#tuple=(1,2,3)
list=(1,2,3)
print(sum(list))
# problem-5
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
