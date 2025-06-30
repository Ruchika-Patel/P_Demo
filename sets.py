
#  1. Create a set containing the numbers 1 to 10.
"""s = set(range(1,11))
print(s)"""

#  2. Write a function that takes two sets and returns their union. 
"""def uni(s1, s2):
    result = s1.union(s2)
    print(result)
    return 
s1 = {2,3,4,7,6}
s2 = {5,6,7}
uni(s1,s2)"""

#  3. Write a function that checks if a set is a subset of another set.

#  4. Create a set with some duplicate values and show how to remove duplicates.
"""s = {2,3,4,5,6,2,4,5}
print(s)"""

#  5. Write a function to find the intersection of two sets.
"""s = {2,3,4,5,6,7}
s2 = {3,4,5,6,9,8}
result = s.intersection(s2)
print(result)"""

#  6. Create a set from a list of fruits: 
"""fruits =  ['apple', 'banana', 'orange', 'apple']
result = set(fruits)
print(result)"""

#  7. Write a program to check if a given element is in a set.
"""set = {2,3,4,5,6,7}
ele = int(input("Enter the num = "))
if ele in set:
    print("Element is in set ")
else: 
    print("Element is not in set ")"""

#  8. Find the difference between two sets.
"""s = {2,3,4,5,6,7}
s2 = {3,4,5,6,9,8}
result = s.difference(s2)
print(result)"""

#  9. Create a set of even numbers from 1 to 20.
"""s = set()
for i in range(0,21):
    if(i % 2 == 0):
        s.add(i)
print(s)"""

#  10.Write a function that returns the size of a set.
"""def size(my_set):
    result = len(my_set)
    print(result)

my_set = {12,23,34,45,67,56,34,57,90,54,33}
size(my_set)"""


#  11. Write a function that returns the symmetric difference between two sets.
"""def sym_dif(s1, s2):
    result = s1.difference(s2)
    print(result)

s1 = {2,3,4,7,6}
s2 = {5,6,7}
sym_dif(s1,s2)"""

#  12.Create a set from a string and show how to find unique characters.
"""my_string = "Ruchika Patel"
my_set = set(my_string)
print(my_set)"""

#  13.Write a program to find all the common elements between two lists using sets.
"""L1 = [2,3,4,5,6]
L2 = [3,5,6,7]
s1 = set(L1)
s2 = set(L2)
result = s1.intersection(s2)
print(result)"""

#  14.Create a set of squares of numbers from 1 to 10.
"""s = set()
for i in range(1,11):
    res = i**2
    s.add(res)
print(s)"""

#  15.Write a function to remove an element from a set safely (without error if the element is not found).
"""def remov(my_set):
    my_set.remove(5)
    return my_set 
my_set = {2,3,4,5,6,7,8}
r = remov(my_set)
print(r)"""

#  16.Find all the unique words in a given sentence using sets.


#  17.Write a function that takes a list and returns a set of its unique elements.
#  18.Create a set of prime numbers between 1 and 50.
"""my_set = set()
for i in range(1,51):
    count = 0
    for j in range(1,i+1):
        if(i % j == 0):
            count = count + 1
            
    if count == 2:
        print(i)"""

#  19.Write a program to merge two sets and remove duplicates.
"""s1 = {2,3,4,5,6,7}
s2 = {3,4,5,6,9,8}
res = s1.union(s2)
print(res)"""

#  20.Find the maximum and minimum elements in a set.
"""s2 = {3,4,5,6,9,8}
min = min(s2)
max = max(s2)
print("Minimum element =",min)
print("Maximum element = ",max)"""

#  21.Create a set with the first 10 Fibonacci numbers.
"""fib_set = set()
a , b = 0 , 1
for i in range(11):
    fib_set.add(a)
    a , b = b , a+b
print(fib_set)"""

#  22.Write a function to check if two sets are disjoint.
"""s1 = {2,3,4,5,6,7}
s2 = {3,4,5,6,9,8}
res = s1.isdisjoint(s2)
print(res)"""

#  23.Create a set from a list of names and find the longest name.
"""my_set = {"Ruchika" , "Ranu", "Manisha","patel"}
res = max(my_set, key = len) 
print(res)"""

#  24.Write a program that counts the occurrences of each element in a list using sets.
"""list1 = [2,3,4,5,6,3,5,3,8]
my_set = set(list1)
for i in my_set:
    count = list1.count(i)
    print(i ,"occure",count)"""

#  25.Create a set of random integers and write a function to find the average.
"""import random
my_set = set()
for i in range(1,6):
    my_set.add(random.randint(1,100))
print(my_set)

avg = sum(my_set)/len(my_set)
print(avg)"""

#  26.Write a function to convert a list of tuples into a set of their first elements.
"""my_list = [(1, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
my_set = set()
for tup in my_list:
    my_set.add(tup[0])
print(my_set)"""

#  27.Create a set from user input and display its contents.
"""user_input = input("Enter input by user =")
my_set = set(user_input.split())
print(my_set)"""

#  28.Write a program that compares two sets and outputs the differences.
"""s = {2,3,4,5,6,7}
s2 = {3,4,5,6,9,8}
result = s.difference(s2)
print(result)"""

#  29.Create a set containing the vowels in the English alphabet.
"""vowel = {'a','e','i','o','u'}
print(vowel)"""

#  30.Write a function to find the Cartesian product of two sets.
"""def product(s,s2):
    return {(i,j) for i in s for j in s2}

s = {2,3,4}
s2 = {2,4,6}
result = product(s,s2)
print(result)"""

#  31.Create a set of numbers and write a function to return the second largest number.
"""my_set = set()
def second_largest(s):
    s.remove(max(s))
    sec_largest = max(s)
    print(sec_largest)

s = {23,45,67,89,90,56}
second_largest(s)"""

#  32.Write a program that finds the common elements in three sets.
"""s = {2,3,4,5,6,7}
s2 = {3,4,5,6,9,8}
s3 = {3,6,7,9}
result = s.intersection(s2,s3)
print(result)"""

#  33.Create a set from a list of integers and return a set of their cubes.
"""num = [2,3,4,5]
my_set = set(num)
for i in my_set:
    res = i ** 3
    print(res)"""

#  34.Write a function to determine if a set is a superset of another set.


#  35.Create a set of characters from a string and display them in sorted order.
#  36.Write a program that takes a set and returns a new set with each element doubled.
#  37.Create a function to find all unique triplets in a list that sum to zero.
#  38.Write a program to find the longest subsequence in a list using sets.
#  39.Create a set of integers and find the product of all elements.
"""my_set = {2,3,4,5}
pro = 1
for i in my_set:
    pro = pro * i
print(pro)"""

#  40.Write a function to find the union of multiple sets.
"""def uni(s,s2,s3):
    res = s.union(s2,s3)
    return res
s = {2,3,4,5,6,7}
s2 = {3,4,5,6,9,8}
s3 = {3,6,7,9}
result = uni(s,s2,s3)
print(result) """

#  41.Create a set from a dictionary's keys.
"""my_dic = {
    "name" : "ruchika",
     "age" : 22,
     "Address" : "Indore"
}
result = set(my_dic.keys())
print(result)"""

#  42.Write a program to count the number of unique elements in a list.
"""list1 = [23,45,56,32,23,45,76]
res = set(list1)
count = len(res)
print(count)"""

#  43.Create a set from a range of numbers and find its median.
"""import statistics
my_set = set(range(1,30))
median = statistics.median(my_set)
print(median)"""

#  44.Write a function to partition a set into two subsets based on a condition.
"""def partition(s):
    my_set = set()
    my_set2 = set()
    for i in s:
        if(i <= 5):
            my_set.add(i)
        else:
            my_set2.add(i)
    print(my_set)
    print(my_set2)

s = {1,2,3,4,5,6,7,8,9,10}
partition(s)"""

#  45.Create a set from a list of tuples and return a set of unique second elements.

#  46.Write a program that generates all subsets of a given set.

#  47.Create a function to compute the power set of a set.
#  48.Write a program to check if a set contains a consecutive sequence.
#  49.Create a set of integers and write a function to find the GCD of all elements.
#  50.Write a function that takes a set and returns the elements in reverse order.