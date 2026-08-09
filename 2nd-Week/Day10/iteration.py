
#Lap 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for attempts in range (5):
    print(f"Attempts: {attempts+ 1 }") 

#Lap 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for num in range (2 , 11 , 2): #double steps
    print(num)

#Lap 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for secondsToLaunch in range(10 , 0 , -1):
    print(f"T-: {secondsToLaunch}")

#Lap 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

course = "Python"

for letter in course:
    print(letter)

#Lap 5 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

students = ["Ymam" , "Sara" , "Ali"]

for student in students :
    print (f"progressing student is : {student}")

#Lap 6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for number in range(1 , 11):
    if number % 2 == 0 :
        print(f"{number}  is even")
    else:
        print(f"{number}  is odd")

#Lap 7 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

numbers = [4 , 5 ,9 , 8 , 2]
even_number = 0

for num in numbers:
    if num % 2 == 0:
     even_number += 1

print(f"Total even numbers is: {num}")


#Lap 8 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

prices = [24 , 44 , 62 , 15]
total = 0 

for price in prices:
    total += price

print(f" Your total is: {total} VAT: {total * (15/100)}")
                                  #       *1.15:.2f}") #two decimal points

#Lap 9 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

count = 0

while count <= 5:
 count += 1
 print(f"count... {count}")
print("Loop completed")

#Lap 10 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

message = print("please enter your age: ")
age_text = input(message).strip()

while not age_text.isdigit:
   age_text = input(message).strip()

age = int(age_text)
print(f"you are : {age}")

#Lap 11 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

password = ""
password = input("please enter your password")

while password != "Python123" :
   
   password = input("Incorrect Password, try again: ")
print ("Access Granted!")

#Lap 12 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for score in [80 , 55 ,45 ,90]:
   if score < 50:
      pass
   print(f"If passed the {score}")
#-----------------------------------
for score in [80 , 55 ,45 ,90]:
   if score < 50:
      continue
   print(f"If did not skip {score}")
#-----------------------------------
for badscore in [80 , 55 ,45 ,90]:
   if badscore < 50:
      break
   print(f"We saw: {badscore}")

#Lap 13 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for row in range(1 , 4):
   for column in range(1 , 4):
     # print(f"Row: {range} , Column {column}")
     print(f"{row} X {column} = {row * column}")
