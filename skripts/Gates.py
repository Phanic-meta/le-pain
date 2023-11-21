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
    
