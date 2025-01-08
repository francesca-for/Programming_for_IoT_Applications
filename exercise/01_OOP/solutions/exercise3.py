class Student:
    def __init__(self,name,surname,birthYear,student_status):
        self.name= name
        self.surname= surname
        self.birthYear= birthYear
        self.bachelor= student_status == 'b' or student_status =='B' or student_status == 'bachelor' or student_status == 'Bachelor' 
        self.master= student_status == 'm' or student_status =='M' or student_status == 'master' or student_status == 'Master'
    
    def show(self):
        print(f"Hi, I'm {self.name} {self.surname}")
    
    def age(self):
        print(f'I am {2024-self.birthYear} years old')

    def save(self):
        with open('student.txt','w') as file_2:
            toWrite=f'{self.name},{self.surname},{self.birthYear}'
            file_2.write(toWrite)
        print('File is already close.. no risk of open file')
    
    def isBachelor(self):
        if self.bachelor:
            print('The student is bachelor')
        else:
            print('The student is not bachelor')
    
    def isMaster(self):
        if self.master:
            print('The student is master')
        else:
            print('The student is not master')

if __name__=='__main__':
    name=input('Enter your name: ')
    surname=input('Enter your surname: ')
    birthYear=int(input('Enter your birth year: '))
    student_status=input('Select your level of Eductation (bachelor,master):')
    studentA=Student(name,surname,birthYear,student_status)
    studentA.show()
    studentA.age()
    studentA.save() 
    studentA.isBachelor()
    studentA.isMaster()