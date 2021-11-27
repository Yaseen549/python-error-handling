# Creating variables
x = 5
y = "John"
print(x)
print(y)

# reassign variables
x = 4           # x is int
x = "Sally"     # x is str now
print(x)

# Casting variables
x = str(3)
y = int(3)
z = float(3)

# Get the type
# type is used to print type of variables
print(x, y, z, type(x), type(y), type(z))

# Single or double quote
x = 'Yaseen'
y = "Yaseen"
print(x, y)

# Case - sensitive
a = 4
A = "Sally"
# A will not overwrite a
print(a, A)

# Pascal Case
MyVar = "MyVar"
# -------------

My_Var = "My_Var"
_My_Var = "_My_Var"

MYVAR = "MYVAR"

# Camel Case
myVar = "myVar"
# -----------

# Snake Case
my_var = "my_var"
_my_var = "_my_var"
# ---------------

# Variable Names
myvar = "myvar"
myvar2 = "myvar2"

print(myVar, myvar2, my_var, _my_var, myVar, MYVAR, MyVar, My_Var, _My_Var)

# Python - Assign multiple values
# Assign multiple values

x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# Assign one value to multiple
x = y = z = "Orange"
print(x + " " + y, z)

# Unpack a collection
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x, y, z)

# Python Output Variables
# Output variables
x = "Awesome"
print("Python is " + x)

# Example
x = "Python is "
y = "awesome"
z = x+y
print(z)

# Example 2
x = 5
y = 10
print(x+y)

# Python - Global Variable
# Global Variable
x = "Excellent"

def myfunc():
    print("Python is " + x)
myfunc()

print("Python is " + x)

