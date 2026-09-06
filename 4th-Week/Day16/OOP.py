#  Example 1: A class is itself an object 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class Student:
    pass

print(Student)          # <class '__main__.Student'> -> the class itself
print(type(Student))    # <class 'type'> -> classes are instances of "type"


#  Example 2: Creating instances (objects) 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    pass

Student_one = Student()
Student_two = Student()

print(Student_one)
print(Student_one is Student_two)  # False -> two separate objects in memory


#  Example 3: __init__ and instance attributes
#  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = Student("Sara", 92)

print(student.name)
print(student.score)


#  Example 4: Methods and return vs print
#  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I'm {self.name}")   # Bad practice:
        # Better to use "return" instead of "print" inside a method,
        # so the caller can decide what to do with the result
        # (print it, store it, format it, etc.)

student = Student("Omar")
student.introduce()


#  Example 5: Each instance has its own attributes 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

sara = Student("Sara", 92)
omar = Student("Omar", 81)

sara.score = 95   # only changes sara's score

print(sara.score)
print(omar.score)   # unaffected

print(omar is sara)  # False -> different objects


#  Example 6: Class attributes (shared by all instances) 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    academy = "Tuwaiq Academy"   # class attribute: shared by every instance

    def __init__(self, name):
        self.name = name

sara = Student("Sara")

print(Student.academy)  # accessed through the class
print(sara.academy)     # also accessible through an instance


#  Example 7: Instance method + default object printing 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_result(self):
        print(self.name, self.score)

student = Student("Lina", 88)
student.display_result()
print(student)   # without __str__, this prints something like <__main__.Student object at 0x...>


#  Example 8: A simple counter class
#  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

counter = Counter()
counter.increment()
counter.increment()

print(counter.value)  # 2


#  Example 9: A method that returns a computed value 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height   # best practice: return instead of print

rectangle = Rectangle(5, 3)

print(rectangle.area())


#  Example 10: Validating input inside a method 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

account = BankAccount(500)
print(account.withdraw(200))
print(account.balance)


#  Example 11: __str__ for a readable print() output 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"   # if we removed __str__, print() would show
                                                # the default <Student object at 0x...> instead

student = Student("Sara", 95)
print(student)   # calls __str__ automatically


#  Example 12: Instances don't share instance attributes
#  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = Counter()
secound = Counter()

first.increment()

print(first.value)    # 1
print(secound.value)  # 0 -> unaffected, since each instance has its own "value"


#  Example 13: A list of objects
#  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello , {self.name}"

    def __str__(self):
        return f"{self.name}"

students = [
    Student("Sara"),
    Student("Omar"),
    Student("Lina")
]

print(students[0].greet())

for student in students:
    print(student.greet())


#  Example 14: Checking an object's type 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    pass

student = Student()

print(type(student))                 # <class '__main__.Student'>
print(type(student) is Student)      # True
print(isinstance(student, Student))  # True -> the recommended way to check type
                                      # (also works correctly with inheritance,
                                      # unlike "type(x) is SomeClass")


#  Example 15: "Private-ish" attributes with a leading underscore 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score   # a single leading underscore is just a NAMING CONVENTION

student = Student("Sara", 95)

print(student.name)
print(student._score)   # still accessible from outside the class,
                         # but the underscore signals "treat this as internal/private"


#  Example 16: Mutable default argument pitfall 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Student:
    def __init__(self, name, scores=[]):   # NOTE: a mutable default argument (like []) is
        self.name = name                   # a common Python bug — the SAME list object gets
        self.scores = scores               # reused across every instance that doesn't pass
                                            # its own "scores" argument. It's safer to use
                                            # "scores=None" and then do
                                            # "self.scores = scores if scores is not None else []"

    def average(self):
        return sum(self.scores) / len(self.scores)

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)

student = Student("Sara", [80, 90])   # here scores is passed explicitly, so it's safe
student.add_score(100)
print(student.name, student.average())