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


# encapsulation example starts
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


# use()

# encapsulation example ends

'''
class User:
    name = ''
    address = ''
    email = ''
    mobile = ''
    username = ''
    password = ''
    role = ''

    def login():
        pass


class Student(User):
    course = ''

    def add_student():
        pass



class Staff(User):
    salary = ''
    shift = ''
    type = ''
    department = ''

    def add_staff():
        pass



def add(a, b):
    return a+b


def add(a, b, c):
    return a+b+c

'''




# polymorphism 
'''
class Animal:
    height = ''
    breed = ''
    color = ''

    def moves(self):
        print('It walks')

    def makesound(self):
        print('It Shouts')


class Dog(Animal):

    def makesound(self):
        print('Dog Barks')


class Cat(Animal):

    def makesound(self):
        print('Cat Meows')


class Crocodile(Animal):

    def makesound(self):
        print('Crocodile Cry')
    
    def moves(self):
        print('Crocodile crawls')

d = Dog()
d.moves()

c = Cat()
c.moves()

cr = Crocodile()
cr.moves()
'''
from abc import ABC, abstractmethod
from math import sqrt

class Shape(ABC):
    def __init__(self, name, n):
        self.name = name
        self.no_of_sides = n

    # name = ''
    # no_of_sides = 0

    # def setCommonValues(self, name, n):
    #     self.name = name
    #     self.no_of_sides = n

    def get_info(self):
        print('Shape: ', self.name)
        print('No. of Sides: ', self.no_of_sides)

    def get_volume(self):
        return 0

    @abstractmethod
    def get_area(self):
        pass


class Triangle(Shape):
    def __init__(self, b, h, name, n):
        self.base = b
        self.height = h
        super().__init__(name, n)

    def get_area(self):
        return 1/2 * (self.base * self.height)

    def get_perimeter(self):
        pass

    @staticmethod
    def get_area_by_sides(a, b, c):
        s = a+b+c
        return sqrt(s * (s-a) * (s-b) * (s-c))

    @classmethod
    def get_triangle(cls, l, b, name, n):
        return cls(l, b, name, n)


t = Triangle(10, 20, 'Triangle', 3)
print(t.get_area_by_sides(5, 10, 15))
t1 = Triangle.get_triangle(10, 10, 'Equilateral Trianlge', 3)
t2 = Triangle.get_triangle(10, 5, 'Right Angled Trianlge', 3)
t3 = Triangle.get_triangle(10, 5, 'Isoceles Trianlge', 3)
print(t1.name)
print(t2.name)
print(t3.name)


class Rectangle(Shape):
    def __init__(self, l, b, name, n):
        self.length = l
        self.breadth = b
        super().__init__(name, n)

    def get_area(self):
        return self.length * self.breadth



class Square(Shape):
    def __init__(self, l, name, n):
        self.length = l
        super().__init__(name, n)

    def get_area(self):
        return self.length**2


class Circle(Shape):
    def __init__(self, r, name, n):
        self.radius = r
        super().__init__(name, n)

    def get_area(self):
        return (3.14 * self.radius**2)


class Cube(Shape):
    def __init__(self, l, name, n):
        self.length = l
        super().__init__(name, n)

    def get_area(self):
        return 6 * self.length**2

    def get_volume(self):
        return self.length**3

# t = Triangle(10, 5, 'Triangle', 3)
# # t.setCommonValues('Triangle', 3)
# # t.setValues(10, 5)
# t.get_info()
# print('Area of given Triangle is: ', t.get_area())

# s = Square(10, 'Square', 4)
# c = Circle(5, 'Circle', 0)
# s.get_info()
# print('Area of given Square is: ', s.get_area())

# c.get_info()
# print('Area of given Circle is: ', c.get_area())


class Calculate:
    @staticmethod
    def add(a, b, c=0):
        return a + b + c


# c = Calculate()
# print(c.add(10, 25))
# print(c.add(10, 25, 35))




