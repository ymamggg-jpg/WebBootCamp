
Students = [
    {"name" : "Ymam" , "scores": (94, 90 , 81) , "skills":{"Python" , "Java" ,"HTML"}} ,
    {"name" : "Sara" , "scores": (99 , 88,71) , "skills": {"Java" , "C++" , "CSS"}}, 
    {"name" : "Ali" , "scores": (81, 90 ,79) , "skills": {"Dart" , "CSS" , "Git"}} 
]

# Students["skills"].add("SQL ")
# Students["skills"].add("python")

for student in Students:
  student["skills"].add("SQL")
 
for student in Students:
#    for score, student in Students:
    Average_scores= sum(student["scores"]) / len(student["scores"])

 #print(f"Average: {Average_scores:.2f}")

for student in Students:
    print(f"Name : {student["name"]}")
    print(f"Average: {Average_scores:.2f}")
    print(f"skills: {student["skills"]}")
     
