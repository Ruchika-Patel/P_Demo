
# 1. Check if a given number is positive.
"""num = int(input("Enter the Number ="))
if(num >= 0):
    print(num ," is positive Number")
else:
    print(num ," is Negative Number")"""

# 2. Check if a given number is even.
"""num = int(input("Enter the Number = "))
if(num % 2 == 0):
    print("Enen Number")
else:
    print("Odd Number")"""

# 3. Check if a given number is a multiple of 5.
"""num = int(input("Enter the Number ="))
if(num % 5 == 0):
    print("Divided By 5")
else:
    print("Not Divided By 5")"""

# 4. Check if a given string is empty.
"""strs = input("Enter the string =")
if(strs == ""):
    print("string is empty")
else:
    print("string is not empty")"""

# 5. Check if a given year is a leap year.
"""year = int(input("Enter the year ="))
if(year % 4 == 0):
    print(year ," is Leap year")
else:
    print(year ,"is not leap year")"""

# 6. Check if a given character is a vowel.
"""vowel = input("Enter the character =")
if(vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u" ):
    print("this is vowel")
else:
    print("this is not vowel")"""

# 7. Check if a given number is between 1 and 10 (inclusive).
"""num = int(input("Enter the number ="))
if(1 <= num <= 10):
    print("Number is include 1 to 10")
else:
    print("No. is not include 1 to 10")"""
   
# 8. Check if a given string is a palindrome.
"""str = input("Enter the word =")
i= len(str)-1
rev = ""
while(i >= 0):
    rev = rev + str[i]
    i = i - 1
print(rev)
if(str == rev):
    print("This is palindrome")
else:
    print("This is not palindrome")
"""
# 9. Check if a given number is a prime number.
"""num = int(input("Enter the number ="))
count = 0
for i in range(1,num+1):
    if(num % i == 0):
        count = count+1
if(count == 2):
    print(num ,"is prime no.")
else:
    print(num, "is not prime no.")"""

# 10. Check if a given string is a pangram.
char = input("Enter the string =").lower()
letter = "abcdefghijklmnopqrstuvwxyz"

if (ch in letter for ch in char):  
    print("string is a pangram")
else:
    print("String is not pangram")


# 11. Check if a given list is empty.
"""list = []
if(list == []):
    print("list is empty")
else:
    print("list is not empty")"""

# 12. Check if a given number is divisible by both 2 and 3.
"""num = int(input("Enter the Number ="))
if (num % 2 == 0 and num % 3 == 0):
    print("divisible by both 2 and 3")
else:
    print("Not divisible by both 2 and 3")"""

# 13. Check if a given string contains only digits.
"""str = input("Enter the string =")

if (str and str.isdigit()):
    print("contain a digit")
else:
    print("Not contine a digit")"""


# 14. Check if a given number is a perfect square.
"""import math
num = int(input("Enter the number ="))
if (math.isqrt(num) ** 2 == num):
    print("No. is Perfect square")
else:
    print("No. is not perfect square")"""

# 15. Check if a given string starts with a capital letter.
"""char = input("Enter the string =")
if(char and char[0].isupper()):
    print("start with capital latter")
else:
    print("Not start with a capital latter")"""

# 16. Check if a given list contains a specific element.
"""list = [23,45,67,23,45]
el = int(input("Enter the target elelemt ="))

if el in list:
    print("Element is found")
else:
    print("Element is not found") """


# 17. Check if a given number is negative or zero.
"""num = int(input("Enter the Number ="))
if(num < 0 ):
    print("Number is Negative")
elif(num == 0):

    print("Number is Zero")
else:
    print("Not Negative and zero Number-5")""" 
       
# 18. Check if a given string is alphanumeric.
"""str = input("Enter the String =")
if str.isalnum():
    print("alphanumeric")
else:
    print("Not alphanumeric")"""


# 19. Check if a given year is a leap year and divisible by 100.
"""year = int(input("Enter the year ="))
if(year % 4 == 0):
    if(year % 100 == 0):
        print("Leap year and Divisible by 100")
    else:
        print("Leap year but not Divisible by 100")
else:
    print("This is not leap year")"""

# 20. Check if a given list is sorted in ascending order.
"""list = [12,34,56,67,89]
list2 = list.copy()
list2.sort()
if(list == list2):
    print("list is sorted in ascending order")
else:
    print("List is not sorted in ascending order")
"""
# 21. Check if a given string is a palindrome ignoring spaces.
"""text = input("Enter the string =")
space = text.replace(" ", "").lower()

if(space == space[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")"""

# 22. Check if a given number is a Fibonacci number.
"""num = int(input("Enter the number ="))
a = 0
b = 1
found = False
while b <= num:
    if b == num:
        found = True
        break
    a = b
    b =  a + b
if found or num == 0:
    print("This is fabonacci number")
else:
    print("This is not fabonacci number")"""


# 23. Check if a given string is a valid email address.
"""import re
email = input('Enter the email address =')
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'

result = re.match(pattern, email)

if result:
     print('Valid Email')
else:
    print('Invalid email')"""


# 24. Check if a given number is a perfect cube.
"""import math
num = int(input("Enter the number ="))
n = round(num ** (1/3))
if (n ** 3  == num):
    print("No. is Perfect cube")
else:
    print("No. is not perfect cube")"""

# 25. Check if a given string is a valid URL.
"""URL = input("enter the URL =")
if ":" in URL and "/" in URL and "." in URL and URL.index(":") < URL.rindex("."):
    print("valid URL")
else:
    print("Invalid URL")"""

# 26. Check if a given year is a leap year or divisible by 400.
"""year = int(input("Enter the year ="))
if(year % 4 == 0):
    if(year % 400 == 0):
        print("Leap year and Divisible by 400")
    else:
        print("Leap year but not Divisible by 400")
else:
    print("This is not leap year")"""

# 27. Check if a given string contains only uppercase letters.
"""text = input("enter the string = ")
if text and text.isupper():
    print("String is upper case")
else:
    print("string is not upper case")"""

# 28. Check if a given list is sorted in descending order.
"""list = [90,87,65,54,32]
list2 = list.copy()
list2.sort(reverse = True)
if(list == list2):
    print("list is sorted in decending order")
else:
    print("List is not sorted in decending order")"""

# 29. Check if a given number is a power of 2.
"""num = int(input('Enter the number ='))
n = round(num ** (1/2))             # num ** 0.5
if(n ** 2 == num): 
    print("Number is power of 2")
else:
    print("Number is not power of 2")"""    

# 30. Check if a given string is a valid password (meets certain criteria).
"""password = input("Enter the password =")
if len(password) == 10 and "@" in password  :
    print("valid password")
else:
    print("Invalid Password")"""

# 31. Check if a given number is a multiple of both 3 and 4.
"""num = int(input("Enter the Number ="))
if (num % 3 == 0 and num % 4 == 0):
    print("Multiple by both 3 and 4")
else:
    print("Not Multiple by both 3 and 4")"""

# 32. Check if a given string contains only lowercase letters.
"""text = input("enter the string = ")
if text and text.islower():
    print("String is Lower case")
else:
    print("string is not lower case")"""

# 33. Check if a given list contains duplicate elements.
"""list = [23,45,67,46,45,23,34]
duplicate= []
for el in list:
    if list.count(el)> 1 and el not in duplicate:
        duplicate.append(el)
if duplicate:
    print("Duplicate Number",duplicate)
else:
    print("Not Duplicate Number")"""

# 34. Check if a given number is divisible by either 5 or 7.
"""num =int(input("Enter the number ="))
if(num % 5 == 0 and num % 7 == 0):
    print("Divisible by both 5 and 7")
else:
    print("Not Divisible by 5 and 7")"""

# 35. Check if a given string is a valid phone number.
"""phno = input("Enter the phon number =")
if(phno and len(phno) == 10):
    print("valid phone no.")
else:
    print("Invalide phone no.")"""

# 36. Check if a given number is a multiple of 10 and less than 100.
"""num = int(input("Enter the Number ="))
if (num < 100):
    if (num % 10  == 0):
        print("Multiple by 10")
    else:
        print("Not Multiple by 10")
else:
    print("not leass then 100")"""

# 37. Check if a given string is a valid date in the format "DD/MM/YYYY".
"""date = input('Enter the time(DD/MM/YYYY) =')
if(len(date)== 10 and date[2] == "/" and date[:2].isdigit() and date[3:5].isdigit() and date[6:].isdigit()):
    print("valid date")
else:
    print("Invalid date")"""

# 38. Check if a given number is a perfect number.
"""num = int(input("enter the number ="))
sum = 0
for i in range(1, num):
    if(num % i == 0):
        sum = sum + i
if(sum == num):
    print("This is a perfect number")
else:
    print("This is not a perfect number")"""

# 39. Check if a given string is a valid social security number.

# 40. Check if a given number is a prime number and less than 100.
"""num = int(input("enter the number = "))
if(num < 100):
    if(num % 2 == 0):
        print(num ,"is prime number")
    else:
        print(num, "is not prime number")
else:
    print("Not less then 100 number")"""

# 41. Check if a given string is a valid IP address.
"""ip = input("Enter the IP Address =")
if "." in ip and ":" in ip :
    print("Valid IP Address")
else:
    print("Invalid IP Address") """

# 42. Check if a given number is divisible by 2, 3, and 5.
"""num =int(input("Enter the number ="))
if(num % 2 == 0 and num % 3 == 0 and num % 5 == 0):
    print("Divisible by 2 ,3 and 5")
else:
    print("Not Divisible by 2 ,3 and 5")"""

# 43. Check if a given string is a valid username (meets certain criteria).
"""username = input("Enter the username =")
if len(username) == 10 and "@" in username  :
    print("valid username")
else:
    print("Invalid username")"""

# 44. Check if a given number is a palindrome.
"""num = int(input("Enter the number ="))
temp = num 
rev = 0
while(num > 0):
    n = num % 10
    rev = rev * 10 + n
    num = num //10

if(temp == rev):
    print(temp, " is palindrome")
else:
    print(temp, "is not palindrome")"""

# 45. Check if a given string is a valid credit card number.
"""num = input("Enter the credit card numbber =")
if(num and len(num) == 15):
    print("valid credit card number")
else:
    print("Invali credit card number")"""


# 46. Check if a given number is a multiple of 4 and not divisible by 6.
"""num =int(input("Enter the number ="))
if(num % 4 == 0 and num % 6 != 0):
    print("multiple by 4 but not divisible by 6")
else:
    print("Not multiple by 4 and not divisible by 6" )"""

# 47. Check if a given string is a valid time in the format "HH:MM".
"""time = input('Enter the time(HH:MM) =')
if(len(time)== 5 and time[2] == ":" and time[:2].isdigit() and time[3:].isdigit()):
    print("valid time")
else:
    print("Invalid time")"""

# 48. Check if a given number is a perfect number and less than 1000.
"""num = int(input("enter the number ="))
sum = 0
if(num < 1000):
    for i in range(1, num):
        if(num % i == 0):
            sum = sum + i
    if(sum == num):
        print("This is a perfect number")
    else:
        print("This is not a perfect number")
else:
    print("Not less the 1000")"""

# 49. Check if a given string is a valid ISBN-10 number.
"""num = input("Enter the Number =")
if len(num) != 10:
    print("invalid Number")
else:
    total = 0
    for i in range(10):
        if 1 == 9 and num[i].upper() == "X":
            total = total + 10 * (i + 1)
        elif num[i].isdigit():
            total = total + int(num[i]) * (i * 1)    
        else:
            print("invalid character found")
            break
    else:      
        if total % 11 == 0:
            print("valid ISBN Number")
        else:
            print("Invalid ISBN number")
"""
 
# 50. Check if a given number is divisible by the sum of its digits.
  