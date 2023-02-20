import random

# Question 1
X = 5
Y = 6
if X < Y: print("small")
elif X > Y: print("BIG")
# Question 2
iterations = range(1, 6)
for i in iterations:
    print(f"Iteration:{i}")
# Question 3
var = random.randint(1,4)
if var == 1: print("summer")
elif var == 2: print("winter")
elif var == 3: print("fall")
elif var == 4: print("spring")
# Question 4
# a)
# b) The answer is 10
count =1
while count <11:
    print(count)
    count = count + 1
# Question 5
my_dict = {"age": 42,
           "first_letter": "B",
           "currency_quote": 0.29,
           "aboard_bool": "True",
            "appart_num": 9
           }
print(my_dict["age"])
print(my_dict["age"]+my_dict["currency_quote"])
print(my_dict.keys())
print(my_dict.values())
# Question 6
phone = input("Please enter your phone number?")
print(f"Phone Number:{phone}")
# Question 7
def print_hello():
    print("Hello")
print_hello()
def calculate():
    print(5+3.2)
calculate()
# Question 8
def print_name(name):
    print(f"Your name:{name}")
print_name("Bruno")
def divide_by_2(num):
    print(num/2)
divide_by_2(10)
# Question 9
def sum(x,y):
    return x+y
results = sum(10,10)
print(results)
def add_space(string1, string2):
    return string1+" "+string2
fullname = add_space("bruno","berreby")
print(fullname)