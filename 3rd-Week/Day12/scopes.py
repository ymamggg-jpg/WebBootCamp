
message = "Global"

def show_message():
    message= "Local"
    print(message)

show_message() #Loacl
print(message) #Global

#LEGB is python's name lookup order
#L - Local / inside the scope
#E - Enclosing / nested func (scope inside scope)
#G - Global /
#B - Built-in

print(len("python"))

#Local Scope:

#Enclosing Scope:

def outer():
    course = "python"

    def inner ():
        print(course)

    inner()
outer()

#Global Scope:

tax_rate = 0.15

def calculate_tax(amount):
    return amount * tax_rate

print(calculate_tax(200))

#Built-in Scope:

scores = [80 , 90 , 100]

print(len(scores))
print(sum(scores))
print(type(scores))