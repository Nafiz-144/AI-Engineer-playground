
"""
1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
2. Write a program to fill in a letter template given below with name and date.
   ```python
   letter = '''
       Dear <|Name|>,
       You are selected!
       <|Date|>
   '''
   ```
3. Write a program to detect double space in a string.
4. Replace the double space from problem 3 with single spaces.
5. Write a program to format the following letter using escape sequence characters.
   `Letter = "Dear Nafiz, this python course was helpful. Thanks!"`"""

# problem-1
a=str(input("Enter the name:"))
print(f"Good Morning,{a}")

# Problem-2
b=str(input("Enter the name:"))
c=str(input("Enter the Date:"))
print("Dear <|",b,"|>, \n You are Selected! \n <|",c,"|>")
'''
letter=
Dear <|Name|>,
You are selected!
 <|Date|>
print(letter.replace("<|Name|>","Nafiz").replace(" <|Date|>","12 september 2027"))

'''
# Problem-3
d=input("Enter the String:")
print("Double Space found!","  " in d)
# problem-4
print("Replace \" Double Space \"to \"Single Space : \"",d.replace("  "," ") )
# problem-5
print("`Letter = \"Dear Nafiz, \n\tthis python course was helpful.\n Thanks!\"`")