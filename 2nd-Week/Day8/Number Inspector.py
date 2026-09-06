
#print (Enter a sentence ")and two numbers please: ")
print ("Enter a sentence")
print ("Enter two numbers")
       sentence = str(input())
       number1 = int(input())
       number2 = int(input())

       int total = number1 + number2
       print("The total is: " + str(total))

     csv_line = sentence
     words = csv_line.split(",")

     message = " | " .join(words)
     print(message)
