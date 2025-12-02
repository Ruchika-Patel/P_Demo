"""val = input("Enter the value =")
dic = {'Name' : 'Ruchika',
       'last_name' : 'patel',
       'Age' : 21}
if val in dic.values():
    print("exist value")
else:
    print("not exist value")"""
    

# Write a Python script to sort (ascending and descending) a dictionary by value.
"""my_dic = {
    "apple" : 2,
    "banana" : 1,
    "cherry" : 3
 } 
result = dict(sorted(my_dic.items(), key = lambda items : items[1]))
print(result)

res = dict(sorted(my_dic.items(), key = lambda items :items[1], reverse=True))
print(res)"""

# Write a Python script to check whether a given key already exists in a dictionary.
"""key = int(input("Enter the number ="))
dic = {0: 10, 1: 20, 2: 30,3: 40, 4:50}
if key in dic.keys():
    print('Already exist key')
else:
    print('Not exist key')"""


#5. Write a Python script to generate and print a dictionary that contains a number
#  (between 1 and n) in the form (x, x*x).
#  Sample Dictionary ( n = 5) :
#  Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""n = int(input('Enter the number ='))
dict = {}
for i in range(1,n+1):
    dict[i] = i ** 2
print(dict)""" 

#Assignment 4th Practice Questions
# 1. To find the sum of all odd numbers till 100.
"""sum = 0
for i in range(1,101):
    if(i % 1 == 0):
        sum = sum + i
print(sum)"""

#2. To find the sum of first 100 integers.
"""sum = 0
for i in range(1,101):
    if(i % 2 == 0):
        sum = sum + i
print(sum) """

#3. To find the factorial of number n.
"""n = int(input("Enter the number ="))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)"""

#4. To find the first n numbers in a Fibonacci series.
"""n =  int(input("Enter the number ="))
a = 0
b = 1
for i in range(0 , n+1):
    print(a)
    a = b 
    b = a+b""" 

#5. To find the sum of digits of a number
"""num = int(input("Enter the number ="))
sum = 0 
for i in range(1,num+1):
    sum += i
print(sum)"""

#6. To find whether a number is prime or not.  
"""num = int(input("Enter the number ="))
count = 0
for i in range(1, num+1):
    if (num % i == 0):
        count = count +1
if(count == 2):
    print("Prime No")
else:
    print("Not Prime No")"""

#7. Test whether a given year is leap year or not.
"""num = int(input("Enter the number ="))
if(num % 4 == 0):
    print("This year is leap year")
else:
    print("This is not leap year")"""



"""with open("data.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")"""

"""vowels = "aeiouAEIOU"
vc = cc = dc = 0
with open("data.txt", "r") as file:
    for ch in file.read():
        if ch.isdigit():
            dc += 1
        elif ch.isalpha():
            if ch in vowels:
                vc += 1
            else:
                cc += 1
print("Vowels:", vc, "Consonants:", cc, "Digits:", dc)"""


"""with open("data.txt", "r") as file:
    words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)"""


with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    for line in src:
        dest.write(line)
print("File copied successfully!")





