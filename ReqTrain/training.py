# x = [6,3,2]
# y = [i**2 for i in x]
# print(y)
#
# x = [6, 3, 2]
# g = (i**2 for i in x)  # generator expression
# print(next(g))         # -> 36
#
# class Person:
#     pass
#
# p = Person()
# print(p)
#
# p.firstname = "Hello"
# print(p.firstname)

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
# p1 = Person("Yaseen","Sheriff")
# p2 = Person("Mohamed","Sheriff")
#
# print(p1.fname, p1.lname)
# print(p2.fname, p2.lname)
#
# help(Person)
#
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

# class Employee(Person):
#     all_employees = []
#     def __init__(self, fname, lname, empid):
#         Person.__init__(self, fname, lname)
#         self.empid = empid
#         Employee.all_employees.append(self)
#
# e1 = Employee("John","smith",123456)
# print(e1.empid)
#
# list1 = ["yaseen","sheriff","yaseen","mohamed"]
# class Employee(list):
#     def search(self, name):
#         matching_employees = []
#         for emp in Employee.all_employees:
#             if name in emp.fname:
#                 matching_employees.append(emp.fname)
#         return matching_employees
#
# e1 = Employee("John","smith",123456)
# print(e1.empid)

# class Employee(Person):
#     all_employees = []
#     def __init__(self, fname, lname, empid):
#         Person.__init__(self, fname, lname)
#         self.empid = empid
#         Employee.all_employees.append(self)
#     def getSalary(self):
#         return 'You get Monthly salary.'
#     def getBonus(self):
#         return 'You are eligible for Bonus.'
#
# e1 = Employee("John","smith",123456)
# print(e1.fname, e1.lname, e1.empid,"\n", e1.getSalary(), "\n",e1.getBonus())

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
# class Employee(Person):
#     emps = []
#     def __init__(self, fname, lname, empid):
#         Person.__init__(self, fname,lname)
#         self.empid = empid
#         Employee.emps.append(self)
#
# e = Employee("Yaseen", "Sheriff",123)
# print(e.fname, e.lname, e.empid)

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
# class Emp(Person):
#     emps = []
#     def __init__(self, fname, lname, empid):
#         Person.__init__(self, fname, lname)
#         self.empid = empid
#         Emp.emps.append(self)
#     def getBonus(self):
#         return "get bonus"
#
# e = Emp("Yaseen", "Sheriff", 123)
# print(e.empid, e.fname, e.lname)
#
# class A:
#     def __init__(self, x=5, y=4):
#         self.x = x # 5
#         self.y = y # 4
#
#     def __str__(self):
#         return 'A(x: {}, y: {})'.format(self.x, self.y) # 5 4
#
#     def __eq__(self, other):
#         return self.x * self.y == other.x * other.y
#
#
# def f1():
#     a = A(12, 3)
#     b = A(3, 12)
#     if (a == b):
#         print(b != a)
#         print(a)
#
#
# f1()
#
# class grandpa(object):
#     pass
#
# class father(grandpa):
#     pass
#
# class mother(object):
#     pass
#
# class child(mother, father):
#     pass
#
# print(child.__mro__)
#
# class A:
#     def __init__(self, a = 5):
#         self.a = a
#
#         def f1(self):
#             self.a += 10
#
#
# class B(A):
#     def __init__(self, b = 0):
#         A.__init__(self, 4)
#         self.b = b
#
#     def f1(self):
#         self.b += 10
#
# x = B()
# x.f1()
# print(x.a,'-', x.b)
#
# class class1:
#     a = 1
#
#     def f1(self):
#         a = 2
#         class1.a += 1
#         print(class1.a, end=' ')
#         print(a, end=' ')
#
# class1().f1()
# class1().f1()
#
#
# class Movie:
#     print(name)
#
#     def __init__(self, name_of_movie, no_of_tickets, total_cost):
#         self.name_of_movie = name_of_movie
#         self.no_of_tickets = no_of_tickets
#         self.total_cost = total_cost
#
#     def __str__(self):
#         print("Movie : ", Movie.name_of_movie)
#         print("Number of Tickets :", Movie.no_of_tickets)
#         print("Total Cost : ", Movie.total_cost)

# !/bin/python3

import math
import os
import random
import re
import sys


# Write your code here

# class Movie:
#     print()
#
#
# if __name__ == '__main__':
#     name = input()
#     n = int(input().strip())
#     cost = int(input().strip())
#
#     p1 = Movie(name, n, cost)
#     print(p1)


#
# class comp:
#
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def add(self, other):
#         r = self.real + other.real
#         i = self.imag + other.imag
#         print(f'Sum of the two Complex numbers: {r} + {i}i')
#
#     def sub(self, other):
#         r = self.real - other.real
#         i = self.imag - other.imag
#         print(f'Subtraction of the two Complex numbers: {r} + {i}i')
#
#
# x = comp(2, 2)
# y = comp(3, 6)
# x.add(y)
# # Sum of the two Complex numbers: 4+6i
# x.sub(y)
# # Subtraction of the two Complex numbers: -2-2i

# print(10 + ( 1 / 0))

# print(36 + '20')
# try:
#     a = pow(2, 4)
#     print("Value of 'a' :", a)
#     b = pow(2, 'hello')   # results in exception
#     print("Value of 'b' :", b)
# except TypeError as e:
#     print('oops!!!')
# print('Out of try ... except.')

#
# def Handle_Exc1():
#     # Write your code here
#     a = int(input())
#     b = int(input())
#     c = a+b
#     print(c)
#     if a > 150 or b < 100:
#         raise ValueError("Input integers value out of range.")
#     elif c > 400:
#         raise ValueError("Their sum is out of range")
#     else:
#         raise ValueError("All in range")
#
#
# if __name__ == '__main__':
#     try:
#         Handle_Exc1()
#     except ValueError as exp:
#         print(exp)

def FORLoop():
    # Write your code here
    n = int(input())



if __name__ == '__main__':
    try:
        d = FORLoop()
        print(type(d))
        print(next(d))

    except StopIteration:
        print('Stop Iteration : No Next Element to fetch')

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'FORLoop' function below.
#

def FORLoop():
    # Write your code here

    n = int(input())
    print(n)
    lst = []

    for i in range(0, n):
        ele = int(input())
        lst.append(ele)  # adding the element
    print(lst)


if __name__ == '__main__':
    try:
        d = FORLoop()
        print(type(d))
        print(next(d))

    except StopIteration:
        print('Stop Iteration : No Next Element to fetch')

