# Loop Assignment Question
#  1. Print the numbers from 1 to 10 using a for loop.
"""for i in range(1,11):
    print(i)"""

#  2. Print the even numbers from 1 to 20 using a while loop.
"""n = 20
for i in range(1,n+1):
    if(i % 2 == 0):
        print(i)"""

#  3. Calculate and print the sum of numbers from 1 to 100 using a for loop.
"""n = 100
sum = 0
for i in range(1,n+1):
    sum +=i
print(sum)"""

#  4. Print a multiplication table for a given number using a for loop.
"""n = int(input("Enter no. = "))
for i in range(1 , 11):
    t = i * n
    print(t)"""

#  5. Print the Fibonacci series up to a given number using a while loop.
"""n = int(input("enter the no = "))
a = 0
b = 1
i = 0
while(i < n):
    print(a)
    a = b
    b = a + b
    i = i+1"""

#  6. Print the reverse of a given string using a for loop.
"""str = input("Enter the string = ")
temp = len(str)
for i in range(temp-1, -1, -1):
    print(str[i], end = "")"""
    

#  7. Calculate and print the factorial of a given number using a while loop.
"""n = int(input("Enter the no = "))
fact = 1
i = 1
while(i < n+1):
    fact = fact * i
    i = i+1
print(fact)"""


#  8. Print the ASCII value of each character in a given string using a for loop.
"""str = input("Enter the string =")
for i in str:
    print("ASCII value ",i,"is", ord(i))"""

#  9. Calculate and print the average of a list of numbers using a for loop.
"""list = [3,5,6,7,8,3,5]
sum = 0
for i in list:
    sum = sum + i
avg =  sum / len(list)
print("sum = ",sum)
print("avg =", avg)"""


#  10. Check if a given number is prime using a while loop.
"""num = int(input("Enter the number ="))
i = 1
count = 0
while(i <= num):
    if num % i == 0:
        count = count + 1
    i = i+1   
if(count == 2):
    print(num, "prime no")
else:
    print(num, "not prime no")"""

    
#  11. Print the first 10 terms of the geometric sequence with a common ratio of 2 using a for loop.

#  12. Generate and print a random number between 1 and 10 using a while loop.
"""import random 
i = 1
while(i <= 5):
    num =  random.randint(1 ,11)
    print(num)
    i = i+1"""

#  13. Print the square of each number from 1 to 10 using a for loop.
"""for i in range(1,11):
    sq = i ** 2
    print(i , "square", sq)""" 

#  14. Count and print the number of vowels in a given string using a for loop.
"""str = input("Enter the string =")
count = 0
for ch in str:
    if ((ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u") or 
        (ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U") ):
        count +=1
print("No. of vowel=",count)"""


#  15. Print the factors of a given number using a while loop.
"""n = int(input("Enter the number ="))
i = 1
while( i <= n+1):
    if(n % i == 0):
        print(i)
    i = i + 1"""

#  16. Calculate and print the sum of the digits of a given number using a for loop.
"""n = int(input("Enter the digit ="))
sum = 0
for i in range(1,n+1):
    r = n % 10
    sum = sum + r
    n = n // 10
print("sum = ",sum)"""


#  17. Print a pattern of numbers from 1 to 5 using nested loops.
"""for i in range(1,6):
    for j in range(1,6):
        print(j, end =" ")
    print()"""

#  18. Print the uppercase letters of the alphabet using a for loop.
"""for i in range(65,91):
    print( chr(i), end = " ")"""

    
#  19. Print the lowercase letters of the alphabet in reverse order using a while loop.
"""i = 122
while(i >= 97):
    print(chr(i), end = " ")
    i -= 1"""

#  20. Print the calendar of a given month using nested loops.
"""import calendar
month = 11
year = 2025
for i in range(1,2):
    for j in range(1, i+1):
        print(calendar.month(year,month))"""


#  21. Generate and print the first 10 prime numbers using a for loop.
"""n = 29
for i in range(1,n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count = count + 1
        
    if(count == 2):
        print(i)"""

#  22. Print the elements of a list in reverse order using a while loop.
"""list1 = [3, 4, 5, 6, 8, 2]
i = len(list1) - 1  

while i >= 0:
    print(list1[i],end = " ")
    i = i - 1"""

# 23. Calculate and print the power of a given number using a for loop.
"""base = int(input("Enter the base number = "))
exponent = int(input("Enter the exponent = "))
result = 1
for i in range(exponent):
    result = result * base 
print(f"{base} raised to the power {exponent} is: {result}")"""

#  24. Check if a given string is a palindrome using a while loop.
"""str = input("Enter the string = ")
i = len(str)-1
rev = ""
while(i >= 0):
    rev = rev + str[i]
    i = i-1

if( str == rev):
    print("palindrome")
else:
    print("Not palindrom")"""


#  25. Print a pattern of asterisks in the shape of a pyramid using nested loops.
"""n = int(input("Enter the number ="))
for i in range(1,n+1):
    print(" " * (n - i),end = "")
    for j in range(1,i+1):
        print("*",end =" ")
    print()"""


#  26. Find and print the maximum element in a list using a for loop.
"""list1 = [34, 56, 78, 34, 8, 9, 45, 34]
max_elem = list1[0]
for i in list1:
    if i > max_elem:
        max_elem = i  
print(max_elem)"""

#  27. Calculate and print the factorial of each number from 1 to 10 using a for loop.
"""for i in range(1,11):
    fact = 1
    for j in range(1, i+1):
        fact = fact * j 
    print(i," facorial ",fact)"""

#  28. Check if a given number is Armstrong using a while loop.
"""original = int(input("Enter the digit ="))
n = len(str(original))
num = original
r = 0
while(num > 0):
    arm= num % 10
    r = r + arm ** n
    num = num // 10
if(original == r):
   print("Armstong no")
else:
    print("Not Armstonge no")"""


#  29. Print the prime factors of a given number using a for loop.
"""n = int(input("Enter the number ="))
for i in range(1,n+1):
    if(n % i == 0):
        print(i)"""

#  30. Calculate and print the sum of all even numbers between 1 and 50 using a while loop.
"""i = 0
sum = 0
while(i <= 50):
    if(i % 2 == 0):
        sum = sum +i
    i = i+1          
print(sum)
"""

#  31. Print the multiplication table of each number from 1 to 5 using nested loops.
"""for i in range(1,6):
    for j in range(1,11):
        t= i * j
        print(t, end = "  ")
    print()"""

#  32. Print the number of characters in each word of a given sentence using nested loops.

#  33. Check if a given string is a pangram using a for loop.

#  34. Print the common elements between two lists using a for loop.
"""list = [3,4,6,7,2,1]
list2 = [3,6,8,4,9,]
duplicate = []
for i in list:
    for j in list2:
        if(i == j):
            duplicate.append(j)
print(duplicate)"""

#  35. Calculate and print the sum of the digits of each number from 1 to 10 using a for loop.
"""for i in range(1,11):
    sum = 0 
    for j in range(1, i+1):
        sum = sum + j
    print(i,"sum ",sum)"""

#  36. Print the odd numbers in reverse order from 20 to 1 using a while loop.
""" i = 20
while(i >= 0):
    if(i % 2 == 1):
        print(i)
    i = i-1"""

#  37. Check if a given number is a perfect number using a for loop.
"""n = int(input("Enter the number ="))
sum = 0
for i in range(1,n+1):
    if(n % i == 0):
        sum = sum + i
if(sum == n):
    print("This is a perfect number")
else:
    print("This is not a perfect number")"""        


#  38. Generate and print a multiplication table for numbers 1 to 10 using nested loops.
"""n = int(input('Enter the no. = '))
for i in range(1, 11):
    for j in range(1, i+1):
        t = i * n
    print(t)"""

#  39. Print the uppercase and lowercase letters of the alphabet alternately using nested loops.
"""for i in range(26):
    for j in range(1):
        upper = chr(ord("A")+i)
        lower = chr(ord("a")+i)
        print(upper,lower  , end = " ")"""

#  40. Calculate and print the GCD (Greatest Common Divisor) of two numbers using a while loop.
"""a = int(input("Enter the number a ="))
b = int(input("Enter the number b ="))
while(b != 0):
    a ,b = b ,a % b
print(a)"""


#  41. Print a pattern of alphabets from A to E using nested loops.
"""for i in range(65,70):
    for j in range(65 , i+1):
        print(chr(j), end = " ")
    print()"""

#  42. Find and print the minimum element in a list using a for loop.
"""list = [34,56,34,56,12,11]
for i in list:
    el = min(list)
print(el)"""


#  43. Calculate and print the sum of all odd numbers between 1 and 50 using a for loop.
"""n = 50
sum = 0
for i in range(1,n+1):
    if(i % 2 == 1):
       sum = sum + i
print(sum)""" 

#  44. Check if a given string is a palindrome ignoring spaces and case sensitivity using a while loop.


#  45. Print the numbers from 1 to 10 in reverse order using a for loop.
"""for i in range(10, 0 ,-1):
    print(i)
"""

# 46. Calculate and print the LCM (Least Common Multiple) of two numbers using a while loop.
"""a = int(input("Enter the value of a ="))
b = int(input("Enter the value of b ="))
if a > b:
    greater = a
else:
    greater = b

while True:
    if((greater % a == 0) and (greater % b == 0)):
        print(greater)
        break
    greater += 1"""


#  47. Print the prime numbers between 1 and 100 using a for loop.
"""n = 100
for i in range(1,n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count = count + 1
        
    if(count == 2):
        print(i)"""

#  48. Check if a given number is a perfect square using a while loop.
"""n = int(input("Enter the number ="))
i = 0
while(i <= n):
    m = n ** (1/2)
    sq = m**2
    i = i+1
if(n == sq):
    print("perfect square")
else:
    print("Not perfect square")""" 

#  49. Print the elements of a nested list using nested loops.
"""list = [[3,4,5,3],[3,4,5,7,5],[2,3,5]]
for i in list:
    for j in i:
        print(j, end = " ")"""


#  50. Calculate and print the sum of all digits in a given sentence using a for loop.
"""sentence = "My phone number is 9876 and pin is 451"
sum = 0
for ch in sentence:
    if ch.isdigit():
        sum = sum + int(ch)
print(sum)""" 