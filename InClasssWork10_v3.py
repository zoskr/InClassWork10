#MiniProject Three, Course Registration Program using OOP, specfically, inheritance

CHEM_req = ["CHEM 1000","CHEM 2000", "CHEM 3000"] #lists containing required courses
ENV_req = ["ENV 1000","ENV 2000", "ENV 3000"]     #available for each department and the sample cases for concentrations
CE_req = ["EECE 1000","EECE 2000","EECE 3000"]
CS_req = ["CS 1000","CS 2000","CS 3000"]
EE_req = ["EE 1000", "EE 2000"]
PHYS_req = ["PHYS 1000", "PHYS 2000"]
Renewable_Concentration = ["ENV 1234","GE 1111"]
Land_Resources = ["ENV 2345","CIV 2356"]

class student: #parent class for the departments
    
    def __init__(self,name): #initializes only student name and empty class list
        self.name = name 
        self.registered_courses = []
        
   
    def register(self,choice): #method for registering student for a course
        self.registered_courses.append(choice)
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
        self.classes = CHEM_req #same reqs as chem
        self.classes.append(ENV_req) #adds env reqs to reqs for combined chem env major
        
class EnergyConcentration(Chem): #multilevel inheritance, hierarchical
    def __init__(self, name):
        super().__init__(name)
        self.classes.append(Renewable_Concentration) #adds concentration courses to parent courses
        
class LandResourcesConcentration(Chem): #multilevel, hierarchical
    def __init__(self, name):
        super().__init__(name)
        self.classes.append(Land_Resources)
           
def case1(): #sample cases
    s1 = Chem("Joe")
    print(s1.classes) 
    choice = 'CHEM 1567'
    if choice in s1.classes:
        print(s1.register(choice))
    else:
        print("Not in required courses")
    


def case3():
    s3 = EE('Sarah')
    choice = 'EE 2140'
    if choice in s3.EE_Electives:
        print(s3.register(choice))
    else:
        print("Not in applicable courses")
            



def case7(): #test case seven
    s7 = EE("Zofia") 
    s8 = CE("Rob")
    choice = 'EE 1000'
    
    if choice in s7.classes:
        print(f"Student is registered for {s7.register(choice)} as a main course.")
        if choice in s7.EE_Electives:
            print(False)
        else:
            print(True) #shows course is only available for EE as a main course
    else:
        print("Not in applicable courses")
        
    if choice in s8.CE_Electives:
        print(f"Student is registered for {s8.register(choice)} as an elective.")
        if choice in s8.classes:
            print(False)
        else:
            print(True) #shows course is only available for CE as an elective
    else:
        print("Not in applicable courses")
    
case7()