# f = open('', 'r')
# ...
# f.close()
#
# in questo modo se si verifica un problema che fa terminare il programma, il file non viene chiuso

import datetime

class Student:
    def __init__(self, name, surname, birthYear):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear

    def show(self):
        print(f"I'm {self.name} {self.surname}, {self.getAge()} years old")

    def getAge(self):
        currentYear = datetime.date.today().year
        return int(currentYear) - self.birthYear
    

if __name__=="__main__":
    str = ''
    with open('/Users/francescafornasier/github/Programming_for_IoT_Applications/es01_2.txt', 'r') as f:
        str = f.read()
    str_list = str.split(',')
    name = str_list[0]
    surname = str_list[1]
    birthYear = int(str_list[2])

    s1 = Student(name, surname, birthYear)

    s1.show()