#Default Logic Gates

class AndGate():
    def __init__(self):
        self.output = False
        self.inputs = {}
        self.coloroff = "#32a852"
        self.coloron = "#2bd659"

    def out_Calc(self, list):
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
                    print( obj["gate"].output)
        self.output = True
        for i in self.inputs:
            if self.inputs[i] == False:
                self.output = False
        return self.output
    
    def input_Add(self,name):
        self.inputs[name] = False

    def input_Remove(self,name):
        self.inputs.pop(name)

    def color_Calc(self):
        if self.output == True:
            return self.coloron
        return self.coloroff
            
class OrGate():
    def __init__(self):
        self.output = False
        self.inputs = {}
        self.coloroff = "#32a852"
        self.coloron = "#2bd659"

    def out_Calc(self, list):
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
                    print( obj["gate"].output)
        self.output = True
        for i in self.inputs:
            if self.inputs[i] == True:
                self.output = True
        return self.output
    
    def input_Add(self,name):
        self.inputs[name] = False

    def input_Remove(self,name):
        self.inputs.pop(name)

    def color_Calc(self):
        if self.output == True:
            return self.coloron
        return self.coloroff

class NotGate():
    def __init__(self):
        self.output = False
        self.inputs = {}
        self.coloroff = "#32a852"
        self.coloron = "#2bd659"

    def out_Calc(self, list):
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
                    print( obj["gate"].output)
        self.output = False
        for i in self.inputs:
            if self.inputs[i] == True:
                self.output = True
        return self.output
    
    def input_Add(self,name):
        self.inputs[name] = False

    def input_Remove(self,name):
            self.inputs.pop(name)

    def color_Calc(self):
        if self.output == True:
            return self.coloron
        return self.coloroff
    
