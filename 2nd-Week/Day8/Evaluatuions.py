# testing operations

#Lab 1 -----------------------------------------------------------------------
#operations order

result = 10 + 5 * 2/4
result2 = (10 + 5) * 2/4
result3 = 10 + 5 * (2/4)

print(result)
print(result2)
print(result3)


#Lab 2 -----------------------------------------------------------------------
# division & remainder

total_items = 25
box_capacity = 4
full_boxes = total_items // box_capacity
remaining_items = total_items % box_capacity
print(f" you can fill up to : {full_boxes}")
print(f"remaining items : {remaining_items}")

#Lab3 -----------------------------------------------------------------------
#exponentiation

base_calc = 2 + 3 * 2 ** 2
gcalc = (2 + 3) * 2 ** 2
print(base_calc)
print(gcalc)

#lab4 -----------------------------------------------------------------------
#Logical operators

user_age = 21
has_permission = True

is_eligible =  (user_age >= 18 or has_permission) 
#is_eligible = (True if (user_age >= 18 or has_permission) else False)
#or\
#if user_age >= 18 or has_permission:
   # is_eligible = True

print(is_eligible)

#Lab 5 -----------------------------------------------------------------------
#Assignment operators

score = 10
score += 5
score *= 2 #==> score = score *2

print(f" your score is : {score}")

#Lab 6 -----------------------------------------------------------------------
#Membership operators

membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"

if current_membership in membership :
    print("You have access to the system")
else:
    print("You do not have access to the system")

#or\
if membership [0] == "Admin":
    print("You have access to the system")

#Lab 7 -----------------------------------------------------------------------
#String methods

sentence = "Python Web Development Bootcamp"

new_sentence = sentence.find("Python") #start index of the word "Python"
if "Python" in sentence:
    print("match found")

print(type(new_sentence))
print(new_sentence)

#Lab 8 -----------------------------------------------------------------------
#String slicing and reversing

message = "Python programming "

first_char = message[0]
last_char = message[-1]
print(f"first character is : {first_char} and last character is : {last_char}")


sliced_message = message[0:5] #slicing from index 0 to 5
reverse_message = message[::-1] #reversing the string
 # [start from : end on : number of steps]

print(f"your message is : {message}")
print(f"reversed message is : {reverse_message}")
print(f"sliced message is : {sliced_message}")

#Lab 9 -----------------------------------------------------------------------
#stripping whitespace from a string

my_email = "      usEr@Example.com  "
clean_email = my_email.strip() .lower() 
#removes whitespace from the beginning and end of the string 
# and converts the string to lowercase
message2 = "python bootcamp"
title_message2 = message2.title()
#Title case converts the first character of each word to
#  uppercase and the rest to lowercase
print(f"your email is : {my_email}")
print(f"your clean email is : {clean_email}")
print(f"your title message is : {title_message2}")

#Lab 10 -----------------------------------------------------------------------
#string splitting and joining

csv_text = "Apple, Banana, Cherry, Date"

split_text = csv_text.split(", ") #splits the string into a list of substrings
joined_text = "|".join(split_text) #joins the list of substrings into a single string

print(f"""your list is: {split_text}
splitted like this : {split_text}
and joined like this : {joined_text}""")

#Lab 11 -----------------------------------------------------------------------


name = "Ymam"
#Try & Accept -- when we dont trust the user input, 
# we can use try and except to handle errors gracefully
try:
    name = "A" #strings are immutable, so this will raise an error
except TypeError as e:
        print(e)


x = 10
y= 10

# x= [10]
#y= [10]

# "is" is different from "==", "is" checks if two variables point to the same object in memory, 
# while "==" checks if the values of the two variables are equal.
#if (x is y):
if x == y:
        print("x and y are equal")
else:
        print("x and y are not equal")
    
print(id(x))
print(id(y))
#Python will assume its the same value and will point to the same memory location,
# but if we change the value of x, it will point to a different memory location

#Lab 12 -----------------------------------------------------------------------
#Replace & None 

message = "Python web development bootcamp"
new_message = message.replace("Python", "Java")

print(f"Original message: {message}")
print(f"New message: {new_message}")


is_online = None #no value yet
if (is_online == None):
    print("True")

    


