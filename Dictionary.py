# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
"""my_dic = {
    "apple" : 1,
    "banana" : 3,
    "cherry" : 2
 }
result = dict(sorted(my_dic.items(), key= lambda item : item[1]))
print("Ascending Order = ",result)

result = dict(sorted(my_dic.items(), key= lambda item : item[1] , reverse = True))
print("Descending Order = ",result)"""


#  2. Write a Python script to add a key to a dictionary.
#  Sample Dictionary : {0: 10, 1: 20}
#  Expected Result : {0: 10, 1: 20, 2: 30}
"""dic = {0: 10, 1: 20}
dic.update({2 : 30})      #dic[2] = 30
print(dic)"""

#  3. Write a Python script to concatenate the following dictionaries to create a new one.
#  Sample Dictionary :
#  dic1={1:10, 2:20}
#  dic2={3:30, 4:40}
#  dic3={5:50,6:60}
#  Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
res = dic1 | dic2 | dic3
print(res)"""                        

#  4. Write a Python script to check whether a given key already exists in a dictionary.
"""key = int(input("Enter the key ="))
dic = {0: 10, 1: 20, 2: 30,3: 40, 4:50}
if key in dic:
    print("key already exists")
else:
    print("key not exists")"""

#  5. Write a Python script to generate and print a dictionary that contains a number
#  (between 1 and n) in the form (x, x*x).
#  Sample Dictionary ( n = 5) :
#  Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""n = int(input('Enter the number = '))
dic = {}
for i in range(1,n+1):
    dic[i] = i ** 2
print(dict(dic))"""


#  6. Write a Python program to sum all the items in a dictionary.
"""dic = {0: 10, 1: 20, 2: 30,3: 40, 4:50}
sum = 0
for i in dic.values():
    sum = sum + i
print(sum)"""


#  7. Write a Python program to get the maximum and minimum values of a dictionary.
"""dic = {0: 10, 1: 20, 2: 30,3: 40, 4:50}
min_val = min(dic.values())
max_val = max(dic.values())
print("Minimum value = ",min_val)
print("Maximum value = ",max_val)"""

#  8. Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
#  d2 = {'a': 300, 'b': 200, 'd':400}
#  Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
"""from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
result = Counter(d1) + Counter(d2)
print(result)"""

#  9. Write a Python program to print all distinct values in a dictionary.
#  Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#  {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#  Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""dic = [ {"V":"S001"}, 
       {"V": "S002"}, 
       {"VI": "S001"}, 
       {"VI": "S005"},
       {"VII":"S005"}, 
       {"V":"S009"},
       {"VIII":"S007"}]
my_dic = set()
for d in dic:
    for i in d.values():
        my_dic.add(i)    
print(my_dic)"""    

#  10. Write a Python program to create and display all combinations of letters,
#  selecting each letter from a different key in a dictionary.
#  Sample data : {'1':['a','b'], '2':['c','d']}
#  Expected Output:
#  ac
#  ad
#  bc
#  bd
"""import itertools
dic = {'1':['a','b'], '2':['c','d']}
value = dic.values()
for i in itertools.product(*value):
    print(''.join(i)) """ 


 
#  11. Write a Python program to combine values in a list of dictionaries.
#  Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
#  {'item': 'item1', 'amount': 750}]
#  Expected Output: Counter({'item1': 1150, 'item2': 300})
"""from collections import Counter
dic = [{'item': 'item1', 'amount': 400}, 
       {'item': 'item2', 'amount': 300},
       {'item': 'item1', 'amount': 750}]
res = Counter()
for d in dic:
    res[d['item']] = res[d['item']] + d['amount']
print(res)"""


#  12. Write a Python program to create a dictionary from a string.
#  Note: Track the count of the letters from the string.
#  Sample string : 'google'
#  Expected output: {'g': 2, 'o': 2, 'r': 2, 'e': 1, 'l': 1}
"""str = 'google'
res = {}
for i in str:
    res[i] = res.get(i,0)+1
print(res)""" 


#  13. Write a Python program to get the top three items in a shop.
#  Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#  Expected Output:
#  item4 55
#  item1 45.5
#  item3 41.3
"""dic = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
result = sorted(dic.items(),key = lambda item : item[1], reverse = True)[:3]
for key, value in result:
    print(key, value)"""


#  14. Write a Python program to sort Counter by value.
#  Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
#  Expecte ddata: [('Chemistry',87),('Physics',83),('Math',81)]
"""from collections import Counter
dic = {'Math':81, 'Physics':83, 'Chemistry':87}
res = Counter(dic)
result = sorted(res.items(),key = lambda item : item[1], reverse = True)
print(res)"""

# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from    11-20, 21-30, and 31-40 respectively .Access the fifth value of each key from the dictionary.
#  {'x': [11,12,13,14,15,16,17,18,19],
#  'y': [21,22,23,24,25,26,27,28,29],
#  'z': [31,32,33,34,35,36,37,38,39]}
#  15
#  25
#  35
#  xhasvalue[11,12,13,14,15,16,17,18,19]
#  yhasvalue[21,22,23,24,25,26,27,28,29]
#  zhasvalue[31,32,33,34,35,36,37,38,39] 
"""dic = {'x': [11,12,13,14,15,16,17,18,19],
    'y': [21,22,23,24,25,26,27,28,29],
    'z': [31,32,33,34,35,36,37,38,39]}
print(dic['x'][4])
print(dic['y'][4])
print(dic['z'][4])"""


#  16.Write a Python program to drop empty items from a given dictionary. Original Dictionary:
#  {'c1': 'Red', 'c2': 'Green', 'c3':None}
#  New Dictionary after dropping empty items:
#  {'c1': 'Red', 'c2': 'Green'}
"""dic = {'c1': 'Red', 'c2': 'Green', 'c3':None}
my_dic = {}
for key , value in dic.items():
    if value is not None: 
        my_dic[key] = value  
print(my_dic)"""  



#  17.Write a Python program to verify that all values in a dictionary are the same. Original Dictionary:
#  {'CierraVega':12, 'AldenCantrell':12, 'KierraGentry':12, 'PierreCox':12}
#  Check all are 12 in the dictionary.
#  True
#  Check all are 10 in the dictionary.
#  False
"""dic = {'CierraVega':12, 'AldenCantrell':12, 'KierraGentry':12, 'PierreCox':12}
if all(value == 12 for key , value in dic.items()):
    print(True)
else:
    print(False)"""
        
    

#  18.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
#  Original list:
#  [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
#  Grouping a sequence of key-value pairs into a dictionary of lists:
#  {'yellow': [1,3], 'blue': [2,4], 'red': [1]}
"""dic = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
my_dic = {}
for key ,value in dic:
    if key not in my_dic:
        my_dic[key] = []
    my_dic[key].append(value)
print(my_dic)"""

# 19. Write a Python program to split a given dictionary of lists into lists of dictionaries.
#  Original dictionary of lists:
#  {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#  Split said dictionary of lists into list of dictionaries:
#  [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62,
#  'Language': 84}, {'Science': 95, 'Language': 80}]
"""dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
my_list = []
for sci, lng in zip(dic['Science'], dic['Language']):
    my_list.append({'science' : sci, 'language': lng })
print(my_list)"""



#  20. Write a Python program to extract a list of values from a given list of
#  dictionaries.
#  Original Dictionary:
#  [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
#  Extract a list of values from said list of dictionaries where subject = Science
#  [92, 94, 88]
#  Original Dictionary:
#  [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
#  Extract a list of values from said list of dictionaries where subject = Math
#  [90, 89, 92]
"""dic = [{'Math': 90, 'Science': 92},
       {'Math': 89, 'Science': 94}, 
       {'Math': 92, 'Science': 88}]
sci = []
for d in dic:
    sci.append(d['Science'])
print('Science : ',sci)

math = []
for m in dic:
    math.append(m['Math'])
print('Math :',math)"""