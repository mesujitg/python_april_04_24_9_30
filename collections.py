from operator import index


students_list = ['bigyan', 'harish', 'arpana', 'bhoomiksha', 'bigyan']
students_tuple = ('bigyan', 'harish', 'arpana', 'bhoomiksha', 'bigyan')
students_set = {'bigyan', 'harish', 'arpana', 'bhoomiksha', 'bigyan'}
student_dict = {'name':'bigyan', 'address':'ktm', 'email':'bigyan@email.com', 
                'phone':9841123456}
user = {'name':'ram', 'age':25, 'salary':50000.00, 'is_marroed':False}

# print(student_dict)
# student_dict['address'] = 'lalitpur'
# print(student_dict)
# student_dict['course'] = 'python-django'
# print(student_dict)

# for i in student_dict:
#     print(i, ': ', student_dict[i])

# print(students_list)
# print(students_tuple)
# print(students_set)
# students_set.add('Shyam')
# print(students_set)

# students_mark = [80, 85, 90, 70]
# student = ['bigyan', 'ktm', 'bigyan@email.com', 9841123456]
# user = ['ram', 25, 50000.00, False]

# for i in range(4):
#     print(student_dict[i])

# for i in students_set:
#     print(i)


# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
#         'Saturday']

# num = int(input('Enter a number'))

# if num < 0 or num > 7:
#     print('invalid')
# else:
#     print(days[num-1])


# print sum of members in a list, nums = [5, 7, 13, 2, 25, 50, 3]
# nums = [5, 7, 13, 2, 25, 50, 3]
# sum = 0
# for i in nums:
#     sum = sum + i

# print(sum)


# calculate the precentage obtained by a student from a list of 
# individual maks: marks = [70, 78, 82, 89, 67]


# print largest number in a list, nums = [5, 7, 13, 2, 25, 50, 3]
# nums = [5, 7, 13, 2, 25, 50, 3]
# largest = nums[0]
# smallest = nums[0]

# for num in nums:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num

# print("Largest Number is: ", largest)
# print("Smallest Number is: ", smallest)

'''
loop        condition1    condition2
num = 5:        X            X           largest=5 smallest=5
num = 7:      largest=7      X           smallest=5
num = 13:     largest=13     X           smallest=5
num = 2:        X          smallest=2    largest=13
num = 25:     largest=25     X           smallest=2
num = 50:     largest=50     X           smallest=2
num = 3:        X            X           largest=50 smallest=2
'''

users = [
    {'name':'bigyan', 'username':'bigyan', 'password':'12345', 'balance':125000},
    {'name':'bini', 'username':'bini', 'password':'11111', 'balance':75000},
    {'name':'bhoomiksha', 'username':'bhoomi', 'password':'54321', 'balance':100000},
    {'name':'arpana', 'username':'arpana', 'password':'22222', 'balance':90000},
    {'name':'deepak', 'username':'deepak', 'password':'deepak1', 'balance':215000},
    ]

def transaction(balance):
    option = input('Enter w for withdrawal d for deposite')
    amount = float(input('Enter amount'))
    if option == 'w':
        balance = balance - amount
    elif option == 'd':
        balance = balance + amount
    return balance


def menu_option():
    op = input('Enter t for transaction e to exit')
    # continue yourself

# un = input('Enter Username')
# pw = input('Enter Password')

# for user in users:
#     if un==user['username'] and pw==user['password']:
#         print('Welcome ', user['name'])
#         print('You balance is: ', user['balance'])
#         user['balance'] = transaction(user['balance'])
#         print('Your balance is', user['balance'])
#         break
# else:
#     print('Wrong credentials')






# users1 = {
#     'name': ['bigyan', 'bini', 'bhoomiksha', 'arpana', 'deepak'],
#     'username': ['bigyan', 'bini', 'bhoomi', 'arpana', 'deepak'],
#     'password': ['12345', '11111', '54321', '22222', 'deepak1'],
#     'balance': [125000, 75000, 100000, 90000, 215000]
# }

# un = input('Enter Username')
# pw = input('Enter Password')
# user_index = -1

# if un in users1['username']:
#     user_index = users1['username'].index(un)
#     if pw == users1['password'][user_index]:
#         pass

# for i in range(len(users1['username'])):
#     if un == users1['username'][i]:
#         user_index = i
#         if pw == users1['password'][user_index]:
#             print('Welcome ', users1['name'][user_index])
#             print('You balance is: ', users1['balance'][user_index])
#             option = input('Enter w for withdrawal d for deposite')
#             amount = float(input('Enter amount'))
#             if option == 'w':
#                 users1['balance'][user_index] = users1['balance'][user_index] - amount
#             elif option == 'd':
#                 users1['balance'][user_index] = users1['balance'][user_index] + amount
#             else:
#                 print('Invalid Selection')
#             print('Your balance is:', users1['balance'][user_index])
#         else:
#             print('Wrong credentials')
#         break
# else:
#     print('Wrong credentials')




# Calculate percentage of given students. 
# Also print the subjects of equal marks
# marks_ram = {'English': 75, 'Nepali': 65, 'Maths': 85, 'Science': 78, 
#                 'Social': 55}
# marks_shyam = {'Nepali': 70, 'English': 73, 'Maths': 85, 'Science': 81, 
#                 'Social': 55}

# total_ram = 0
# total_shyam = 0


# for i in marks_ram:
#     total_ram += marks_ram[i]
#     total_shyam += marks_shyam[i]
#     if marks_ram[i] == marks_shyam[i]:
#         print(i, ':', marks_ram[i])

# print('Ram: ', (total_ram/500) * 100, '%')
# print('Shyam: ', (total_shyam/500) * 100, '%')


# store multiple users' information(name, email, phone) to a list of dictionary
# users = [
#         {'name': 'bini', 'email': 'bini@email.com', 'phone': 9812345678},
#         {'name': 'pradeep', 'email': 'pradeep@email.com', 'phone': 9812345678},
#         {'name': 'bhoomikshya', 'email': 'bhoomi@email.com', 'phone': 9812345678},
#     ]

# ask information(name, email, phone) to a user and store it in a list 
# in the form of user dictionary. check if the data is valid using a function

import re
# global variable
users = []

def registration():
    # local variables
    name = input('Enter your name')
    email = input('Enter your email')
    phone = input('Enter your phone')

    if validate(email, phone) == '':
        users.append({'name': name, 'email': email, 'phone': phone})
        print('User registered successfully!')
        print(users)
        registration()
    else: 
        print(validate(email, phone))
        registration()


def validate(email, phone):
    regex_email = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    regex_phone = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    msg = ''
    if not re.fullmatch(regex_email, email):
        # print('Invalid Email')
        # return False
        msg += 'Invalid Email \n'
    if not re.fullmatch(regex_phone, phone):
        # print('Invalid Phone')
        # return False
        msg += 'Invalid Phone \n'

    return msg

registration()
