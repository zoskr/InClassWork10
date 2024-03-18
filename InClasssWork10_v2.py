CHEM_req = ("CHEM 1000","CHEM 2000", "CHEM 3000")
ENV_req = ("ENV 1000","ENV 2000", "ENV 3000")
CE_req = ("EECE 1000","EECE 2000","EECE 3000")
CS_req = ("CS 1000","CS 2000","CS 3000")
EE_req = ("EE 1000", "EE 2000")
PHYS_req = ("PHYS 1000", "PHYS 2000")

class student:
    def __init__(self,name):
        self.name = name

class Chem(student):
    def __init__(self, name):
        super().__init__(name)
        self.classes = CHEM_req
        
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

class ChemEnv(Chem,Env):
    def __init__(self, name):
        super().__init__(name)
        self.classes = CHEM_req
        self.classes.append(ENV_req)

