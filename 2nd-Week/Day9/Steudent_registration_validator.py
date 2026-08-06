
print("--{Student Registration Validator}--")

course_list = ["Python", "Java", "C++", "JavaScript", "HTML/CSS"]
print(course_list)
print("Please enter your details below:")



Student_name = input("Enter your name: ").strip().title
Student_score = input("Enter your score: ").isdigit()
Selected_course = input("Enter your selected course: ").strip().lower

# valid_name = Student_name.isalpha()
# valid_score = Student_score.isnumeric()
# valid_course = Selected_course.isalpha()

if Selected_course.title() in course_list:
    # if  valid_course :
       if Student_score > 0 and Student_score < 100:
            if Student_score >= 90:
             print(f"Congratulations {Student_name}! You have been accepted into the {Selected_course} course with a score of (A).")
            elif Student_score >= 80:
              print(f"Congratulations {Student_name}! You have been accepted into the {Selected_course} course with a score of (B).")
            elif Student_score >= 70: 
             print(f"Congratulations {Student_name}! You have been accepted into the {Selected_course} course with a score of (C).")
            elif Student_score >= 60:
             print(f"Congratulations {Student_name}! You have been accepted into the {Selected_course} course with a score of (D).")
            else:
             print(f"Sorry {Student_name}, you have not been accepted into the {Selected_course} course with a score of (F).")
       else:
         print("Invalid score. Please enter a score between 0 and 100.")
    # else:  
    #   print("not a valid score")                   
else:
   print(f"sorry we don't offer this course: {Selected_course}.")