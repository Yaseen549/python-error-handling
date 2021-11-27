# Built-in data types

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type: 	dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview

# Getting data types
# String
x = "some words"
print(x)
print(type(x))

# int
x = 20
print(x)
print(type(x))

# float
x = 20.5
print(x)
print(type(x))

# complex
x = 1j
print(x)
print(type(x))

# list
x = ["apple","banana"]
print(x)
print(type(x))

# tuple
x = ("apple","banana")
print(x)
print(type(x))

# range
x = range(6)
print(x)
print(type(x))

# dict
x = {"name": "John"}
print(x)
print(type(x))

# set
x = {"apple","banana"}
print(x)
print(type(x))

# Frozenset
x = frozenset({"apple","banana"})
print(x)
print(type(x))

# boolean
x = True
print(x)
print(type(x))

# bytes
x = b"Hello"
print(x)
print(type(x))

# bytearray
x = bytearray(5)
print(x)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(x)
print(type(x))

print("---------------------------------")
# Setting the specific Data Type
x = str("Hello, World!")
print(x)
x = int(20)
print(x)
x = float(20.5)
print(x)
x = complex(1j)
print(x)
x = list(("apple","banana","cherry"))
print(x)
x = tuple(("apple","banana","cherry"))
print(x)
x = range(6)
print(x)
x = dict(name="John", age=36)
print(x)
x = set(("apple","banana","cherry"))
print(x)
x = frozenset(("apple","banana","cherry"))
print(x)
x = bool(5)
print(x)
x = bytes(5)
print(x)
x = bytearray(5)
print(x)
x = memoryview(bytes(5))
print(x)



