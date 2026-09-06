
#Lab 1

class Ticket:
    def __init__(self , name , status = "open"):
        self.name = name 
        self.status = status

    def newStatus(self , status):
        self.status = status

myTicket1 = Ticket("1000" , "In-Progressed")
myTicket2 = Ticket("1001" , "Pending")


print(myTicket1.status)
print(myTicket2.status)

print(f"Ticket ID : {myTicket2.name} is {myTicket2.status}")

#Lab2 

class Greeter :
    def __init__(self , message):
        self.message = message

    def greet(self , user ):
        self.user = user 

        return(f"Hello {user} , {self.message}")

myGreeter = Greeter("Welcome to Tuwaiq")
mymsg = myGreeter.greet("Ymam")

print(mymsg)

#Lab 3 

class Welcome:
    def __init__(self , name):
        self.name = name 


    def welcome(self):
        print(f"weclcome {self.name}")
    #return (f"weclcome {self.name}")
students = [
    Welcome("Sara"),
    Welcome("Ymam"),
    Welcome("Nouf"),
    Welcome("Yousef")
]  

for student in students:
   student.welcome()
   #print() student.welcome()) 

#Lab 4 
from pathlib import Path 

# path = Path("Home") / "students" / "students.txt"
# # path.parent.mkdir(parents = True , exit_ok=True)

# print(path.is_dir())
# print(path.suffix)
# print(path.name)
# print(path.is_file())


# path.write_text("welcome to class" , encoding = "utf-8")


#Lab 5 
class Student:

   __enrolled = True #
#    _enrolled2 = True

   def __init__(self , name):
     self.name = name 
     self.score = [] 

   def add_score(self , score):
        if score <0 or score > 100:
            raise ValueError("score must be between 0 and 100")
        self.score.append(score)

   @property
   def average(self):
         if not self.score:
             return 0
         else:
             return sum(self.score) / len(self.score)
   @property
   def enrolled(self):
           return self.__enrolled  

         
   @enrolled.setter     
   #setter
   def enrolled(self , status):
       self.__enrolled = status

       #getter
  

    
student = Student("Ymam")
student.add_score(80)
student.add_score(90)
student.add_score(100)

print(student.average())
print(student.score)

print(student.__enrolled) #
# print(student._enrolled2)

print(student._Student__enrolled) #

student.setEnrollment(False)
print(student.getEnrollment())


class Food:
    def __init__(self , name):
        self.name = name

    def showName (self):
        return self.name

class Fruites(Food):
   
    def __init__(self,name, cal):
        super().__init__(name)
        self.cal = cal

    @staticmethod
    def strName(newName):
        return newName.strip()
           
myFruite = Fruites("Apple" , 200)
print(myFruite.showName()) 

print(myFruite.strName("  Fa  "))