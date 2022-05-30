# try:
#     file = open('../files/userss.txt', 'a')
#     file.write('text goes here...')
#     # data = file.readlines()
#     # print(data)
# except Exception as e:
#     print('Invalid file name: ', e)

# xml excel csv json
import csv, json, xml

# file = open('../files/users.csv', 'w')
# csv.writer(file, ['krishna', 'ktm', 'krish@email.com'])

file = open('../files/users.csv', 'r')
data = csv.reader(file)
# print(type(data))
for d in data:
    print(d)

filej = open('../files/users.json', 'r')
data = json.load(filej)
print(data)

# as in prev exercise
data[1]["address"] = "itahari"

print(data)

# file_w = open('../files/users.json', 'w')
# file_w.write(data)

# with open("../files/users.json", "w") as outfile:
outfile = open("../files/users.json", "w")
json.dump(data, outfile)
