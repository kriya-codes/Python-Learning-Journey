# A list stores multiple values in a single variable.

numbers=[10, 20, 30, 40, 50, 60, 70]
print(numbers)

student=["Alice", 20, 9.2, True]  # can store different datatypes as well.
print(student)

# Accessing list elements:-
# Python starts counting list positions from 0, not 1.

fruits=["Apple", "Banana", "Guava", "Mango", "Orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# Above we've learned how to access individual elements using indexes. 
# Now let's learn how to access multiple elements at once.
# For above two list:
print(numbers[1:3])
print(fruits[2:6])

# It is know as slicing. 
# The syntsx is : list_name[start:stop] 
# where, start — the index where slicing begins (included). 
#        stop — the index where slicing ends (excluded).

# More examples:
print(numbers[:4]) # starts from the beginning.
print(numbers[3:]) # continues till end.
print(numbers[:])  # copies the whole list into a new list.

# Slicing with a step:
# The syntsx is : list_name[start:stop:step]

print(numbers[::2])  # takes every second element, starting at index 0.
print(numbers[1::2]) # takes every second element, starting at index 1.
print(numbers[::-1]) # reverses the list.

# Adding Elements to a Python List.
# We'll learn three important methods: append(), insert(), and extend(). They all add elements, but they work differently.

# 1. append() — Add one element at the end
veggies=["Potato", "Onion", "Tomato"]
veggies.append("Chillis") # adds its argument as a single element
print(veggies)

veggies.append(["Chillis, Carrot"])
print(veggies) # becomes one nested list element, not two separate elements.

# 2. insert() — Add an element at a specific position
veggies.insert(1, "Peas") # insert(index, value)
print(veggies)

# 3. extend() — Add multiple elements
vegetable=["Potato", "Onion", "Tomato"]
vegetable.extend(["Chillis, Carrot"])
print(vegetable)

# Removing Elements from a List.
# There are three important ways to remove elements: remove(), pop(), and del.

# 1. remove() — Remove a specific value
veggies.remove("Chillis")
print(veggies)

# 2. pop() — Remove using an index
veggies.pop(4) # without index it removes last element
print(veggies)

# 3. del — Delete an element or a range (it's a Keyword of Python)
del veggies[1]
print(veggies)

#====================================Some Maths programs on list==============================
# Find the sum of number_list:
num=[10, 15, 20, 35, 5]
def Sum(sum):
    sum=0
    for i in num:
        sum = i + sum
    print("Sum of Number_list:", sum) 




