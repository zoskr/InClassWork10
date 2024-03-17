#InClassWork10

CHEM_req = ("CHEM 1000","CHEM 2000", "CHEM 3000")
ENV_req = ("ENV 1000","ENV 2000", "ENV 3000")
CE_req = ("EECE 1000","EECE 2000","EECE 3000")
CS_req = ("CS 1000","CS 2000","CS 3000")
EE_req = ("EE 1000", "EE 2000")
PHYS_req = ("PHYS 1000", "PHYS 2000")

class standard_major:
    def __init__(self,name,major):
        self.name = name
        self.major = major
        
    def course_req(self):
        if self.major == "EECE":
            print(EE_req)

class student:
    def __init__(self,name):
        self.name = name












s1 = standard_major("Bobby","EECE")