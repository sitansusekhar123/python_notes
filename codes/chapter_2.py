

    
# built in functions

# int() - converts a datatype - (str, float) to an integer
    
# print(int(3.14)) # result: 3
# print(int('3')) # result: 3

# str() - converts a datatype - (int, float) to a string

# x = str(3.14)
# y = x + str(10)
# print(y)

# x = 3
# print(float(x))

# number_list = [1, 2, 3, 4, 5]
# print(min(number_list))

# x = 3.578
# print(round(x,0))

# start = 5
# end = 10
# step = 5
# print(list(range(start, end, step)))

# print(list(range(4,10)))

import math

# print(math.log10(1000)) # result: 3.14
# math.sin(3.14), math.cos(3.14), math.tan(3.14), math.pow(2, 3)
# print(math.pow(2, 3)) # 2^3 = 8
# print(math.sqrt(25)) # square root of 25 = 5
# print(math.factorial(5)) # 5! = 120

# import random

# print(random.randint(1, 1000))

# print(random.random())

# print(random.uniform(1, 1000))

# data_list = [1, 2, 3, 4, 5]

# random.shuffle(data_list)

# print(data_list)


# user defined function

# def func():
#     print('Hello World')

    
# def func2(): 
#     print('Hello World 2')

    
# func()
# func2()

# def addition(a, b):
#     c = a + b
#     d = c * 100
#     return c,d
    
# x,y = addition(5, 10)

# print(x)
# print(y)

# positional arguments
def addition (a, b, c):
    d = a + b
    
    print(d)
    print(c)
    # return c

# addition(c="hello", b=5, a=10)

# addition(10, 5, "hello")
# addition("hello", 10, 5)

# default arguments
# def addition (a, b=100, c="hello"):
#     d = a + b
#     print(d)
#     print(c)
    
# addition(10, 5, "earth")

# keyword argument
# def addition (name, address, age):
#     print(name)
#     print(address)
#     print(age)
    
# addition(age=17, name = "Saksham" , address = "India")

    
'''
total = 0

number = 1, total = 0 + 1 = 1
number = 2, total = 1 + 2 = 3
number = 3, total = 3 + 3 = 6
'''

# number_list = [1, 2, 3, 4, 5]
# print(len(number_list))
# print(number_list[0])
# print(number_list[1])
# print(number_list[4])
# print(number_list[5])

# Local Variable
# Global Variable

# total = 0   # global variable
# string = "hello"

# def addition_list(number_list):
#     total = 0   # local variable
#     for number in number_list:
#         total = total + number
#     print(total)
#     print(string)
#     return total
    
# list_of_number = [1, 2, 3, 4, 5]
# added_total = addition_list(list_of_number)
# print(added_total)

# def print_recursion(string):
#     print_recursion(string)
    
# print_recursion("hello")


# def factorial_recursion(number):
#     if number == 1:
#         return 1
#     else:
#         return number * factorial_recursion(number - 1)
    
# '''
# number = 5

# ELSE: 5 * [factorial_recursion(4) = 24]
# ELSE: 4 * [factorial_recursion(3) = 6]
# ELSE: 3 * [factorial_recursion(2) = 2]
# ELSE: 2 * [factorial_recursion(1) = 1]
# IF: 1
# '''
    
# print(factorial_recursion(5))


# variable length arguments

def addition_numbers(*n):
    total = 0
    for number in n:
        total = total + number
    print(total)
    
addition_numbers(1, 2, 3, 4, 5, 6, 7, "hello")