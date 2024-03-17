#InClassWork10

CHEM_req = ("CHEM 1000","CHEM 2000", "CHEM 3000")
ENV_req = ("ENV 1000","ENV 2000", "ENV 3000")
CE_req = ("EECE 1000","EECE 2000","EECE 3000")
CS_req = ("CS 1000","CS 2000","CS 3000")
EE_req = ("EE 1000", "EE 2000")
PHYS_req = ("PHYS 1000", "PHYS 2000")



class major1:
    def __init__(self,major,courseReq):
        self.major = major
        self.courseReq = courseReq
        
class major2:
    def __init__(self,major,courseReq):
        self.major = major
        self.courseReq = courseReq

class student(major1): #single inheritance
    def __init__(self,name,major,courseReq):
        super().__init__(major, courseReq)
        self.name = name
        
        
class combined(student, major2):
    







    













x = courseReq("Chem", CHEM_req)


