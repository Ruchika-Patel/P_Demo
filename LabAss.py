"""num = int(input("Enter the number ="))
if(num % 2 == 0):
    print('Even Number')
else:
    print('Odd Number')"""

"""# Integer
num1 = 10
print("Integer:", num1, "Type:", type(num1))

# Float
num2 = 10.5
print("Float:", num2, "Type:", type(num2))

# String
name = "Ruchika"
print("String:", name, "Type:", type(name))

# Boolean
is_active = True
print("Boolean:", is_active, "Type:", type(is_active))

# List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, "Type:", type(fruits))

# Tuple
colors = ("red", "green", "blue")
print("Tuple:", colors, "Type:", type(colors))

# Set
unique_numbers = {1, 2, 3, 4}
print("Set:", unique_numbers, "Type:", type(unique_numbers))

# Dictionary
student = {"name": "Ruchika", "age": 21, "grade": "A"}
print("Dictionary:", student, "Type:", type(student))"""


"""import sys  # to access command line arguments

# Check if exactly 2 arguments are passed (excluding script name)
if len(sys.argv) != 3:
    print("Usage: python filename.py num1 num2")
else:
    # Convert arguments from string to integer and add
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    total = num1 + num2

    print("Sum:", total)"""


"""length = float(input("Enter the length of area = "))
width = float(input("Enter the width of area = "))
area = length * width
circumference = 2 * (length + width)
print("Area of the rectangle :",area)
print("circumference of the rentangle:",circumference)"""


"""age= int(input("Enter your age = "))
if(age >= 18):
    print("Eligible for voting")
else:
    print("Not Eligiblr for voting")"""


#Q1. Create variables with these literals and print each value and its type: 10, 3.5, 'Python', True, None.
"""integer_value = 10
flost_value =  3.5
string = "Python"
Boolean_value = True
Empty_value = None
print("integer_value = " ,type(integer_value))
print("flost_value  = " ,type(flost_value ))
print("string = " ,type(string))
print("Boolean_value = " ,type(Boolean_value))
print("Empty_value = " ,type(Empty_value))"""

#Q2. Convert the string '123' to int, and 45 to string. Print both values and types before and after conversion.
'''str_num = "123"
int_num = 45

print("Before Conversion")
print("str_num = ",str_num ,"Type = ", type(str_num))
print("int_num = ",int_num , "Type = ", type(int_num))

convert_Str = int(str_num)
convert_int = str(int_num)
print("After Conversion")
print("convert_Str = ",convert_Str ,"Type = ", type(convert_Str))
print("convert_int = ",convert_int , "Type = ", type(convert_int))'''

#. 3 Show integer division vs float division with 7/2 and 7//2. Print the results and their types.

"""float_div = 7/2
int_div = 7//2
print('Float Divition =',float_div, "type = ", type(float_div))
print("Integer Diviton = ",int_div ,"type = ",type(int_div))"""

# 4 . Create a multi-line string (triple quotes) with two lines of text. Print it and its length using len().
"""str = Hello
My name is Ruchika patel
Shree Govindram Seksaria Institute of Tecnology and Science
print("Multiple line String = \n",str , "\ntype =",type(str))
print("Length = ",len(str))"""

#Take a user input (as text), then print the original value and type; next convert to int using int() and print again.
"""int_num = input('Enter the number = ')
print("Original Value =",int_num ,'Type =', type(int_num))

convert_int = int(int_num)
print("After Convert = ",convert_int, "Type =",type(convert_int))"""

#Q6. For each value in this list: ['', 'text', 0, 1, [], [1], {}], print the value and bool(value).
"""value = ['', 'text', 0, 1, [], [1], {}]
for val in value:
    print("value = ",val, "  bool(Value) = ",bool(val))"""

#Q7. Compare True == 1 and False == 0. Print results and briefly explain in a comme nt.
"""print("True == 1 :", True == 1)
print("False == 0 :", False == 0)"""

# Explanation:
# In Python, True is treated as integer 1 and False as integer 0
# when compared or used in arithmetic operations.

# 8 Let s = 'Python'. Print s[0], s[-1], s[1:4], and s[::-1].
"""s = "Python"
print(s[0])
print(s[-1]) 
print(s[1:4]) 
print(s[::-1])"""

#9 Q9. Ask the user for first_name and last_name. Create full_name = first_name + ' ' + last_name and print it.
"""first_name = input("Enter the first name =")
last_name = input("Enter the last name =")
print("Full Name = ",first_name, "" ,last_name)"""

#Q10. Create a list nums = [2, 4, 6]. Append 8, change the first item to 1, and print the list and its length
"""nums = [2, 4, 6]
nums.append(8)
nums[0] = 1
print("List = ",nums)
print("Length = " ,len(nums))"""

#Q11. Create a tuple t = ('a', 'b', 'c'). Try to change t[0] to 'z' and observe the error. Then print t unchanged.
"""t = ('a', 'b', 'c')
try:
    t[0] = "z"
except TypeError as e:
    print("Error : ",e)
print("Tuple = ",t)"""

#Q12. From list a = [1, 2, 3] and list b = [4, 5], make c = a + b and print c. Also print c[1:4].
"""a = [1, 2, 3]
b = [4, 5]
c = a + b
print(c[1:4])"""

#Q13. Create a set from the list [1, 2, 2, 3, 3, 3]. Print the set to show duplicates removed.
"""list = [1, 2, 2, 3, 3, 3]
s = set(list)
print(s)"""

#Q14. Make two sets: a={1,2,3} and b={3,4}. Print a union b, a intersection b, and a difference b.
"""a={1,2,3}
b={3,4}
uni = a.union(b)
inter = a.intersection(b)
dif = a.difference(b)
print("Union = ",uni)
print("Intersection = ",inter)
print("Differnece = ",dif)"""

#Create a dict student = {'name':'Asha', 'age':20}. Print student['name'], then change age to 21 and print the dict.
"""student = {'name':'Asha', 'age':20}
print(student["name"])
student["age"] = 21
print(student)"""

#Q16. Start with empty dict d = {}. Add keys 'city'->'Indore', 'pin'->452001. Print keys, values, and items.
"""d = {}
d["city"]= "Indore"
d["pin"] = 452001
print("Dictionary = ",d)
print("Key = ",d.keys())
print("Value = ",d.values())
print("Item = ",d.items())"""

#Q17. For each value in [10, 3.5, 'hi', True, [1,2], (1,2), {1,2}, {'a':1}], print the value and type(value).
"""list1 = [10, 3.5, 'hi', True, [1,2], (1,2), {1,2}, {'a':1}]
for val in list1:
    print(val , " Type = " ,type(val))"""

#18 For the same list of values, check and print whether each is an instance of (int, float, str, bool, list, tuple, set, dict).
"""list1 = [10, 3.5, 'hi', True, [1,2], (1,2), {1,2}, {'a':1}]
for val in list1:
    print(val, "=", isinstance(val,(int, float, str, bool, list, tuple, set, dict)))"""

#Q19. Ask the user for input, then try to convert it to int using int(). If it fails, leave it as string. Print the final value and its type.
"""val = input("Enter the value = ") 
try:
    val = int(val)
except ValueError:
    pass
print("value = ",val)
print("Type = ",type(val))"""

#Q20. Define a simple class Box with attributes w and h set in __init__. Create a Box(5, 7) and print type(obj), obj.w, and obj.h.
"""class Box:
    def __init__(self, w,h):
        self.w = w
        self.h = h
obj = Box(5,7)

print("type = ",type(obj))
print("width = ",obj.w)
print("Height = ",obj.h)"""

#Q3 Given mixed literals (e.g., 42, 3.14, 2+5j, '42', b'42', bytearray(b'42')), print their values, types, and whether they are instances of numbers. Number where. appropriate.
"""import numbers
literals = [42, 3.14, 2+5j, '42', b'42', bytearray(b'42')]
for literal in literals:
    print("Value = ",literal)
    print("Types =",type(literal))
    print("Is Number =",(isinstance(literal, numbers.Number)))
    print("-" * 30) """

"""s = input("Enter the vowel =")
vowel = "aeiouAEIOU"
for i in s:
    if i in vowel:
        print(i, end = " ")"""
        
#Q.3 Write a program that takes 2 numbers as command    line arguments and prints its sum.
import sys

# Check if exactly 2 arguments are given (excluding script name)
if len(sys.argv) != 3:
    print("Usage: python sum.py <num1> <num2>")
    sys.exit(1)

# Convert arguments to integers
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Calculate sum
total = num1 + num2

print("Sum =", total)





