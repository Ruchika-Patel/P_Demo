#Q.1  Write a recursive function to calculate the factorial of a number.
"""def fact(n):
    if(n == 0):
        return 1
    else:
        return n * fact(n-1)
print(fact(5))"""

# Q.2 Write a recursive function to calculate the sum of first n natural numbers.
"""def sum(n):
    if(n == 0):
        return 0
    else:
        return n + sum(n-1)
print(sum(10))"""

# Q.3 Write a recursive function to print numbers from n to 1.
"""def num(n):
    if(n == 0):   // stop condition
        return 
    print(n)
    num(n-1)
    print("end")
num(10)"""

# Q.4 Write a recursive function to print numbers from 1 to n.
"""def print_num(n):
    if(n == 11):      //stop condition
        return 
    print(n)
    print_num(n+1)
print_num(1)"""    

# Q.5 Write a recursive function to compute the nth Fibonacci number.
"""def fabonacci(n):
    if(n == 6):
        return 0
    else:
        return n + fabonacci(n+1)
print(fabonacci(1))"""

# Q.6 Write a recursive function to calculate the sum of digits of a number.
"""def sum(n):
    if(n == 0):
        return 0
    else:
        return n % 10 + sum(n//10)
print(sum(1234))   
"""

# Q.7 Write a recursive function to reverse a string.
"""def revers(n,rev=0):
    if(n < 10):
        return n 
    else:
        return int(str(n % 10) + str(revers(n//10)))
print(revers(1234))"""

