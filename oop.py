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
    name = ''
    address = ''
    email = ''
    course = ''

    def addStudent(self):
        students.append({'name': self.name, 'address': self.address, 
                        'email': self.email, 'course': self.course})

    def showStudents(self):
        for s in students:
            print(s['name'], s['address'], s['email'], s['course'])

    def updateStudent(self, index):
        students[index]['name'] = self.name
        students[index]['address'] = self.address
        students[index]['email'] = self.email
        students[index]['course'] = self.course

    def deleteStudent(self, index):
        students.pop(index)


s = Student()

def use():
    option = input('a: Add Student b: View Students c: Update Student d: Delete Student')
    
    global s
    if option == 'a':
        n = input('Enter Name')
        a= input('Enter Address')
        e = input('Enter Email')
        c = input('Enter Course')

        s.name = n
        s.address = a
        s.email = e
        s.course = c
        s.addStudent()
    
    elif option == 'b':
        s.showStudents()

    elif option == 'd':
        index = int(input('Enter SN'))
        s.deleteStudent(index-1)

    use()


use()

