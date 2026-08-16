
import copy
students = [
    {"name" : "Ymam" , "score": [91 , 82 , 94]},
    {"name": "Sara" , "score": [82 , 51 , 81]},
    {"name": "Omar", "score" : [88 , 71 , 20]}

]

Students_average = [

 {"name" :student["name"] ,"average": sum (student["score"] ) / len(student["score"] )}
    #student["score"]:student
        for student in students
        # if average < 60
        # continue   
]
print(Students_average)


passing_students = [
    student
    for student in Students_average
    if student["average"] >= 60
]
print(passing_students)

student_index = {

}
