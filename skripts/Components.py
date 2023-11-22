#Default Components

class Switch():
    def __init__(self):
        self.output = False
        self.inputs = {}
        self.coloroff = "#3a676b"
        self.coloron = "#65e4f0"

    def out_Calc(self, list):
        return self.output
    
    def change_State(self):
        if self.output == True:
            self.output = False
        else: self.output = True

    def color_Calc(self):
        if self.output == True:
            return self.coloron
        return self.coloroff
    
class Bulb():
    def __init__(self):
        self.output = False
        self.inputs = {}
        self.coloroff = "#7a766a"
        self.coloron = "#fcc93d"

    def out_Calc(self, list):
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
        self.output == False
        for i in self.inputs:
            if self.inputs[i] == True:
                self.output = True
            else:
                self.output = False
        return self.output
    
    def input_Add(self,name):
        self.inputs[name] = False

    def input_Remove(self,name):
        self.inputs.pop(name)

    def color_Calc(self):
        if self.output == True:
            return self.coloron
        else: 
            return self.coloroff