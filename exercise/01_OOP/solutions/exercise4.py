#from statistics import mean
import statistics

class Student:
    def __init__(self,name,surname,birthYear,student_status):
        self.name= name
        self.surname= surname
        self.birthYear= birthYear
        self.bachelor= student_status == 'b' or student_status =='B' or student_status == 'bachelor' or student_status == 'Bachelor' 
        self.master= student_status == 'm' or student_status =='M' or student_status == 'master' or student_status == 'Master'
        self.votes=[]

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
    
    def read_votes(self, voteFileName):
        fileRead=open(voteFileName).read()
        votesList=fileRead.split(',')
        #votes=['24','21','23']
        #1
        list_votes=[]
        for vote in votesList:
            list_votes.append(int(vote))
        self.votes=list_votes
        #votes=[24,21,23]
    
    def statistics_votes(self):
        #maximum
        max_vote=max(self.votes)
        print(f'The maximum vote is {max_vote}')
        #minimum
        min_vote=min(self.votes)
        print(f'The minimum vote is {min_vote}')
        #average -> old school
        num_votes=len(self.votes)
        sum_votes=0
        for vote in self.votes:
            sum_votes+=vote
        average_votes=sum_votes/num_votes
        print(f'The average vote is {average_votes}')

        #average -> clever way
        #average2=mean(self.votes)
        average2=statistics.mean(self.votes)
        print(f'The average vote is {average2}')





if __name__=='__main__':
    name=input('Enter your name: ')
    surname=input('Enter your surname: ')
    birthYear=int(input('Enter your birth year: '))
    #student_status=input('Select your level of Eductation (bachelor,master):')
    
    #make sure user enters a valid status. If not, ask again
    condition_studentStatus=True
    while condition_studentStatus:
        student_status=input('Select your level of Eductation (bachelor,master):')
        if student_status=='b' or student_status=='B' or student_status=='bachelor' or student_status=='Bachelor':
            condition_studentStatus=False
        elif student_status=='m' or student_status=='M' or student_status=='master' or student_status=='Master':
            condition_studentStatus=False
        else:
            print('Please enter a valid status')

    studentA=Student(name,surname,birthYear,student_status)
    studentA.show()
    studentA.age()
    studentA.save() 
    studentA.isBachelor()
    studentA.isMaster()
    voteFileName=input('Enter the name of the file that contains the votes: ')
    studentA.read_votes(voteFileName)
    studentA.statistics_votes()