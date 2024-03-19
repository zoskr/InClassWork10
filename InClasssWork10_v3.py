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
    s1 = Chem("joe")
    print(s1.classes) 
    choice = 'CHEM 1567'
    if choice in s1.classes:
        print(s1.register(choice))
    else:
        print("Not in required courses")
    

    
    
    