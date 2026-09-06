
#Lap 1 =====================================================

def greet():
    print("Welcome to python")

greet()


#Lap 2 =====================================================

def show_menu():
    print("1- Coffe")
    print("2- Tea")
    print("3- Ginger")

show_menu()
print("Outside the call")
show_menu()


#Lap 3 =====================================================

def unknownScope():
    print("Line 1 ")
    def _():
    #def gotofunc():
        print("From within the GOTO ")

    print("Where's line 2")
    _()
    print("i'm up here")



#Lap 4 =====================================================

def greet_student(name):

    print("welcome {name}")

greet_student("Sara")
greet_student("Taif")


#Lap 5 =====================================================

def show_booking(desination = "Riyadh" , nights = "1"):
                  #default values
   
    if nights.isdigit():
        nn= int(nights)
    print(f"You're travling to {desination}, and will stay for {nights} nights")

show_booking("Jeddah" , "3" )
#show_booking("Doha" , 4 )
show_booking()

#Lap 6 =====================================================

def getVAT(total , rate = 0.15):


    """This function will get the total with VAT added to it and returen it, and return the sum """
    subtotal = total + (total * rate)
    return subtotal

print(getVAT(154))
print(154 , 0.05)
print(getVAT.__doc__)
help(getVAT)
  

#Lap 7 =====================================================


#Lap 8 =====================================================


#Lap 9 =====================================================


#Lap 10 =====================================================


#Lap 11 =====================================================


#Lap 12 =====================================================