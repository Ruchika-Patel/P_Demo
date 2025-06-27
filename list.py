# Python List Assignment Questions
#  1. How do you create an empty list in Python?
"""list = []
print(list)"""

#  2. How can you initialize a list with some values?
"""list = [2,3,4,5,7,2,1]
print(list)"""

#  3. How do you access elements in a list by their index?
"""list = [3,4,6,77,4,1,43,56,]
for i in range(len(list)):
    print(list[i],"inset" , i)"""

#  4. What happens if you try to access an index that is out of range in a list?
"""list = [3,4,5,6,7,8,9,4,5,4]
l = len(list)
for i in range(1 , l+3):
    if i < len(list):
        print(list[i])
    else:
        print("Index", i, "is out of range")"""

#  5. How do you add an element to the end of a list?
"""list = [11,12,13,14,15]
list.append(16)
print(list)"""

#  6. How do you add an element at a specific index in a list?
"""list = [11,12,14,15]
list.insert(2,13)
print(list)"""

#  7. How do you remove an element from a list by its value?
"""list = [11,12,13,14,15]
list.remove(14)
print(list)"""

#  8. How do you remove an element from a list by its index?
"""list = [11,12,13,14,15]
list.pop(2)
print(list)"""

#  9. How do you find the length of a list?
"""list = [11,12,13,14,15]
print(len(list))"""

#  10. How do you check if an element exists in a list?
"""list = [11,12,13,14,15]
ele = int(input("Enter the exists element = "))
if ele in list:
    print("Exist element")
else:
    print("Not Exist element")"""

#  11. How can you count the occurrences of a specific element in a list?
list2 = [12,23,34,45,56,67,12,34,]
num = int(input("Enter the number = "))
result = list2.count(num)
print(result)


#  12. How do you slice a list to get a sub-list?
"""list = [12,23,34,45,56,67]
list2 = list[2:4]
print(list2)"""

#  13. How can you reverse the order of elements in a list?
"""list = [12,34,56,78,45,32]
list.reverse()
print(list)"""

#  14. How do you sort a list in ascending order?
"""list = [12,14,16,11,17,13,15,18]
list.sort()
print(list)"""

#  15. How do you sort a list in descending order?
"""list = [12,14,16,11,17,13,15,18]
list.sort(reverse = True)
print(list)"""

#  16. How can you create a copy of a list?
"""list = [12,14,16,11,17,13,15,18]
list_copy = list.copy()
print(list_copy)"""

#  17. How do you concatenate two lists?
"""list = [11,12,13,14,15]
list2 = [16,17,18,19,20]
cnt = list + list2
print(cnt)"""

#  18. How can you check if all elements in a list satisfy a certain condition?
"""name = ["Ruchika","Ranu","patel"]
result = all(i.startswith("R") for i in name)
print(result)"""

#  19. Howcanyoucheck if any element in a list satisfies a certain condition?
"""name = ["Ruchika","Ranu","patel"]
result = any(i.endswith("a") for i in name)
print(result)"""

#  20. How do you find the minimum and maximum elements in a list?
"""list = [2,5,7,5,3,1,8,7,9]
min = min(list)
max = max(list)
print("Minimum element = ",min)
print("Maximum element = ",max)"""

#  21. How can you find the sum of all elements in a list?
"""list = [2,5,7,5,3,1,8,7,9]
sum = 0
for i in list:
    sum = sum + i
print(sum)"""

#  22. How do you find the average of elements in a list?
"""list = [2,5,7,5,3,1,8,7,9]
sum = 0
for i in list:
    sum = sum + i
avg = sum/len(list)
print(avg)"""

#  23. How do you find the index of the first occurrence of a specific element in a list?



#  24. How do you remove all elements from a list?
"""list = [2,3,4,5,6,7]
list.clear()
print(list)"""

#  25. How can you iterate over the elements of a list using a for loop?
"""list = [12,23,45,56,67,78]
for i in list:
    print(i)"""

#  26. How can you iterate over the elements of a list using a while loop?
"""list = [12,34,45,56,67,78,34,54]
i = 0
while(i < len(list)):
    print(list[i])
    i = i+1"""

#  27. How do you convert a list of strings into a single string?
"""list = ["My" , "name", "is" ,"Ruchika", "Patel"]
list2 = " ".join(list)
print(list2)"""

#  28. How can you split a string into a list of substrings?
"""list = "My name is Ruchika Patel"
list2 = list.split()
print(list2)"""

#  29. How do you create a list of numbers within a specific range?
"""list = [12,34,45,56,67,78,34,54]
for i in range(1, len(list)):
    print(list[i])"""

#  30. How do you find the unique elements in a list?
"""list = [1,2,3,4,3,2,5,5,6,7,6,]
list2 = set(list)
print(list2)"""


#  31. How can you check if two lists are equal?
"""list = [11,12,13,14,15]
list2 = [11,12,13,14,15]

if(list  == list2):
    print("list is equal")
else:
    print("list not equal")"""

#  32. How can you check if two lists have at least one element in common?
"""list = [1,2,3,4,5,6]
list2 = [7,8,9,10,3,4]
if any(i in list for i in list2):
    print("Atleast one element common")
else:
    print("No common element")"""

#  33. How do you remove duplicates element from a list?
"""list = [2,3,4,5,3,4,6]
duplicate = []
for i in list:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)"""


#  34. How can you extend one list with the elements of another list?  
"""list1 = [1,2,3,4]
list2 = [5,6,7]
list1.extend(list2)
print(list1)"""

#  35. How do you create a list with a repeating element?
"""list = [4]*3 + [5]*2 + [2]*3 
print(list)"""

#  36. How can you convert a list of integers into a list of strings?
"""num = [23,2,35,6,5,7,8,6]
s_list = list(map(str , num))
print(s_list)"""

#  37. How do you check if a list is empty?
"""list = []
if not list:
    print("list is empty")
else:
    print("list is not empty")"""

#  38. How can you create a list using the map() function?
"""User_input = input("Enter the element = ")
s_list = User_input.split()    # convert into string
num = list(map(int, s_list))  #convert into integer
print(num)"""

#  39. How do you zip two lists together?
"""name = ["Ruchika","Nikita","Deepali","manisha"]
marks = [98,69,69,67]
result = list(zip(name, marks))
print(result)"""

#  40. How can you transpose a list of lists?
"""matrix = [[2,3,4],[5,6,7]]
transpose = list(zip(* matrix))
print(transpose)"""

#  41. How do you find the index of the last occurrence of a specific element in a list?
 
#  42. How can you create a list of tuples from two separate lists?
"""list1 = [2,3,4,5]
list2 = ['A','B','C','D']
result = list(zip(list1,list2))
print(result)"""

#  43. How do you convert a list of tuples into two separate lists?
"""list1 = [(2, 'A'), (3, 'B'), (4, 'C'), (5, 'D')]
rst1 ,rst2 = zip(*list1)
print(rst1)
print(rst2)"""

#  44. How can you find the second largest element in a list?
"""list = [34,56,78,89,90,23,100]
list.remove(max(list))
sec_largest = max(list)
print(sec_largest)"""

#  45. How do you add multiple elements to a list at once?
"""list = [2,3,4]
list.extend([5,6,7,8])
print(list)"""

#  46. How can you remove multiple elements from a list at once?
"""list = [2, 3, 4, 5, 6, 7, 8]
list.clear()
print(list)"""

#  47. How do you check if a list is sorted?
"""list = [34,56,78,89,90,23]
if list == sorted(list):
    print("List is sorted")
else:
    print("List is not sorted")"""

#  48. How can you reverse the order of elements in a list without using slicing or the reverse() method?
"""list = [11,12,13,14,15,16,17]
temp = len(list)
for i in range(temp-1,-1,-1):
    print(list[i],end = " ")"""

#  49. How do you create a list of the first n natural numbers?
"""num = int(input("Enter the number = "))
for i in range(1,num+1):
    print(i)"""

#  50. How can you flatten a list of lists into a single list?
"""list = [[2,3,4,5],[6,7,8,9],[4,5,6,7]]
list2 = []
for i in list:
    for j in i:
        list2.append(j)
print(list2)"""

