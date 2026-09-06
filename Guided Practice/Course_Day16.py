
class Student:
    def __init__(self , name ,score = [] ):
        self.name = name
        self.score = score

    def add_score(self , score):
            if 0 <= score <= 100:
                self.score.append(score)

    def average (self):
        if not self.score:
             return 0
        
        return sum(self.score) / len(self.score)
    def display (self):
                 return f"Student's name: {self.name} ,The scores are: {self.score} and the average equal = {self.average()} ,"

    



class Course:
     def __init__(self, course_name ,students = []):
          self.course_name = course_name
          self.students = students

     def add_student (self , student):
          self.students.append(student)

    

     def display_all (self):
          for student in self.students:
               print(f"{student.display()} In course {self.course_name}")


course = Course("Python")
student1 = Student ("Ymam" , [99 , 94 , 81])
student2 = Student("Sara")
student2.add_score(85)
student2.add_score(77)


course.add_student(student1)
course.add_student(student2)
# course.add_student(["Lina" , [99 , 100 , 71]])

course.display_all()

course2 = Course("Java")
student2_1 = Student("Nouf" , [90 , 89 , 99])
student2_1 = Student ("Layan" , [91 , 82 , 90])

course2.add_student(student2_1)
course2.add_student(student2_1)
course2.display_all()