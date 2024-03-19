#MiniProject Three, Course Registration Program using OOP, specfically, inheritance
#Did not do the test cases for each department but they are demonstrated at least once

CHEM_req = ["CHEM 1000","CHEM 2000", "CHEM 3000"] #lists containing required courses
ENV_req = ["ENV 1000","ENV 2000", "ENV 3000"]     #available for each department and the sample cases for concentrations
CE_req = ["EECE 1000","EECE 2000","EECE 3000"]
CS_req = ["CS 1000","CS 2000","CS 3000", "CS 4000", "CS 5000"]
EE_req = ["EE 1000", "EE 2000"]
PHYS_req = ["PHYS 1000", "PHYS 2000"]
Renewable_Concentration = ["ENV 1234","GE 1111"]
Land_Resources = ["ENV 2345","CIV 2356"]

class student: #parent class for the departments
   
    def __init__(self,name): #initializes only student name and empty class list
        self.name = name
        self.registered_courses = {}
       
   
    def register(self,choice): #method for registering student for a course
        self.registered_courses.update(choice)
        return self.registered_courses
   
   
       
#each major department follows the same formula, description for chem matches
   
class Chem(student): #chem major, child to student, single inheritance
    def __init__(self, name):
        super().__init__(name) #super method pulls from student
        self.classes = CHEM_req #assigns classes available to the chem list
       
class Env(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = ENV_req
       
class CE(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = CE_req
        self.CE_Electives = ["EE 1000"]
        
class CS(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = CS_req
       
class EE(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = EE_req
        self.EE_Electives = ['EECE 2140','EECE 2150']
        
class Phys(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = PHYS_req

class ChemEnv(Chem,Env): #multiple, hybrid inheritance (student to chem to chemenv)
    def __init__(self, name):
        super().__init__(name)
        self.classes += ENV_req#adds env reqs to reqs for combined chem env major
       
class EnergyConcentration(Chem): #multilevel inheritance, hierarchical
    def __init__(self, name):
        super().__init__(name)
        self.classes += Renewable_Concentration #adds concentration courses to parent courses
       
class LandResourcesConcentration(Chem): #multilevel, hierarchical
    def __init__(self, name):
        super().__init__(name)
        self.classes += Land_Resources
           
def case1(): #test case 1, Single MajorCourse Registration
    s1 = Chem("joe") #single inheritance
    print(s1.classes) #prints chem required courses
    choice = {"1:00":'CHEM 1000'}
    if list(choice.values())[0] in s1.classes: #student is registered to course without error
        print(s1.register(choice))
    else:
        print("Not in required courses")
   
def case2(): #test case 2, Dual Major Course Registration
    s2 = ChemEnv("joe") #multiple, hybrid inheritance
    print(s2.classes)
    choice = {"1:00":'ENV 1000'} #course counting for both majors
    l1 = list(choice.values())    
    if l1[0] in s2.classes:
        print(s2.register(choice)) #student is registered for class without error
    else:
        print("Not in required courses")
   

def case3(): #test case 3, Elective Course Registration
    s3 = EE('Sarah') #single inheritance
    c1 = {"4:00" :'EECE 2140'}
    choice1 = c1["4:00"] #selecting value (class ID)
    if choice1 in s3.EE_Electives:#student is able to register for elective without error
        print(f"Student is succeefully registered for {s3.register(c1)}")
    else:
        print("Not in applicable courses")

def case4(): #test case 4, Scheduling Conflict Detection
    s4 = ChemEnv("joe") #multiple, hybrid inheritance
    c1 = {"1:00":'ENV 1000'}
    choice1 = list(c1.values())    
    if choice1[0] in s4.classes: #student is registered for first course if in reqs
        print(s4.register(c1))
    else:
        print("Not in required courses")
   
    c2 = {"1:00":'CHEM 1000'}
    time2 = list(c2.keys()) #splitting course two into keys and values
    choice2 = list(c2.values())    
    if choice2[0] in s4.classes: #if there is a time conflict, the student cannot be registered for the second course
        if time2[0] in list(s4.registered_courses.keys()):
            print("Schedule confilct")
        else:
            print(s4.register(c2)) #if no conflict, they are registered
    else:
        print("Not in required courses")
        
def case5(): #test case 5, Prerequisite Check

    s5 = Phys("Becky")
    course1 = {"2:00":'PHYS 1000'}
    course2 = {"3:00":'PHYS 2000'}
   
    if list(course1.values())[0] in list(s5.registered_courses.values()): #showing denial based on prereq not met
        s5.register(course2) #if the prereq(course1) is in the dictionary, course2 can be registered
        print("Student has been registered") 
    else:
        print("Student cannot be registered, prerequisite not met") 
       
    c1 = {"2:00":"PHYS 1000"}
   
    s5.register(c1) #prereq added to taken courses
    if list(course1.values())[0] in list(s5.registered_courses.values()): #student is registered as prereq is now met
        s5.register(course2)
        print("Student has been registered")
    else:
        print("Student cannot be registered, prerequisite not met")
        
def case6(): #Credit Limit Enforcement
    s6 = CS("joe")
    c1 = {"8:00":"CS 1000"}
    choice1 = list(c1.values())   #uses the course ID not the time from dictionary 
    if choice1[0] in s6.classes:
        if len(s6.registered_courses)<4: #allows student to register if they are taking under 4 classes, 16 credit hours
            print(s6.register(c1))       #s6 registered for one course
        else:
            print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c2 = {"9:00":"CS 2000"}
    choice2 = list(c2.values())    
    if choice2[0] in s6.classes: 
        if len(s6.registered_courses)<4:
            print(s6.register(c2))  #s6 registered for two courses
        else:
            print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c3 = {"10:00":"CS 3000"}
    choice3 = list(c3.values())    
    if choice3[0] in s6.classes:
       if len(s6.registered_courses)<4:
           print(s6.register(c3)) #s6 registered for three courses
       else:
           print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c4 = {"11:00":"CS 4000"}
    choice4 = list(c4.values())    
    if choice4[0] in s6.classes:
        if len(s6.registered_courses)<4:
            print(s6.register(c4)) #s6 registered for four courses
        else:
            print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c5 = {"12:00":"CS 5000"}
    choice5 = list(c5.values())    
    if choice5[0] in s6.classes:
        if len(s6.registered_courses)<4:
            print(s6.register(c5)) #s6 trying to register for a fifth, will fail
        else:
            print("Too many credit hours.") #fail message will print, four is the max
    else:
        print("Not in required courses")
       
def case7(): #test case 7, Hybrid Inheritance Functionality
    s7 = EE("Zofia")
    s8 = CE("Rob")
    c1 = {"4:00" :'EE 1000'}
    choice1 = list(c1.values())
   
    if choice1[0] in s7.classes: #if class is in the required courses for EE
        print(f"Student is registered for {s7.register(c1)} as a main course.")
        if choice1[0] in s7.EE_Electives:
            print(False)
        else:
            print(True) #shows course is only available for EE as a main course
    else:
        print("Not in applicable courses")
       
    if choice1[0] in s8.CE_Electives: #if class is in elective options for CE
        print(f"Student is registered for {s8.register(c1)} as an elective.")
        if choice1[0] in s8.classes:
            print(False)
        else:
            print(True) #shows course is only available for CE as an elective
    else:
        print("Not in applicable courses")
        
case1() #calling the test case functions
case2()
case3()
case4()
case5()       
case6()
case7()