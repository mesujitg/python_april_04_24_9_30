# try:
#     file = open('../files/userss.txt', 'a')
#     file.write('text goes here...')
#     # data = file.readlines()
#     # print(data)
# except Exception as e:
#     print('Invalid file name: ', e)

# xml excel csv json
import csv, json, xml

file = open('../files/users.csv', 'w')
csv.writer(file, ['krishna', 'ktm', 'krish@email.com'])

filer = open('../files/users.csv', 'r')
data = csv.reader(filer)
print(type(data))
for d in data:
    print(d)
