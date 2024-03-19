CHEM_req = ["CHEM 1000","CHEM 2000", "CHEM 3000"]
ENV_req = ["ENV 1000","ENV 2000", "ENV 3000"]
CE_req = ["EECE 1000","EECE 2000","EECE 3000"]
CS_req = ["CS 1000","CS 2000","CS 3000"]
EE_req = ["EE 1000", "EE 2000"]
PHYS_req = ["PHYS 1000", "PHYS 2000"]
Renewable_Concentration = ["ENV 1234","GE 1111"]
Land_Resources = ["ENV 2345","CIV 2356"]

class student:
    def __init__(self,name):
        self.name = name
        self.registered_courses = [] 
    def register(self,choice):
        self.registered_courses.append(choice)
        return self.registered_courses
        
class Chem(student):
    def __init__(self, name):
        super().__init__(name)
        self.chem_classes = CHEM_req
        
class Env(student):
    def __init__(self, name):
        super().__init__(name)
        self.env_classes = ENV_req
        
class ChemEnv(Chem,Env):
    def __init__(self, name):
        super().__init__(name)
        self.classes.append()
class EnergyConcentration(Chem):
    def __init__(self, name):
        super().__init__(name)
        self.classes.append(Renewable_Concentration)
        
class LandResourcesConcentration(Chem): #hierarchical?
    def __init__(self, name):
        super().__init__(name)
        self.classes.append(Land_Resources)
        
    
def case1():
    s1 = Chem("joe")
    print(s1.classes)
    choice = 'CHEM 1000'
    if choice in s1.chem_classes:
        print(s1.register(choice)) 
    else:
        print("Not in required courses")
    
def case2():
    s2 = ChemEnv("bob")
    print(s2.classes)
    
    choice = 'ENV 1000'
    if choice in s2.classes:
        print(s2.register(choice)) 
    else:
        print("Not in required courses")
    
    
case2()
    
    
    
    