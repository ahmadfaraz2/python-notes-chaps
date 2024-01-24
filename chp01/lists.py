
empty_list = []
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'],[1, 3, 4]]
# elements of a list can be accessed via an index
names = ["Ahmad", "Faraz", "Aayan", "Abdullah", "Saad"]
print(names[0])

print(names[3])

print(names[2])

# indices can also be negative
# print(names[-1])

print(names[-4])

print(names[-3])

# Lists are mutable, so you can change the values in a list
# names[0] = "Ali"
# print(names)
['Ali', 'Faraz', 'Aayan', 'Abdullah', 'Saad']

# It is also possible to add and remove elements from a list
names.append("Ahmad")

print(names)
['Ali', 'Faraz', 'Aayan', 'Abdullah', 'Saad', 'Ahmad']

 # Add a new element to list at a specific index

names.insert(3, "Muzamil")

print(names)
['Ali', 'Faraz', 'Aayan', 'Muzamil', 'Abdullah', 'Saad', 'Ahmad']

names.insert(1, "Zohaib")
print(names)
['Ali', 'Zohaib', 'Faraz', 'Aayan', 'Muzamil', 'Abdullah', 'Saad', 'Ahmad']

names.remove("Faraz")

print(names)
['Ali', 'Zohaib', 'Aayan', 'Muzamil', 'Abdullah', 'Saad', 'Ahmad']
# Remove the first occurence of a value with L.remove(value)

names.remove("Zohaib")

print(names)
['Ali', 'Aayan', 'Muzamil', 'Abdullah', 'Saad', 'Ahmad']



# Get the index in the list of the first item 

names.index("Ahmad")

len(names)

names.count("Ahmad")

names.sort()
print(names)
['Aayan', 'Abdullah', 'Ahmad', 'Ali', 'Muzamil', 'Saad']

names.reverse()

print(names)
['Saad', 'Muzamil', 'Ali', 'Ahmad', 'Abdullah', 'Aayan']

names.reverse()

print(names)
['Aayan', 'Abdullah', 'Ahmad', 'Ali', 'Muzamil', 'Saad']

names.pop()
'Saad'

print(names)
['Aayan', 'Abdullah', 'Ahmad', 'Ali', 'Muzamil']

# Reverse the list
a = [1, 1, 1, 2, 3, 4]
a.reverse()
# or
a[::-1]

# You can iterate over the list elements like below:
# for element in my_list:
#   print (element)