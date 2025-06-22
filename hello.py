# palindrom
"""list = [1,2,1]
cp = list.copy()
cp.reverse()
if(list==cp):
     print("palindrom")
else:
    print("not palindrom")"""


"""tup = ("C","D","A","A","B","B","A")
tup1=tup.count("A")
print(tup1)"""

"""
tup = ["C","D","A","A","B","B","A"]
tup.sort()
print(tup)"""

# dictionary
"""info ={
    "Name" : "Ruchika",
    "College" : "SGSITS",
    "Marks" : 68,
    "Age" : 21,
}"""

"""new_Dict = { "Address" : "Indore"}
info.update(new_Dict)
print(info)"""


# Set 
"""Set = { 1,3,4,5,7,5,7,8,7}
set2 ={1,2,6,9,7}

a=Set.intersection(set2)
print(a)"""


"""dict = {
    "table" : ["a piece of funiture" , "list of fact is figure"],
    "cat" : "a Small Animal",
}
print(dict)"""

# Table 
"""n = int(input("Enter the number ="))
i=1 
while i<=10:
    t=n*i
    print(t)
    i+=1"""


"""nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(nums):
    print(nums[i])
    i+=1"""


"""nums = (1,4,9,16,25,36,49,64,81,100)    

x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx",i)
    i+=1"""

"""i=1
while i <= 15:
    if(i%2== 0):
       i+=1
       continue
    print(i)
    i+=1"""

"""list =[12,34,56,67,78,4]
str = "Ruchika"
for char in str:
    if(char=="R"):
        print(char)
        break
else:
    print("The end")"""


"""nums = [1,4,9,16,25,36,49,64,81,100]
x=64
ind=0
for i in nums:
    if(i==x):
        print("No. is found",ind)
    ind+=1
"""

"""for i in range(1,100):
    print(i)"""
"""for i in range(100,0,-1):
    print(i)
"""

#factorial
"""n=5
fact=1
for i in range (1,n+1):
    fact=fact*i
print(fact)
"""

#sum of n natural number
"""n=10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)"""
"""
def clac_sum(a,b,c):
    sum = a + b + c
    avg = sum/3
    print(avg)
                                               
clac_sum(12,3,4)
clac_sum(10,4,4)
"""

"""def fat(n): 
    fact = 1
    for i in range(1, n+1):
        fact*=i   
    print(fact)
fat(5)"""


"""def convert(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR ")

convert(34)"""

#recurtsion

"""def show(n):
    if(n == 0):
        return 
    print(n)
    show(n-1)
show(3)"""

"""def fact(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact(n-1)
print(fact(4))"""


"""def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
cal=sum(10)
print(cal)"""
1

"""f = open("Demo.txt", "r")
data = f.readline()
print(data)
data2 = f.readline()
print(data2)
f.close()  """

"""def show(n):
    if(n == 11):
        return  
    print(n)
    show(n+1)
show(1)"""

 #1. Check if a given number is positive.
num = int(input("Enter the Number ="))
if(num >= 0):
    print(num ," is positive Number")
else:
    print(num ," is Negative Number")

# 2. Check if a given number is even.
num = int(input("Enter the Number = "))
if(num % 2 == 0):
    print("Enen Number")
else:
    print("Odd Number")