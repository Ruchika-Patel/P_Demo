# String Assignment Questions
 
#  1. Write a program to count the number of characters in a given string.
"""str = input("Enetr thr string =")
str2 = len(str)
count = 0
for i in range(1,str2):
    count = count+1
print(count)"""


#  2. Write a program to convert a string to uppercase.
"""str = input("Enetr thr string =")
print(str.upper())"""


# 3.  Write a program to check if a string is a palindrome.
"""str = input("Enetr thr string =")
i = len(str)-1
rev = ""
for j in range(i,-1,-1):
    rev = rev + str[j]
if(str == rev):
    print("palindrome")
else:
    print("Not palindrome")"""
 
# 4.  Write a program to count the number of vowels in a given string.
"""str = input("Enter the String = ")
count = 0
for ch in str:
    if((ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u") or 
       (ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U")):
        count = count+1
print(count)"""
 
# 5. Write a program to check if a string is an anagram of another string.
 
# 6. Write a program to find the index of a specific character in a string.
"""str = input("Enter the string: ")
ch = input("Enter the character to find: ")

for i in range(len(str)):
    if str[i] == ch:
        print(i , "index ", str[i])"""

 
# 7. Write a program to check if a string contains only digits.
"""str = input("Enter the string =")

if (str and str.isdigit()):
    print("contain a digit")
else:
    print("Not contain a digit")"""

 
# 8. Write a program to remove all whitespace characters from a string.
"""str = input("Enter the string =")
ws = str.replace(" ", "")
print(ws)"""
    

# 9. Write a program to check if a string starts with a specific prefix.
"""str = input("Enter the string =")
pre = input("Enter the string =")
if str.startswith(pre):
    print("starts with prefix")
else:
    print("starts with not prefix")"""


# 10. Write a program to replace all occurrences of a specific character in a string.
"""str = input("Enter the string = ")
char = input("Enter the character to replace = ")
text = input("Enter the new character = ")

new_str = str.replace(char , text)
print(new_str)"""

# 11. Write a program to find the length of the longest word in a string.
"""str = input("Enter the string = ")
word = str.split()
print(word)
long_len = max(len(word) for word in word)
print(long_len)"""

 
# 12. Write a program to check if a string ends with a specific suffix.
"""str = input("Enter the string =")
end = input("Enter the prefix word =")
if str.endswith(end):
    print("starts with end")
else:
    print("starts with not end")"""

 
# 13. Write a program to capitalize the first letter of each word in a string.
"""str = input("Enter the string =")
capital = str.title()
print(capital)"""
 
# 14. Write a program to find the most frequent character in a string.

 
# 15. Write a program to check if a string contains only alphanumeric characters.
"""str = input("Enter the string =")
if str and str.isalnum():
    print("alphanumeric")
else:
    print("Not alphanumeric")"""


 
# 16. Write a program to split a string into a list of words.
"""str = input("Enter the string =")
result = str.split()
print(result)"""
 
# 17. Write a program to remove all punctuation marks from a string.
"""import string
u_enter = input("Enter the string =")
str2 = str.maketrans('','',string.punctuation)
print(str2)"""
 
# 18. Write a program to check if a string is a valid email address.
"""enter = input("Enter the email = ")
email = "@./"
if any(i in email for i in enter):
    print("valid email")
else:
    print("Invalis email")"""

 
# 19. Write a program to extract the domain name from a URL.
"""url = input("Enter the url =")
url2 = url.replace("https://", "").replace("http://", "").replace("www.", "")
domain = url2.split()
print(domain)"""
 
# 20. Write a program to remove all duplicate characters from a string.
"""str = input("Enter the string =")
result = ""
for i in str:
    for i in not result:
        result = result+i
print(result)"""
    
# 21. Write a program to count the number of occurrences of a specific word in a string.
"""str = input("Enter the string =")
word = input("Enter the word =")
count_word = str.count(word)
print(word , count_word)"""
 
# 22. Write a program to check if a string is a valid password (meets certain criteria).
"""password = input("Enter the password = ")
S_char = "@#$&"
if any(ele in S_char for ele in password):
    print('Valid Password')
else:
    print("Invalid Password")"""


 
# 23. Write a program to find the second most frequent character in a string.
 
# 24. Write a program to convert a string to title case.
"""str = input("Enter the string =")
capital = str.title()
print(capital)"""
 
# 25. Write a program to reverse the order of words in a string.
"""str = input("Enter the string =")
l = str.split()
l.reverse()
print(l)"""
 
# 26. Write a program to check if a string contains only uppercase letters.
"""str = input("Enter the string =")
if (str and str.isupper()):
    print("upper case letter contain")
else:
    print("upper case letter not contain")"""

 
# 27. Write a program to remove a specific word from a string.
"""str = input("Enter the string =")
rem = input("specific word remove = ")
r = str.replace(rem, "")
print(r)"""
 
# 28. Write a program to check if a string is a valid phone number.
"""num = int(input("Enter the ph. no. = "))
l = len(str(num))
if(num and l == 10):
    print("Valid phone no.")
else:
    print("Not valid phone no.")"""
 
# 29. Write a program to check if a string contains only lowercase letters.
"""str = input("Enter the string =")
if (str and str.islower()):
    print("lower case letter contain")
else:
    print("lower case letter not contain")"""
 
# 30. Write a program to extract all URLs from a string.
"""str = input("Enter the URL = ")
if (":" in str or "/" in str or "." in str or "?" in str):
    print("valid URL ")
else:
    print("not valid URL")"""
 
# 31. Write a program to remove leading and trailing whitespace from a string.
"""str = input("Enter the string =")
space = str.strip()
print(space)"""
 
# 32. Write a program to check if a string is a valid social security number.
"""num = input("Enter the number =")
if (len(num) ==  14 and num[:4].isdigit and num[5:9].isdigit and num[10:].isdigit and "-" in num):
    print("valid SSN")
else:
    print("Invalid SSN")"""

# 33. Write a program to check if a string is a valid IP address.
"""str = input("Enter the IP Address = ")
if (":" in str or "." in str ):
    print("valid IP Address ")
else:
    print("not valid IP Address")"""
 
# 34. Write a program to count the number of words in a string.
"""str = input("Enter the string =")
l =len(str.split())
print(l)"""
 
# 35. Write a program to remove the last occurrence of a specific word from a string.
 
# 36. Write a program to check if a string is a valid date in the format "DD/MM/YYYY".
"""date = input("Enter the date(dd/MM/YYYY) = ")
if(len(date) == 10 and "/" in date and date[:2].isdigit() and date[3:5].isdigit() and date[6:].isdigit()):
    print("valid Date")
else:
    print("Invalid Date")"""
 
# 37. Write a program to convert a string to snake case.
"""str = input("Enter the string =")
str2 = str.strip().lower()
result = str2.replace(" ","_")
print(result)"""

# 38. Write a program to remove the first occurrence of a specific word from a string.
 
# 39. Write a program to check if a string is a valid username (meets certain criteria).
"""user_name = input("Enter the user name = ")
S_char = "_"
if any(ele in S_char for ele in user_name):
    print('Valid User Name')
else:
    print("Invalid User Name") """
 
# 40. Write a program to convert a string to camel case.
"""str = input("Enter the string =")
str2 = str.strip().split()
result = str2[0].lower() + ''.join( el.capitalize() for el in str2[1:])
print(result)"""
 
# 41. Write a program to remove all non-alphanumeric characters from a string.
"""import re
text = input("Enter a string: ")
clean_text = re.sub(r'[^a-zA-Z0-9]', '', text)
print("Alphanumeric-only string:", clean_text)"""
 
# 42. Write a program to check if a string is a valid credit card number.
"""num = input("Enter the credit card number =")
if(len(num) == 16 and num.isdigit() and num == " "):
    print("Valid credit card number")
else:
    print("Invalid credit card Number")"""
 
# 43. Write a program to check if a string is a valid time in the format "HH:MM".
"""time = input('Enter the time(HH:MM) =')
if(len(time)== 5 and time[2] == ":" and time[:2].isdigit() and time[3:].isdigit()):
    print("valid time")
else:
    print("Invalid time")"""

 
# 44. Write a program to extract all hashtags from a string.
 
# 45. Write a program to check if a string contains only printable characters.
 
# 46. Write a program to check if a string is a valid ISBN-10 number.
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
            print("Invalid ISBN number")"""
  
# 47. Write a program to extract all email addresses from a string.
 
# 48. Write a program to check if a string is a valid hexadecimal number.
"""num = input("Enter the Hexadecimal number = ")
c =  "0123456789ABCDEF" 
if c in num:
    print("valid Hexadecimal number")
else:
    print("Invalid Hexadecimal number")"""
 
# 49. Write a program to check if a string is a valid binary number.
"""num = input("Enter the Binary number = ")
chr =  "01" 
if chr in num:
    print("valid binary number")
else:
    print("Invalid Binary number")"""
 
