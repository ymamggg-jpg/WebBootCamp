# Lab1&2
# create , rename , reassign variables
# following python naming conventions

Student_name = "Ymam"
Student_age = 21
course = "Web development bootcamp"
registered = True
MAX_CLASS_SIZE = 25

print(f"""
welcome {Student_name} to {course}
you are {Student_age} 
registration status: {registered}
""")


#Lap 3
student_name , student_age , course , registered , MAX_CLASS_SIZE = "Ymam" , 21 , "Web development bootcamp" , True , 25

print (type(student_name))
print (type(student_age))
print (type(course))
print (type(registered))
print (type(MAX_CLASS_SIZE))

print(isinstance(student_name , str))
print(isinstance(student_age , int))
print(isinstance(course , str))
print(isinstance(registered , bool))
print(isinstance(MAX_CLASS_SIZE , int))

#age = int(input("Enter your age: "))
#
#if (isinstance(age , str)):
#    print(f"your age is {age}")
#else:
#    print("you are", age + 5 ,"years old in 5 years time")

teacher_name = "Faisal"
print(teacher_name)

index = int(input("select an index "))

if (index < len(teacher_name)):
  print(teacher_name[index])

else:
    print("index out of range")

print(type(len(teacher_name)))






