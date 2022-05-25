try:
    file = open('files/users.txt', 'r')
    data = file.read()
    print(data)
except:
    print('Invalid file name')
