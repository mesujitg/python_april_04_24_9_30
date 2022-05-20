# class & object
'''
class Student
{
    private string name;
    private string roll_no;


    public void register(){}

    public void login(){}
}

class Dog:
    height = ''
    breed = ''
    color = ''

    def makesound():
        pass
    
    def moves():
        pass



class Student:
    name = ''
    roll_no = ''
    phone = ''
    email = ''
    address = ''
    dob = ''
    gender = ''
    course = ''
    semester = 1

    # CRUD

    def addStudent(): 
        pass

    def selectStudent():
        pass

    def updateStudent():
        pass

    def deleteStudent():
        pass

    def pay():
        pass
'''

students = []

class Student:
    # __name = ''
    # __address = ''
    # __email = ''
    # __course = ''
    # __institute = ''

    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__email = ''
        self.__course = ''
        self.__institute = 'Broadway Infosys'

    # setter
    def setValues(self, n, a, e, c):
        self.__name = n
        self.__address = a
        self.__email = e
        self.__course = c

    def setName(self, n):
        if self.__name.isalpha():
            self.__name = n

    def setAddress(self, a):
        self.__address = a

    def setEmail(self, e):
        self.__email = e

    def setCourse(self, c):
        self.__course = c

    # getter
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def addStudent(self):
        students.append({'name': self.__name, 'address': self.__address, 
                        'email': self.__email, 'course': self.__course})

    def showStudents(self):
        for s in students:
            print(students.index(s)+1, '.', s['name'], s['address'], s['email'], s['course'])

    def updateStudent(self, index):
        students[index]['name'] = self.__name
        students[index]['address'] = self.__address
        students[index]['email'] = self.__email
        students[index]['course'] = self.__course

    def deleteStudent(self, index):
        students.pop(index)


# s = Student()

def use():
    option = input('a: Add Student b: View Students c: Update Student d: Delete Student')
    
    global s
    if option == 'a':
        n = input('Enter Name')
        a= input('Enter Address')
        e = input('Enter Email')
        c = input('Enter Course')

        # s.setName(n)
        # s.setAddress(a)
        # s.setEmail(e)
        # s.setCourse(c)
        # s.setValues(n, a, e, c)

        s = Student(n, a, e, c)
        s.addStudent()
    
    elif option == 'b':
        s = Student()
        s.showStudents()

    elif option == 'd':
        index = int(input('Enter SN'))
        s.deleteStudent(index-1)

    elif option == 'c':
        index = int(input('Enter SN'))
        n = input('Enter Name')
        a= input('Enter Address')
        e = input('Enter Email')
        c = input('Enter Course')

        # s.setName(n)
        # s.setAddress(a)
        # s.setEmail(e)
        # s.setCourse(c)
        s = Student(n, a, e, c)
        # s.setValues(n, a, e, c)
        s.updateStudent(index-1)

    use()


use()

