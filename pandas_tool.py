import pandas

students_list = ['bigyan', 'harish', 'arpana', 'bhoomiksha', 'bigyan']
student_dict = {'name':'bigyan', 'address':'ktm', 'email':'bigyan@email.com',  'phone':9841123456}

students6 = [
    {'name':'bigyan', 'address':'ktm', 'email':'bigyan@email.com', 'mobile':9841123456},
    {'name':'bini', 'address':'lalitpur', 'email':'bini@email.com', 'mobile':9841123456},
    {'name':'bhoomiksha', 'address':'baneshwor', 'email':'bhoomi@email.com', 'mobile':9841123456},
    {'name':'harish', 'address':'ktm', 'email':'harish@email.com', 'mobile':9841123456},
    ]

students7 = {
    'name':['bigyan', 'bini', 'bhoomiksha', 'harish'],
    'address':['ktm', 'lalitpur', 'baneshwor', 'ktm'],
    'email':['bigyan@email.com', 'bini@email.com', 'bhoomi@email.com', 'harish@email.com'],
    'mobile':[9841123456, 9841123456, 9841123456, 9841123456]
}


# print(pandas.Series(students_list))
# print(pandas.Series(student_dict))

# print(pandas.DataFrame(students6))
# print(pandas.DataFrame(students7))


# file = open('files/users.json', 'r')
file = pandas.read_json('files/users.json')
print(file)

