#  1. Write a function to calculate the factorial of a number.
"""def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
factorial(5)"""


#  2. Create a function to check if a number is prime.
"""def prime(n):
    if(n % 2 == 0):
        print("prime no.")
    else:
        print("Not prime no.")
n = int(input("Enter the number ="))
prime(n)"""


#  3. Implement a function that reverses a string.
"""def str_reverse(str):
   l = len(str)
   for i in range(l-1,-1,-1):
      print(str[i],end = "")
str = input("Enter the string = ")
str_reverse(str)"""

#  4. Write a function to calculate the sum of digits in a number.
"""def sum_digit(num):
    sum = 0
    while num > 0:
        r = num % 10
        sum = sum + r
        num = num // 10
    return sum
num = int(input("Enter the num = "))
res = sum_digit(num)
print(res)"""

#  5. Create a function to find the greatest common divisor (GCD) of two numbers.
"""def gcd_fun(a,b):
    while(b != 0):
        a ,b = b ,a % b
    return a
a = int(input("Enter the number a ="))
b = int(input("Enter the number b ="))
result = gcd_fun(a,b)
print(result)"""

#  6. Implement a function that counts the occurrences of a character in a string.
"""def func(str,char_count):
    count = 0
    for i in str:
        if i == char_count:
            count = count + 1
    return count
str = input("Enter the string = ")
char_count = input("Enter the character count = ")
result = func(str,char_count)
print(result)"""

#  7. Write a function to check if a string is a palindrome.
"""def palindrome(str):
    l = len(str)-1
    rev = ""
    for i in range(l, -1, -1):
        rev = rev + str[i]
    if(str == rev):
        print("palindrome")
    else:
        print("Not palindrome")
str = input('Enter the String = ')
palindrome(str)"""    

#  8. Create a function that generates a list of Fibonacci numbers.
"""def fabonacci(n):
    fib_list = []
    a ,b = 0 ,1 
    for i in range(n):
        fib_list.append(a)
        a , b = b , a + b
    return fib_list
n = int(input('Enter the number = '))
result = fabonacci(n)
print(result)"""

#  9. Implement a function to calculate the area of a circle.
"""import math
def area(radius):
    return math.pi * radius ** 2
radius = float(input('Enter the radius of circle = '))
result = area(radius)
print(result)"""


#  10.Write a function that sorts a list of numbers using the bubble sort algorithm.
"""def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - 1 -i):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
    return arr 
arr = [5,3,4,1] 
print("Original array = ",arr)
result = bubble_sort(arr)
print('Sorted array = ',result)"""

#  11. Create a function to convert Celsius to Fahrenheit.
"""def celsius_func(n):
    fahrenheit = (n * 9/5)+ 32
    return fahrenheit

n = float(input('Enter the celsius = '))
temprature = celsius_func(n)
print(temprature)"""  

#  12.Implement a function that finds the median of a list of numbers.
"""import statistics
def median_ele(n):
    median = statistics.median(n)
    print(median)
n = [2,3,4,5,6,7,8,9]
median_ele(n)"""


#  13. Write a function to find the least common multiple (LCM) of two numbers.
"""import math
def lcm(a,b):
    return abs(a * b) // math.gcd(a,b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
res = lcm(a,b)
print(res)"""

#  14.Create a function that checks if two strings are anagrams.
"""def Anagram(s1, s2):
    str1 = s1.replace(" ","").lower()
    str2 = s2.replace(" ","").lower()

    return sorted(str1) == sorted(str2)

s1 = input('Enter the 1st string = ')
s2 = input('Enter the 2nd string = ')
if Anagram(s1, s2):
    print("This is a Anagram")
else:
    print('This is not Anagram')"""

#  15.Implement a function to calculate the perimeter of a rectangle. 
"""def rectangle(length , width):
    return 2  * (length + width)

l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))
result = rectangle(l,w)
print(result)"""


#  16.Write a function to check if a year is a leap year.
"""def year(n):
    if(n % 4 == 0):
        print("leap year")
    else:
        print("not leap year")
n = int(input('Enter te number =' ))
year(n)"""

#  17.Create a function that calculates the power of a number using recursion.
"""def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base , exponent -1)

base = int(input('Enter the base = '))
exponent = int(input('Enter the exponent ='))
result = power(base , exponent)
print(result)"""


#  18.Implement a function to find the maximum element in a list.
"""def max_ele(list1):
    res = max(list1)
    print(res)
list1 = [2,3,5,67,9,6,4,34,90]
max_ele(list1)"""


#  19.Write a function to calculate the area of a triangle given its sides.
"""import math
def tringle(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a+b>c and b+c>a and a+c>b :
    result = tringle(a,b,c)
    print(result)"""


#  20.Create a function that converts a decimal number to binary.
"""def decimal_func(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    while(decimal > 0):
        r = decimal % 2
        binary = str(r) + binary
        decimal = decimal // 2
    return binary
decimal = int(input('Enter the decimal = '))
result = decimal_func(decimal)
print('binary number = ',result)"""



#  21.Implement a function to reverse a list.
"""def reverse_fun(list1):
    list1.reverse()
    print(list1)
list1 = [1,2,3,4,5,6]
reverse_fun(list1)"""


#  22.Write a function that generates a random password.
"""import random
import string

def random_func(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    all_chars = letters + digits + special_chars

    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

length = int(input("Enter the length of password = "))
result = random_func(length)
print("Generated Password:", result)"""


#  23.Create a function to find the average of a list of numbers.
"""def avrage(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    avg = sum / len(list1) 
    print(avg)
list1 = [2,3,4,5,6]
avrage(list1)"""

#  24.Implement a function that checks if a number is even or odd.
"""def func(num):
    if (num % 2 == 0):
        print('Even number')
    else:
        print("Odd number")
num = int(input('Enter the number = '))
func(num)"""

#  25.Write a function to calculate the factorial of a number using recursion.
"""def fact(n):
    if(n == 0):
        return 1
    else:
        return n * fact(n-1)
n = int(input('Enter the number = '))
res = fact(n)
print(res)"""

#  26.Create a function to check if a string is a valid email address.
"""import re
def valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False
    
email = input("Email  Address = ")
if valid_email(email):
    print('Valid Email')
else:
    print('Invalid email')"""


#  27.Implement a function that merges two sorted lists into a single sorted  list
"""def sort_list(list1, list2):
    merge = list1 + list2
    merge.sort()
    return merge
list1 = [2,4,3]
list2 = [5,7,1]
res = sort_list(list1,list2)
print(res)"""


#  28.Write a function to find the square root of a number using the Newton-Raphson method.

#  29.Create a function to remove duplicates from a list.
"""def duplicate(list1):
    temp = []
    for i in list1:
        if i not in temp:
            temp.append(i)
    return temp
list1 = [2,3,4,5,3,2]
res = duplicate(list1)
print(res)"""

#  30.Implement a function that finds the mode of a list of numbers. 

#  31.Write a function to calculate the area of a trapezoid.
"""def trapezoid_func(a,b,h):
    area = 0.5 * (a + b) * h
    return area
a = int(input('Enter the first side = '))
b = int(input('Enter the second side = '))
h = int(input('Enter the height = '))
res = trapezoid_func(a,b,h)
print(res)"""

#  32.Create a function that converts a binary number to decimal.
"""def binary_to_decimal(binary):
    decimal = 0
    length = len(binary)
    for i in range(length):
        bit = int(binary[i])
        power = length - i -1 
        decimal = decimal + bit * (2 ** power)
    return decimal
binary = input('Enter the binary number = ')
result = binary_to_decimal(binary)
print('Decimal No. = ',result)"""


#  33.Implement a function to check if a string is a pangram (contains all letters of the alphabet)
"""def is_pangram(str1):
    sentence = str1.lower()
    alpha_set = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence)
    return alpha_set.issubset(sentence)
str1 = input('Enter the sentence = ')
if is_pangram(str1):
    print('It is a pangram')
else:
    print('not pangram')""" 


#  34.Write a function to rotate elements in a list to the right by a given number of positions.
"""def rotate(list1 ,n):
    res = list1[-n:] + list1[:-n]
    return res 
list1 = [10,20,30,40,50]
n = int(input('Enter the number ='))
result = rotate(list1, n)
print(result)"""

#  35.Create a function that calculates the n-th term of the Fibonacci sequence using memoization.
def fibo(n, mamo={}):
    if n in mamo: 
        return mamo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    mamo[n] = fibo(n - 1, mamo) + fibo(n - 2, mamo)
    return mamo[n]
n = int(input('Enter the number = '))
res = fibo(n)
print(res)


#  36.Implement a function to find the second largest element in a list.
"""def second_largest(list1):
    list1.remove(max(list1))
    res = max(list1)
    return res
list1 = [2,3,4,6,8,9]
result = second_largest(list1)
print('Second Largest element = ',result)"""


#  38.Write a function to calculate the area of a circle sector.
"""import math 
def circle_sector(radius , angle):
    area = (angle / 360) * math.pi * radius ** 2
    return area
radius  = float(input('Enter the radius = '))
angle = float(input('Enter the angle = '))
result = circle_sector(radius , angle)
print(result)"""

#  39.Create a function that counts the number of words in a sentence.
"""def word(str1):
    list1 = str1.split()
    length = len(list1)
    return length
str1 = input('Enter the sentence = ')
result = word(str1)
print(result)"""


#  40.Implement a function to perform linear search in a list.
"""def linear_search(arr , target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i  
    return -1
        
arr = [20,40,30,50,10,60]
target = int(input('enter the number of search = '))
result = linear_search(arr, target)

if result != -1:
    print(target ," found at index ",result)
else:
    print(target ,"not found element")"""


#  41.Write a function to convert a string to title case (capitalize first letter of each word).
"""def title_case(str1):
    res = str1.title()
    return res
str1 = input('Enter the string = ')
result = title_case(str1)
print(result)"""

#  41.Create a function that calculates the sum of a series: 1 + 1/2 + 1/3 + ...+ 1/n.
"""def series(n):
    total = 0
    for i in range(1,n+1):
        total = total + 1 / i
    return total 
n = int(input('Enter the number = '))
print(series(n))"""

#  42.Implement a function to check if a number is a perfect square.
"""def perfect_square(num):
    res = num ** 0.5
    return res.is_integer()

num = int(input('Enter the number = '))
if perfect_square(num): 
    print('This is a perfect square')
else:
    print('This is not a perfect square')"""

#  43.Write a function to calculate the distance between two points in 2D space.
"""import math
def point(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx **2 + dy ** 2)
    return distance
x1 = float(input('Enter x1 value = '))
x2 = float(input('Enter x2 value = '))
y1 = float(input('Enter y1 value = '))
y2 = float(input('Enter y2 value = '))
res = point(x1,y1,x2,y2)
print(res)"""

#  44.Create a function that finds the largest prime factor of a number.
"""def prime(n):
    fact = 2
    while fact <= n:
        if n % fact == 0:
            n = n // fact
        else:
            fact = fact + 1
    return fact
n = int(input('Enter the number =  '))
res = prime(n)
print(res)"""
 

#  45.Implement a function to calculate the volume of a sphere.
"""import math 
def volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
radius = float(input('Enter the radius value ='))
print(volume(radius))"""

#  46.Write a function to perform binary search in a sorted list.
"""def binary_search(list , target):
    low = 0
    high = len(list)-1
    while low <= high:  
        mid = (low + high) // 2  
        if list[mid] == target:  
            return mid  
        elif list[mid] < target: 
            low = mid + 1  
        else:  
            high = mid - 1
    return -1

list = [12,23,34,45,56,67,98]
target = int(input('Enter the target = '))
res = binary_search(list,target)

if res != -1:
    print(target,"found at index",res)
else:
    print("Element not found ")"""


#  47.Create a function that calculates the mean, median, and mode of a list of numbers.
"""import statistics
def calculate(num):
    mean = statistics.mean(num)
    median = statistics.median(num)
    mode = statistics.mode(num)
    return mean , median , mode
num = [3,4,6,5,7,8,9,4,1]
mean ,median, mode = calculate(num)
print('Mean = ',mean)
print('Median =',median)
print('Mode =',mode)"""

#  48.Implement a function to check if a string is a palindrome using recursion.
"""def palindrome(str1):
    if len(str1) <= 1:
        return True
    if str1[0] != str1 [-1]:
        return False
    return palindrome(str1[1:-1])
str1 = input('Enter the string = ')
print(palindrome(str1))"""


#  49.Write a function to calculate the factorial of a large number using the iterative method.
"""def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
n = int(input('Enter the number = '))
res = factorial(n)
print(res)"""

#  50.Create a function that generates a list of prime numbers using the Sieve of Eratosthenes algorithm.
