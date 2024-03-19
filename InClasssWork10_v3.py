#MiniProject Three, Course Registration Program using OOP, specfically, inheritance

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
       
class CS(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = CS_req
       
class EE(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = EE_req
       
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
           
def case1(): #sample cases
    s1 = Chem("joe")
    print(s1.classes)
    choice = {"1:00":'CHEM 1000'}
    if choice.values()[0] in s1.classes:
        print(s1.register(choice))
    else:
        print("Not in required courses")
   
def case2():
    s2 = ChemEnv("joe")
    print(s2.classes)
    choice = {"1:00":'ENV 1000'}
    l1 = list(choice.values())    
    if l1[0] in s2.classes:
        print(s2.register(choice))
    else:
        print("Not in required courses")
   

def case3():
    s3 = EE('Sarah')
    c1 = {"4:00" :'EE 2140'}
    choice1 = list(c1.values())
    if choice1 in s3.EE_Electives:
        print(s3.register(c1))
    else:
        print("Not in applicable courses")

def case4():
    s4 = ChemEnv("joe")
    c1 = {"1:00":'ENV 1000'}
    choice1 = list(c1.values())    
    if choice1[0] in s4.classes:
        print(s4.register(c1))
    else:
        print("Not in required courses")
   
    c2 = {"1:00":'CHEM 1000'}
    time2 = list(c2.keys())
    choice2 = list(c2.values())    
    if choice2[0] in s4.classes:
        if time2[0] in list(s4.registered_courses.keys()):
            print("Schedule confilct")
        else:
            print(s4.register(c2))
    else:
        print("Not in required courses")
       
       
def case6():
    s6 = CS("joe")
    c1 = {"8:00":"CS 1000"}
    choice1 = list(c1.values())    
    if choice1[0] in s6.classes:
        if len(s6.registered_courses)<4:
            print(s6.register(c1))
        else:
            print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c2 = {"9:00":"CS 2000"}
    choice2 = list(c2.values())    
    if choice2[0] in s6.classes:
        if len(s6.registered_courses)<4:
            print(s6.register(c2))
        else:
            print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c3 = {"10:00":"CS 3000"}
    choice3 = list(c3.values())    
    if choice3[0] in s6.classes:
       if len(s6.registered_courses)<4:
           print(s6.register(c3))
       else:
           print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c4 = {"11:00":"CS 4000"}
    choice4 = list(c4.values())    
    if choice4[0] in s6.classes:
        if len(s6.registered_courses)<4:
            print(s6.register(c4))
        else:
            print("Too many credit hours.")
    else:
        print("Not in required courses")
       
    c5 = {"12:00":"CS 5000"}
    choice5 = list(c5.values())    
    if choice5[0] in s6.classes:
        if len(s6.registered_courses)<4:
            print(s6.register(c5))
        else:
            print("Too many credit hours.")
    else:
        print("Not in required courses")
       
def case7(): #test case seven
    s7 = EE("Zofia")
    s8 = CE("Rob")
    c1 = {"4:00" :'EE 1000'}
    choice1 = list(c1.values())
   
    if choice1[0] in s7.classes:
        print(f"Student is registered for {s7.register(choice1[0])} as a main course.")
        if choice1[0] in s7.EE_Electives:
            print(False)
        else:
            print(True) #shows course is only available for EE as a main course
    else:
        print("Not in applicable courses")
       
    if choice1[0] in s8.CE_Electives:
        print(f"Student is registered for {s8.register(choice1[0])} as an elective.")
        if choice1[0] in s8.classes:
            print(False)
        else:
            print(True) #shows course is only available for CE as an elective
    else:
        print("Not in applicable courses")
        
        