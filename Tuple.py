# 1. Create a tuple of your favorite colors.
"""color = ("Red","green","Pink","Black")
print(color)"""

#  2. Access the third element of a tuple.
"""color = ("Red","green","Pink","Black")
print(color[3])"""

#  3. Find the length of a tuple.
"""num = (2,3,4,5,6,7,8,3,1)
print(len(num))"""

#  4. Check if a specific element exists in a tuple.
"""num = (11,12,13,14,15,16)
ele = int(input("Enter the exists element = "))
if(ele in num):
    print("Exist element")
else:
    print("Not exist element")"""

#  5. Slice a tuple to extract a specific range of elements.
"""num = (11,12,13,14,15,16,17,18)
print(num[2:6])"""

#  6. Concatenate two tuples.
"""num = (11,12,13,14,15,16,17,18)
color = ("Red","green","Pink","Black")
result = num + color
print(result)"""

#  7. Repeat a tuple three times.
"""num = (26,22,6)
result = num * 3
print(result)"""

#  8. Convert a list into a tuple.
"""num = (11,12,13,14,15,16,17,18)
result = list(num)
print(result)"""

#  9. Convert a tuple into a list.
"""num = [11,12,13,14,15,16,17,18]
result = tuple(num)
print(result)"""

#  10. Find the index of a specific element in a tuple.
"""num = (11,12,13,14,15,16,17,18)
idx = num.index(13)
print(idx)"""

#  Tuple Functions and Methods
#  11. Use the max() and min() functions on a tuple.
"""num = (11,12,13,14,15,16,17,18)
result = min(num)
result2 = max(num)
print('Minimun Number :',result)
print('Maximun number :',result2)"""

#  12. Sort a tuple of numbers in ascending order.
"""num = (2,3,4,5,6,7,8,3,1)
num2 = list(num)
num2.sort()
print(num2)"""

#  13. Sort a tuple of strings in descending order.
"""num = (2,3,4,5,6,7,8,3,1)
num2 = list(num)
num2.sort(reverse = True)
print(num2)"""

#  14. Count the occurrences of a specific element in a tuple.
"""list2 = (12,23,34,45,56,67,12,34,)
num = int(input("Enter the number = "))
result = list2.count(num)
print(result)"""

#  15. Create a tuple of mixed data types.
"""mix_dt = ("Ruchika",23,"Indore",34.56,True)
print(mix_dt)"""

#  16. Unpack a tuple into multiple variables.
"""info = ("Ruchika",23,"Indore")
name , age , city = info
print("Name :",name)
print("Age : ",age)
print("City : ",city)"""

#  17. Create a nested tuple.
"""tup = ((1,2,3),(4,5,6),(7,8,9))
print(tup)"""
        
# 18. Access elements from a nested tuple.
"""tup = ((1,2,3),(4,5,6),(7,8,9))
for i in range(len(tup)):
    for j in range(len(tup[i])):
        print(tup[i][j],end = " ")"""

#  19. Use the enumerate() function on a tuple.
"""name = ("Ruchika","Ranu","manshi","priynashi","mohit")
for ind , i in enumerate(name):
    print(ind,i)"""

#  20. Use the zip() function to combine two tuples.
"""tpl1 = [12,34,56,76]
tup2 = [3,4,5,7,8]
result = tuple(zip(tpl1 , tup2))
print(result)"""

#  21. Find the tuple with the maximum sum of elements from a list of  tuples.
"""tup = [(1,2,3),(4,5),(10,1),(2,12)]
result = max(tup,key=sum)
print(result)"""

#  22. Reverse a tuple without using built-in functions.
"""num = (11,12,13,14,15,16,17,18)
temp = len(num)
for i in range(temp-1,-1,-1):
    print(num[i], end = " ")"""

#  23. Create a tuple of tuples, where each inner tuple contains the square of the corresponding elements in a given tuple.
"""tup = (2,4,6,8)
for i in tup:
    result = i**2
    print(result)"""

#  24. Find the common elements between two tuples.
"""tpl = (2,3,4,5,6,7)
tpl2 = (3,5,6,8,9)
result = tuple(set(tpl) & set (tpl2))
print(result)"""

#  25. Find the unique elements in a tuple.
"""tpl = (3,4,5,6,3,4,2,2,7)
tpl2 = set(tpl)
print(tpl2)"""

#  26. Write a function to check if a tuple is a palindrome.
"""num = int(input("Enter the number = "))
temp = num
p = 0
while(temp>0):
    r = temp % 10
    p = (p*10) + r
    temp = temp // 10

if(num == p):
    print("Palindrome")
else:
    print("Not palindrome") """

#  27. Write a function to find the most frequent element in a tuple.


#  28. Write a function to remove duplicate elements from a tuple.
"""tpl = (3,4,5,6,3,4,2,2,7)
temp = []
for i in tpl:
    if i not in temp:
        temp.append(i)
print(temp)"""

#  29. Write a function to rotate a tuple to the left by a given number of positions.
"""tpl = (10,20,30,40,50,60)
n = 2
result = tpl[n:] + tpl[:n]
print(result)"""

#  30. Write a function to rotate a tuple to the right by a given number of positions.
"""tpl = (10,20,30,40,50,60)
n = 2
result = tpl[-n:] + tpl[:-n]
print(result)"""