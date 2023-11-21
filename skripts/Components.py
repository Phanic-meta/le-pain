#Default Components

class Switch():
    def __init__(self):
        self.state = False
        self.inputs = {}
    def create_output(self,other):
        pass

class Bulb():
    def __init__(self):
        self.state = False
        self.inputs = {}
    def state_calc(self):
        for i in self.inputs():
            if self.inputs[i] == True:
                self.state = True
        return self.state