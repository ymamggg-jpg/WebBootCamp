#Lab 1----------------------
age = 21
if age >= 18 and age <= 60:
    print("welcome")
print("code complete")

#or 

if 18 <= age <= 55:
   print("welcome")
print("code complete")

#Lab 2----------------------

temperator = 31
if temperator >= 35:
    print("its hot outside")
else:
    print("cool")
#Lab 3----------------------

score = 84

if score >= 90:
 print("A")
elif score >= 80:
   print("B")
elif score >= 70:
   print("C")
else:
   print("you need to improve")

#Lab 4----------------------

is_active =True
is_verified= True
role = "editor"
is_blocked = False

if is_active and is_verified:
   print("Account is ready")

if role == "admin" or role == "editor":
   print("user can edit")

if not is_blocked:
   print("user is not blocked")

else:
   print ("sign up please")

#Lab 5----------------------

account_active = True
has_permission = False

if account_active:
   if has_permission:
      print("Acces Granted")
   else:
      print (" acces denied")
else:
   print ("account is not active")

#Lab 6----------------------

name = "Ymam"
cart = []
balance = 0

if name:
   print ("has a value")

if not cart:
   print ("your cart is empty")
print(bool(balance))

#Lab 7----------------------

name = input("please enter your first name").strip()

if not name:
   print("please enter a name")
elif not name.replace(" ","").isalpha():
   print("name must contain letters")
else:
   print (f"Valid name{name}")

print (name.replace(" ",""))

#Lab 8----------------------

age_text = input(print("enter your age")).strip

if age_text.isdigit():
   age = int(age_text)
   print(f"you will be {age + 5} in 5 years")
else:
   print("enter a number")

#Lab 9----------------------

is_score_valid = False
score_text = input("enter a number between 0 and 100")

if score_text.isdigit():
   score_x = int(score_text)

   if score_x >= 0 and score_x <= 100 :
      print("Valid score")
      is_score_valid = True
   else:
      print("score is invaild")
else:
   print("please enter a number")

#Lab 10----------------------   

memebrship = ["Admin", "Editor","Viewer"]

current_membership = input("enter your membership").strip().lower()

if current_membership.title() in memebrship:
 print("you're allowed to view the contecnt")
 print(current_membership)
else:
   print("please contact the admin")
   print(current_membership)

#Lab 11----------------------  

commands = input("please enter a command (start , stop , status )").strip().lower()

match command:
   case "start":
      print(" starting system....👌")
   case "stop":
      print("Stopping the system....")
   case "status":
      print("system is up and running :) ")
   case _:
      print("please enter a proper command")


      
      


