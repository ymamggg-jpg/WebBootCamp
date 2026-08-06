#values can be truthy or falsy

name = ""
item = []
result = None
count = 0

bool(name)   #false
bool(item)   #false
bool(result) #false
bool(count)  #false

#test methods support basic validation

isdigit () #checks if all characters in the string are digits
isalpha ()#checks if all characters in the string are alphabetic
isupper ()#checks if all characters in the string are uppercase
islower ()#checks if all characters in the string are lowercase
isalnum ()#checks if all characters in the string are alphanumeric
isascii ()#checks if all characters in the string are ASCII
isprintable ()#checks if all characters in the string are printable
isidentifier ()#checks if the string is a valid identifier
isdecimal ()#checks if all characters in the string are decimal
isnumeric ()#checks if all characters in the string are numeric
isfinite ()#checks if the number is finite
isinf ()#checks if the number is infinite
isnan ()#checks if the number is not a number

