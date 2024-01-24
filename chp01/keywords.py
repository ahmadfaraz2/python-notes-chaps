print("=========================keyword module=========================")
import keyword

# print(dir(keyword))
print(keyword.kwlist)
print("------------------Soft Keylist------------------")
print(keyword.softkwlist)

print("===========================type() function======================")

a = 1
print(type(a))

pi = 3.14
print(type(pi))

c = 'A'
print(type(c))

name = "Ahmad"
print(type(name))

q = True
print(type(q))

x = None
print(type(x))


print("===================assignement examples===================")

# "a_name" is now a name for the reference to the object "an_object"

#a_name = an_object

# You can assign multiple values to multiple variables in one line
a, b, c = 1, 2, 3
print(a, b, c)

# You can also assign a single value to several variables simultaneously.
x = y = z = 1
print(x, y, z)
