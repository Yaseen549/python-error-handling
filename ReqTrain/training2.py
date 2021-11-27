# zfill
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(15))
print(b.zfill(22))
print(c.zfill(10))

# string methods
t = " Hello am Yaseen "
print(t.casefold())
print(t.capitalize())
print(t.center(20))
print(t.swapcase())
print(t.title())
print(t.find("e"))
print(t[2])

# format strings
quantity = 3
itemno = 567
price = 49.95
myorder = f"I want to pay {price} dollars for 100\x99 {quantity} pieces of item {itemno}."
print(myorder)

# random
import random
randomNum = random.randrange(1,10+1)
print(randomNum)
strings = "Am a String"
print(strings)
if strings[randomNum] == " ":
    print("0")
else:
    print(strings[randomNum])

a = "Hello, World!"
print(a.replace("o", "0"))
print(a.split("o"))


a = "    Hello, World! "
print(a.strip())

txt = "My world"
print(txt[:5])


txt = "hello world"
print("hello" in txt)

a = "Hello"
print(a[3])
for e in a:
    print(e)
# #
# #
a = "3"
b = 3
print(type(a))
print(type(b))
# converted "3" into 3 => means string to integer => means word to number
a = int(a)
print(a+b)


# random
import random
print(random.randrange(1,2+1))

# integer float complex
x = 1
y = 2.0
z = 1j
# #
print(x)
print(y)
print(z)
# #
print(type(x))
print(type(y))
print(type(z))
# #
a = float(x)
b = int(y)
c = complex(x)
# #
print(a)
print(b)
print(c)
# #
print(type(a))
print(type(b))
print(type(c))
# #
# x = frozenset({"apple", "banana", "cherry"})
#
# c = set("1")
# d = {1,1,2}
#
#display x:
# print(x)
#
# print(c)
# print(d)
#
#display the data type of x:
# print(type(x))
#
# print(type(c))
# print(type(d))
#
#
#
#
# x = 1
# y = 4j
# print(x,y)
#
#
#
# unpack
# fruits = ["Happy","bear","tear","zero"]
# x , y , z, a = fruits
# print(x)
# print(y)
# print(z, a)
#
#
# a = 10
# b = 5
#
# Camel casing
# print("amCamelCasing")
# print("AmPascalCasing")
# print("am_snake_casing")
#
# a,b,c = 1,2,3
# print(a+b+c)
# a = b = c = 5
# print(a,b,c)