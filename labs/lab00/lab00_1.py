import datetime

class Student:
    def __init__(self, name, surname, birthYear):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear

    def getAge(self):
        currentYear = int(datetime.date.year)
        return currentYear - self.birthYear

    def show(self):
        print(f"I'm {self.name} {self.surname}, {self.getAge()} years old")


if __name__=="__main__":
    name = input('Name:')
    surname = input('Surname:')
    birthYear = int(input('Birthyear:'))
    s1 = Student(name, surname, birthYear)

    s1.show();