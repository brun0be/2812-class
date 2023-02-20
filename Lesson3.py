# Question 1
try:
    var = 1/0
except ZeroDivisionError as e:
    print(e)
except BaseException as e:
    print(e)
# Question 2
# Code legal try/catch/finally both can be used.
try:
    x = 1
finally:
    print("finally")
# Question 3
# Any error catch without meaningful message.
# Question 4
# The error message is not specific enough for future investigation.
# Question 5
try:
    var = 1/0
except IOError as e:
    print(e)
# I/O operations related error.
# IOError means Input/Output error. It occurs when a file, file path, or OS operation we're referencing does not exist.
except ZeroDivisionError as e:
    print(e)
# Second argument to an operation was zero.
# Question 6,7,8
def question_6 (txt):
    file = open("./words.txt", "a+")
    file.write(name)
    file.close()
    # file.write("\n"+name)
    file = open("./words.txt", "r")
    line = file.readlines()
    print(line)

name = "Bruno Berreby"+"\n"
question_6(name)
name = "מרדכי ברבי"+"\n"
question_6(name)
