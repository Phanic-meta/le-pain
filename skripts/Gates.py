#Default Logic Gates

class AndGate():
    def __init__(self):
        self.output = False
        self.inputs = {}
    def out_Calc(self):
        self.output = True
        for i in self.inputs:
            if self.inputs[i] == False:
                self.output = False
        return self.output
    def input_Add(self,name):
        self.inputs[name] = False
    def input_Remove(self,name):
        self.inputs.pop(name)
            
class OrGate():
    def __init__(self):
        self.output = False
        self.inputs = {}
    def out_Calc(self):
        self.output = False
        for i in self.inputs:
            if self.inputs[i] == True:
                self.output = True
        return self.output
    def input_Add(self,name):
        self.inputs[name] = False

class NotGate():
    def __init__(self):
        self.output = False
        self.inputs = {}
    def out_Calc(self):
        self.output = True
        for i in self.inputs:
            if self.inputs[i] == False:
                self.output = False
        return self.output
    def input_Add(self,name):
        self.inputs[name] = False
    
