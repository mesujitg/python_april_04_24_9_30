# name = 'ram kumar sharma'
# salary = 50000.00
# age = 25
# is_married = False
# childrens = ['lab', 'kush']
# users = ['bigyan', 'bini', 'bhoomiksha', 'bini', 'arpana', 'deepak', 'bini']

# users.insert(1, 'Rahul')
# print(users)

# print(users.index('deepak'))
# print(name.index('u'))
# print(name.count('r'))
# print(name.count('ma'))
# print(users.count('bini'))

# print(users[1:])
# print(users[:1])
# print(users[2:4])
# print(type(childrens))
# print(len(childrens))
# print(round(5.5))
# print(name.isalnum())

# import math as m
from math import *
import datetime as dt
import random
import re

# students = ['ram', 'shyam', 'hari', 'krishna', 'gopal']
# random.shuffle(students)
# print(students)

# print(dt.datetime.now())

# print(factorial(5))
# print(sqrt(25))
# print(pi)
# print(floor(2.9999999))
# print(ceil(2.000000001))

# first_name = input('Enter your first name')
# last_name = input('Enter your last name')
# email = input('Enter your email')
# regex_email = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
# phone = input('Enter you phone')
# regex_phone = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

# if not first_name.isalpha():
#     print('Invalid first name')
# if not last_name.isalpha():
#     print('Invalid last name')
# if not re.fullmatch(regex_email, email):
#     print('Invalid Email')
# if not re.fullmatch(regex_phone, phone):
#     print('Invalid Phone')

'binisiku11@gmail.com'

'7 Dec 2022'
'2022-01-01'
'01-01-2022'

'9841584011'
'+977(984)(158)4011'


words = ['apple', 'orange', 'grapes', 'banana', 'pineapple']
index = 0

def show_word():
    global index
    word = words[index]
    word_list = list(word)
    random.shuffle(word_list)
    for i in word_list:
        print(i, end='')
    print()
    ans = input('Enter correct word')
    if ans == word:
        print('Correct')
        if index < len(words)-1:
            index += 1
            show_word()
        else:
            print('You have completed all the words.')
    else:
        print('Incorrect')
        show_word()

show_word()