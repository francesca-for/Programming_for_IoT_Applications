class Student:
    def __init__(self,name,surname,birthYear):
        self.name=name
        self.surname=surname
        self.birthYear=birthYear
    def show(self):
        print(f"Hi, I'm {self.name} {self.surname}")
    
    def age(self):
        print(f'I am {2024-self.birthYear} years old')
    def save(self):
        #1 Open and close
        '''
        file_1=open('student.txt','w')
        toWrite=f'{self.name},{self.surname},{self.birthYear}'
        file_1.write(toWrite)
        file_1.close()
        '''
        #2 all at once.. no risk of file open
        with open('student.txt','w') as file_2:
            toWrite=f'{self.name},{self.surname},{self.birthYear}'
            file_2.write(toWrite)
        print('File is already close.. no risk of open file')



if __name__=='__main__':
    name=input('Enter your name: ')
    surname=input('Enter your surname: ')
    birthYear=int(input('Enter your birth year: '))
    studentA=Student(name,surname,birthYear)
    studentA.show()
    studentA.age()
    studentA.save()