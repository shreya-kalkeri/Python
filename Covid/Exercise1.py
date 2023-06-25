import random
import datetime

class Covid:
    def __init__(self,Patients):
        self.patients = Patients
        #print(self.patients)
    
    #To choose a random patient from the batch
    def chooseRandom(batchSplit):
        def wrapperFunction(*args, **kwargs):
            yieldedSplit = batchSplit(*args, **kwargs)
            for eachSplit in yieldedSplit:
                r1 = random.choice(eachSplit)
                print(f"Patient {r1} tested on {datetime.datetime.now()}")
            return yieldedSplit
        return wrapperFunction
    
    #To split the batch into desired number of patients
    @chooseRandom
    def batchSplit(self,s):
        for i in range(0,len(self.patients),s):
            yield self.patients[i:i+s]

    #To extend the patient list
    def listGrow(self,userList):
        self.patients.extend(userList)

Patients = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15',
'p16','p17','p18','p19','p20']

recoveredPatients = Covid(Patients)

#Extend the list
inQuestion = input("Do you want to extend the list? y/n \n")
if inQuestion == 'y':
    inputString = input("Enter your new list seperated by space \n")
    userList = inputString.split()
    recoveredPatients.listGrow(userList)
else:
    pass 

#split the list according to the batch size
s = int(input("Enter the batch size \n"))
recoveredPatients.batchSplit(s)