


#  Data: list of dictionaries ====================
# Each student is a dictionary containing:
# - a tuple of scores (immutable)
# - a set of skills (unique, unordered values)
Students = [
    {"name": "Ymam", "scores": (94, 90, 81), "skills": {"Python", "Java", "HTML"}},
    {"name": "Sara", "scores": (99, 88, 71), "skills": {"Java", "C++", "CSS"}},
    {"name": "Ali", "scores": (81, 90, 79), "skills": {"Dart", "CSS", "Git"}}
]

# The lines below don't work because Students is a list, not a dictionary,
# so you can't access "skills" directly on it — you must loop through each student first.
# Students["skills"].add("SQL ")
# Students["skills"].add("python")

#  Add a skill to every student ====================
for student in Students:
    student["skills"].add("SQL")

# The block below is an earlier (broken) attempt at computing the average:
# - unpacking "score, student in Students" is wrong since each item is a single dictionary
# - the print statement was also mis-indented outside the loop
# for student in Students:
# #    for score, student in Students:
#     Average_scores= sum(student["scores"]) / len(student["scores"])

# print(f"Average: {Average_scores:.2f}")

#  Print each student's info ====================
for student in Students:
    Average_scores = sum(student["scores"]) / len(student["scores"])   # average of the scores tuple
    print(f"Name : {student['name']}")
    print(f"Average: {Average_scores:.2f}")
    print(f"skills: {student['skills']}")
