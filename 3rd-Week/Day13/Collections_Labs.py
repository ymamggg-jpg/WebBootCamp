import math

# ==================== Lab 1: Loops in collections ====================
# List of student names
students = ["Sara", "Ymam", "Taif"]

# Print each name in the list using a normal for loop
for student in students:
    print(student)

# enumerate returns (index, value) pairs for each item in the list
for iterable in enumerate(students):
    print(iterable)

# Create an enumerate object and use next() to get only the first item from it
iterable = enumerate(students)
print(next(iterable))


# ==================== Lab 2: Data Types (Collections) ====================
# Set: a collection of unique, unordered items
set_col = {"Ali", "Nasser", "Sara"}

# Tuple: an immutable (unchangeable) ordered collection
tuple_col = (11, 33, 99, 10, 43)

# Dictionary: key-value pairs
dict_col = {"name": "Abdullah", "age": 22, "has_car": True}

# List: an ordered, mutable (changeable) collection
list_col = ["ABC", 333, (13, 43)]

# Print the type of each value inside the dictionary
for c in dict_col.values():
    print(type(c))

# Print the contents of each collection
print(set_col)
print(tuple_col)
print(dict_col)
print(list_col)

# Print the type of each collection
print(type(set_col))
print(type(tuple_col))
print(type(dict_col))
print(type(list_col))


# ==================== Lab 3: Indexing and Slicing ====================
cars = ["BMW", "GMC", "Porsche", "Merc", "Geely"]

print(cars[3])          # The element at index 3
print(cars[-1])         # The last element in the list
print(cars[-1::-1])     # Reverse the entire list


# ==================== Lab 4: Modifying a List (append, insert, pop) ====================
tasks = ["Read Email", "Open ticket"]

tasks[0] = "Login"                     # Update the first element
tasks.append("Get coffee")             # Add an element to the end of the list
tasks.insert(0, "Get breakfast")       # Add an element to the start of the list

tasks.pop(3)        # Remove the element at index 3
print(tasks)


# ==================== Lab 5: Math Functions and the math Library ====================
num = [11, 22, 33, 44, 55, 66]

print(sum(num))                  # Sum of all numbers
print(len(num))                  # Number of elements in the list
print(max(num))                  # Largest value
print(min(num))                  # Smallest value
print(math.sqrt(max(num)))       # Square root of the largest value
print(math.__doc__)              # Documentation string of the math module
print(num)
print(num.pop(2))                # Remove the element at index 2 and return its value
print(sorted(num, reverse=True)) # Sort the list in descending order


# ==================== Lab 7: Set Operations ====================
skills = {"Python", "Django", "FastAPI", "Java"}

skills.add("CSS")        # Add a new element
skills.add("HTML")       # Add a new element
skills.discard("Java")   # Remove an element (unlike set.remove(), it won't raise an error if missing)
print(skills)