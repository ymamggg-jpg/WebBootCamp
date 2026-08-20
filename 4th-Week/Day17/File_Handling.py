from pathlib import Path

# ####################################################
#  Building paths with pathlib ====================
# The "/" operator joins path parts, working correctly on any OS
data_file = Path("data") / "students.txt"

print(data_file)          # data/students.txt
print(data_file.name)     # students.txt -> the filename with extension
print(data_file.suffix)   # .txt -> just the extension


# #################################################### 
# Creating a directory & checking existence ====================
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)   # create the folder if it doesn't already exist
                                 # (exist_ok=True avoids an error if it's already there)

data_file = data_dir / "studends.txt"

print(data_dir.is_dir())    # True -> confirms "data" is a directory
print(data_file.exists())   # False -> this file hasn't been created yet


# ==================== File open modes ====================
# "r" read an existing file
# "w" write and replace content (overwrites the file)
# "a" append after existing content
# "x" create only when the file doesn't already exist (errors if it does)

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("New note\n")   # "with" automatically closes the file afterward


# #################################################### 
# Reading a file with pathlib's .open() ====================
path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(file.close)   # NOTE: this prints the *method itself* (e.g. <built-in method close...>),
                     # not whether the file is closed. To check that, use file.closed instead.


# #################################################### 
# Two equivalent ways to read a file ====================
path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    text = file.read()

# .read_text() is a shortcut that opens, reads, and closes the file for you
same_text = path.read_text(encoding="utf-8")

print(text == same_text)   # True -> both approaches read identical content


# #################################################### 
# Reading a file line by line ====================
path = Path("students.txt")

with path.open("r", encoding="utf-8") as file:
    for line in file:            # iterating over a file object yields one line at a time
        name = line.strip()      # remove the trailing newline (and extra whitespace)
        if name:                 # skip empty lines
            print(name)


# ####################################################
#  Writing to a file (overwrite mode) ====================
path = Path("students.txt")

with path.open("w", encoding="utf-8") as file:
    count = file.write("Sara\nAli\n")   # write() returns the number of characters written

print(count)


# #################################################### 
# Appending to a log file ====================
path = Path("activity.log")

with path.open("a", encoding="utf-8") as file:
    file.write("student enrolled: Sara\n")

print("Activity saved")


# #################################################### 
# Writing a whole file at once (with non-English text) ====================
names = ["sara", "نورة", "Ali"]
text = "\n".join(names) + "\n"

# .write_text() is a shortcut that opens, writes, and closes the file for you
Path("students.txt").write_text(
    text,
    encoding="utf-8"   # important for correctly saving non-English characters like "نورة"
)
##############################################################
import csv 

with open("students.csv" , "w",
          encoding = "utf-8" , newline="") as file:

    writer = csv.writer(file)
   
    writer.writerow(["name" , "course"])
    writer.writerow(["Sara" , "Python"])
    writer.writerow(["Ali"  , "Django"])

#####################################################
import json

students = [
    {"name" : "Sara" , "score" : 92} , 
    {"name" : "Ali" , "score" : 81}
    
]

with open("students.json" , "w" , encoding="utf-8") as file:
    json.dump(students, file , indent = 2)

with open("students.json" , "r" , encoding= "utf-8") as file:
    loaded = json.load(file)

print(loaded[0]["name"])
##############################################################
try:
    score = int(input("Score: "))
except ValueError:
    print("Enter a whole number")
    print(ValueError)

print("Program continues")

##############################################################
from pathlib import Path

try:
    text = Path ("students.txt").read_text(
        encoding="utf-8"
    )
except FileNotFoundError:
    print("Student file not found")
except PermissionError:
    print("Student file cannot be read")

########################################################
from pathlib import Path 

path = Path("student.txt")

try:
    text = path.read_text(encoding= "utf-8")
except OSError as error:
    print("Load Failed: " , error)
else:
    print(text)
finally:
    print("Load attempt finished")

########################################################
def validate_score(score):
    if not 0 <= score <= 100 :
        raise ValueError("Score must be 0 to 100")
    return score 

try :
    score = validate_score(120)
except ValueError as error:
    print(error)

#######################################################
class StudentNotFoundError(Exception):
    pass

def find_student(name , students ):
    for student in students:
        if student["name"] == name:
         return student
    raise StudentNotFoundError(name)

students = [{"name" : "Sara"}]

try:
    print(find_student("Ali" , students))
except StudentNotFoundError as error:
    print("Missing Student: ", error)
########################################################

