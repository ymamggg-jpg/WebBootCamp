
# Looping with range()

for number in range (5): #range(5) will generate numbers from 0 to 4
 number = number +1
 print(number)

for n in range(5):
 print(n)

for n in range(1, 6): #range(1,6) will generate numbers from 1 to 5
 print(n)

for n in range(1, 10,-1 ): #range(1,10,-1) will generate numbers from 1 to 9 with a step of -1
 print(n)

# Looping through a string

word = "Python"
for character in word: # Loop through each character in the string
 print(character)

students = ["Ymam", "Ali", "Ahmed", "Sara"]
for student in students: # Loop through each student in the list
 print("welcome " , {student}) 

# loops with if

for number in range (1 , 11):
  if number % 2 == 0:
     print(f"{number} is even")


#loops with counter

count = 0

for number in range (1 , 11):
 if number % 2 == 0 :
  count += 1
print (f"Even numbers: {count}")

# Accumulators 

total = 0

for number in range(1 , 6):
  total += number

print(total) #15

#------------------


count = 1

while count <= 5:
 print(count)
 count += 1

# (for) --> Known sequence or range , use it to process items
# (while) --> Condition-controlled , u

age = input("Enter your age: ")
while not age.isdigit():
 print("age invalid")
 age = input("Enter your age: ")
age= int (age)
print(f"age accepted")


while True:
 command = input("Enter command: ")

 if command == "exit" :
  break #gonna leave the nearest iteration scope

print(f"you entered: {command}")

#---------------------

for number in range( 1 ,6 ):
 if number == 5:
  continue # go back to the condition (output :skip number 5)
print(number)

#pass





