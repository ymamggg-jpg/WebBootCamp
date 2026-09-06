# ==================== Lists: basics ====================
Students = ["Sara", "Omar", "Ymam"]

print(Students)             # Print the whole list
print(Students[0])          # Print the first element
print(type(Students))       # Print the type of Students (list)

colorse = ["red", "yellow", "Blue"]
print(colorse[0])           # First element
print(colorse[-1])          # Last element
print(colorse[1])           # Second element


# ==================== Lists: updating elements ====================
tasks = ["plan", "code"]
tasks[0] = "design"         # Replace the first element


# ==================== Lists: remove, pop, sort ====================
scores = [88, 72, 95, 81]

scores.remove(72)   # Remove the value 72 (removes by value, not index)
last = scores.pop()  # Remove and return the last element
scores.sort()        # Sort the list in ascending order (in place)

print(scores)
print(last)


# ==================== Loops and enumerate ====================
students = ["sara", "Omar", "Ymam"]

# Normal loop over the list
for student in students:
    print(student)

# enumerate with unpacking: gives index and value separately
for index, student in enumerate(students):
    print(index, student)

# enumerate without unpacking: gives a (index, value) tuple
for student in enumerate(students):
    print(student)


# ==================== Matrix (commented out example) ====================
# matrix = [
#     [1 ,2 ,3]
#     [4 ,5 ,6]
# ]

# Tuples
# print(matrix[0])
# print(matrix[1][2]) #6


# ==================== Tuples ====================
# Tuple: an ordered, immutable (unchangeable) collection
location = (24.7136, 46.6753)
print(location[0])    # First value (latitude)
print(location[-1])   # Last value (longitude)

# location[0] = 25   # TypeError: tuples cannot be modified

# Tuple unpacking with * (star) to collect the remaining values into a list
student = ("Sara", 22, "Python", True, 23.1)
name, age, course, *other = student  # the star collects "leftover" values

print(name)
print(age)
print(course)


# ==================== Sets ====================
# Set: duplicate values are automatically removed
skills = {"Python", "Git", "Python"}

skills.add("Django")           # Add a new element
print(skills)
print("Git" in skills)         # Check membership
print(len(skills))             # Number of elements


# ==================== Set operations ====================
backend = {"Python", "Django", "SQL"}
frontend = {"HTML", "CSS", "JavaScript", "SQL"}

print(backend | frontend)   # Union: all elements from both sets
print(backend & frontend)   # Intersection: elements common to both sets
print(backend - frontend)   # Difference: elements only in backend


# ==================== Dictionaries: basics ====================
student = {
    "name": "Sara",
    "Age": 22,
    "course": "Pyton"
}

print(student["name"])   # Access value by key


# ==================== Dictionaries: update, get, pop ====================
student = {"name": "Sara", "score": 90}

student["score"] = 95          # Update an existing key
student["grade"] = "A"         # Add a new key

email = student.get("email", "NOT set")   # Safely get a key with a default value
grade = student.pop("grade")              # Remove a key and return its value

print(student)


# ==================== Dictionaries: looping ====================
student = {"name": "Sara", "score": 95}

# Looping over a dictionary gives you the keys by default
for key in student:
    print(key)

# .items() gives key and value together
for key, value in student.items():
    print(key, value)

# .values() gives only the values
for value in student.values():
    print(value)


# ==================== "in" checks on different collections ====================
names = ["sara", "Omar"]
skills = {"python", "Git"}
student = {"name": "Sara", "score": 95}

print(len(names))              # Number of items in the list
print("python" in skills)      # Check membership in a set
print("name" in student)       # Checking a dictionary checks its keys


# ==================== List of dictionaries ====================
students = [
    {"name": "Sara", "score": 95},
    {"name": "Omar", "score": 88}
]

# Loop over the list, then access each dictionary's keys
for student in students:
    print(student["name"], student["score"])
