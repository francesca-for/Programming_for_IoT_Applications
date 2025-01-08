class Student:
    def __init__(self,name,surname,birthYear):
        self.name=name
        self.surname=surname
        self.birthYear=birthYear
    def show(self):
        print(f"Hi, I'm {self.name} {self.surname}")
    
    def age(self):
        print(f'I am {2024-self.birthYear} years old')

if __name__=='__main__':
    name=input('Enter your name: ')
    surname=input('Enter your surname: ')
    birthYear=int(input('Enter your birth year: '))
    studentA=Student(name,surname,birthYear)
    studentA.show()
    studentA.age()