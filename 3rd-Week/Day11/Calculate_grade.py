

#This Function calulate the letter grade based on the given score

def Calculate_grade(score):
    """"This Function calulate the letter grade based on the given score"""
    if 100>= score >= 0 :
        if score >= 90 :
            return ("Your Score Is --> A")
        elif score >= 80 :
            return ("Your Score Is --> B")
        elif score >= 70 :
            return ("Your Score Is --> C")
        elif score >= 60 :
            return ("Your Score Is --> D")
        else:
            return ("Your Score Is --> F")
    else:
     #print("Enter a score between 100 and 0 please")
     return ("Enter a score between 100 and 0 please")
#------Calling the function------

score = int(input("Enter Score:  "))
print(Calculate_grade(score))
print(Calculate_grade.__doc__)