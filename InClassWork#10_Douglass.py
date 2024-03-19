#InClassWork10

CHEM_req = ("CHEM 1000","CHEM 2000", "CHEM 3000")
ENV_req = ("ENV 1000","ENV 2000", "ENV 3000")
CE_req = ("EECE 1000","EECE 2000","EECE 3000")
CS_req = ("CS 1000","CS 2000","CS 3000")
EE_req = ("EE 1000", "EE 2000")
PHYS_req = ("PHYS 1000", "PHYS 2000")


class student:
    def __init__(self,name,major):
        self.name = name
        self.major = major

class OneMajor(student):
    def __init__(self, name, major):
        super().__init__(name, major)
        if(major == "CHEM"): self.classes = CHEM_req
        elif(major == "ENV"): self.classes = ENV_req
        elif(major == "CE"): self.classes = CE_req
        elif(major == "CS"): self.classes = CS_req
        elif(major == "EE"): self.classes = EE_req
        elif(major == "PHYS"): self.classes = PHYS_req
        
       
class TwoMajors(OneMajor):
    def __init__(self, name, major1, major2):
        super().__init__(name, major1)
        
        if(major2 == "CHEM"): self.classes.append(CHEM_req)
        elif(major2 == "ENV"): self.classes.append(ENV_req)
        elif(major2 == "CE"): self.classes.append(CE_req)
        elif(major2 == "CS"): self.classes.append(CS_req)
        elif(major2 == "EE"): self.classes.append(EE_req)
        elif(major2 == "PHYS"): self.classes.append(PHYS_req)
        
    def toPrint(self):
        print(self.name, ", ", self.major1, " and ", self.major2)
        print("Classes", self.allClasses)


def main():
    obj = TwoMajors("Bob", "EE", "CE")
    obj.toPrint()
    










