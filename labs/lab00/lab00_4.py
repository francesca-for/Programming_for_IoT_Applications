import datetime

class Student:
    def __init__(self, name, surname, birthYear, educationLevel):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear
        self.educationLevel = educationLevel
        self.grades = []

    def show(self):
        print(f"I'm {self.name} {self.surname}, {self.getAge()} years old, {self.educationLevel} degree student")

    def getAge(self):
        currentYear = datetime.date.today().year
        return int(currentYear) - self.birthYear
    
    def isBachelor(self):
        if self.educationLevel == "Bachelor":
            return True
        else:
            return False
        
    def isMaster(self):
        if self.educationLevel == "Master":
            return True
        else:
            return False
        
    def addGrades(self, file):
        fileContent = file.read()
        gradesList = fileContent.split(',')
        for g in gradesList:
            self.grades.append(int(g))
        

if __name__=="__main__":
    str = ''
    with open('/Users/francescafornasier/github/Programming_for_IoT_Applications/es01_2.txt', 'r') as f:
        str = f.read()
    str_list = str.split(',')
    name = str_list[0]
    surname = str_list[1]
    birthYear = int(str_list[2])
    educationLevel = str_list[3]
    s1 = Student(name, surname, birthYear, educationLevel)

    s1.show()

    with open('/Users/francescafornasier/github/Programming_for_IoT_Applications/es01_4_grades.txt', 'r') as file:
        s1.addGrades(file)