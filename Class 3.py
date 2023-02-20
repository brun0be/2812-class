# from datetime import datetime
# import requests
#
# print(datetime.now())
#
# response = requests.get("http://www.github.com")
# print(response.status_code)
#
# file = open("hobbies.txt")
# for line in file.readlines():
#     print(line, end='')
#
# file = open("hobbies.txt", "a+")
# file.write("\ntorah")
# file.readlines()


# def write_name(name):
#     file = open("names.txt", "a+")
#     file.write("\n"+name)
#
#
# def read_names():
#     file = open("names.txt")
#     for line in file.readlines():
#         print(line, end='')
#
# write_name("bruno")
# write_name("sarah")
# write_name("yoav")
# read_names()

try:
    var = 1/0
except ZeroDivisionError as e:
    print(e)
except BaseException as e:
    print(e)
