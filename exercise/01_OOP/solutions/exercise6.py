import statistics
import json

class Student:
    def __init__(self,jsonfile):
        self.conf=json.load(open(jsonfile))
        self.name= self.conf['name']
        self.surname= self.conf['surname']
        self.birthYear= self.conf['birthYear']
        self.bachelor= self.conf['bachelor'] 
        self.master= self.conf['master']
        self.votes=self.conf['votes']

    def show(self):
        print(f"Hi, I'm {self.name} {self.surname}")
    
    def age(self):
        print(f'I am {2024-self.birthYear} years old')

    def save(self):
        '''
        with open('student.txt','w') as file_2:
            toWrite=f'{self.name},{self.surname},{self.birthYear}'
            file_2.write(toWrite)
        print('File is already close.. no risk of open file')
        '''
        json.dump(self.conf,open('myFile.json','w'))
    
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
    
    def asDictionary(self):
        #Output -> {“name”:”Lionel”,”surname”:”Messi”,”birthYear”:1987,”votes”:[24,27,18,30,21]}
        '''
        dictionary_student={
            "name":self.name,
            "surname":self.surname,
            "birthYear":self.birthYear,
            "votes":self.votes
        }
        #print(dictionary_student)
        '''
        json.dumps(self.conf)





if __name__=='__main__':
    studentA=Student('student.json')
    studentA.show()
    studentA.age()
    studentA.save() 
    studentA.isBachelor()
    studentA.isMaster()
    studentA.statistics_votes()
    #print(studentA.asDictionary())
    studentA.asDictionary()