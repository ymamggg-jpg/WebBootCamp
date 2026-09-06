


#Lab 1 ========================================================
course = "Web Development Bootcamp"
duration = 12

def type(course):
    print("Opss!")

print(course)
print(duration)
print(type(course))
print(globals())
#Lab 2

building = "Tuwaiq Academy"
cohort_size = 20

print(f"Welcome to {building}, class limit is {cohort_size}")
print("Tuwaiq" in building)
print("chort_size" in globals())
#print(globals())
print(globals()["building"])
print(globals()["course"])


#Lap 3 ========================================================

location = "Global"

def outter():
    location = "Outter"
    print("From {location}")
    def inner():
        location = "Inner"
        print("From {location}")
    inner()
outter()

#Lab 4 ========================================================

#location = 0

def outter():
    location = 1
    print("From {location}")
    def inner():
        nonlocal location #Allows to change the value of the outter one
        location += 2
        print("From {location}")
    inner()
outter()

#Lab 5 ========================================================

def printer():
    print("Welcome")

def desk():
    printer()

def house():
    desk()

house()

#Lab 6 ========================================================

language = "Python"

def show_lang(language):
    print(language)

show_lang("Dart")
print(language)


#Lab 7 ========================================================

rate = 0.15
def getTotal(amount):
    total = amount * rate + amount 
    return total

print (f"{getTotal(199.99):.2f}")
print (round(getTotal(199.99),2 ))

#Lab 8 ========================================================

def inspect_order(item , qty):
    subtotal = 25 * qty
print(locals())
print(locals()["subtotal"])
inspect_order("Pen" , 10)


