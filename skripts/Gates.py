#Default Logic Gates
import pygame

class AndGate():
    def __init__(self, visuals):
        self.imageon = pygame.image.load("./sprits/Andon.png")
        self.imageoff = pygame.image.load("./sprits/And.png")
        self.width = self.imageoff.get_width()
        self.height = self.imageoff.get_height()
        self.output = False
        self.inputs = {}
        self.visuals = visuals

    def out_Calc(self, list):
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
        if self.inputs == {}:
            return False
        self.output = True
        for i in self.inputs:
            if self.inputs[i] == False:
                self.output = False
        return self.output
    
    def input_Add(self,name):
        self.inputs[name] = False

    def input_Remove(self,name):
        try:
            self.inputs.pop(name)
        except:
            pass

    def color_Calc(self, scale):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        x = self.visuals[0]
        y = self.visuals[1]
        self.visuals = pygame.Rect(x,y,width*scale,height*scale)
        if self.output == True:
            self.imageon = pygame.transform.scale(self.imageon, (int(self.width*scale), int(self.height*scale)))
            return self.imageon
        self.imageoff = pygame.transform.scale(self.imageoff, (int(self.width*scale), int(self.height*scale)))
        return self.imageoff
    def image_Scale(self):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        return (width,height)
            
class OrGate():
    def __init__(self,visuals):
        self.imageon = pygame.image.load("./sprits/Oron.png")
        self.imageoff = pygame.image.load("./sprits/Or.png")
        self.width = self.imageoff.get_width()
        self.height = self.imageoff.get_height()
        self.output = False
        self.inputs = {}
        self.visuals = visuals

    def out_Calc(self, list):
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
        self.output = False
        for i in self.inputs:
            if self.inputs[i] == True:
                self.output = True
        return self.output
    
    def input_Add(self,name):
        self.inputs[name] = False

    def input_Remove(self,name):
        try:
            self.inputs.pop(name)
        except:
            pass

    def color_Calc(self, scale):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        x = self.visuals[0]
        y = self.visuals[1]
        self.visuals = pygame.Rect(x,y,width*scale,height*scale)
        if self.output == True:
            self.imageon = pygame.transform.scale(self.imageon, (int(self.width*scale), int(self.height*scale)))
            return self.imageon
        self.imageoff = pygame.transform.scale(self.imageoff, (int(self.width*scale), int(self.height*scale)))
        return self.imageoff
    def image_Scale(self):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        return (width,height)

class NotGate():
    def __init__(self,visuals):
        self.imageon = pygame.image.load("./sprits/Noton.png")
        self.imageoff = pygame.image.load("./sprits/Not.png")
        self.width = self.imageoff.get_width()
        self.height = self.imageoff.get_height()
        self.output = False
        self.inputs = {}
        self.visuals = visuals

    def out_Calc(self, list):
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
        self.output = True
        for i in self.inputs:
            if self.inputs[i] == True:
                self.output = False
        return self.output
    
    def input_Add(self,name):
        self.inputs[name] = False
        

    def input_Remove(self,name):
        try:
            self.inputs.pop(name)
        except:
            pass

    def color_Calc(self, scale):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        x = self.visuals[0]
        y = self.visuals[1]
        self.visuals = pygame.Rect(x,y,width*scale,height*scale)
        if self.output == True:
            self.imageon = pygame.transform.scale(self.imageon, (int(self.width*scale), int(self.height*scale)))
            return self.imageon
        self.imageoff = pygame.transform.scale(self.imageoff, (int(self.width*scale), int(self.height*scale)))
        return self.imageoff
    def image_Scale(self):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        return (width,height)

class BufferGate():
    def __init__(self,visuals):
        self.imageon = pygame.image.load("./sprits/Noton.png")
        self.imageoff = pygame.image.load("./sprits/Not.png")
        self.width = self.imageoff.get_width()
        self.height = self.imageoff.get_height()
        self.output = False
        self.inputs = {}
        self.visuals = visuals
        self.index = 0

    def out_Calc(self, list):
        currentstate = self.output
        for ins in self.inputs.keys():
            for obj in list:
                if obj["name"] == ins:
                    self.inputs[ins] = obj["gate"].output
        self.output = False
        for i in self.inputs:
            if self.inputs[i] == True:
                self.output = True
        if currentstate != self.output:
            self.index += 1
            print(self.index)
        else:
            self.index = 0
            print(self.index)
        if self.index >= 240:
            return self.output
        else:
            self.output = currentstate
            return currentstate
    
    def input_Add(self,name):
        self.inputs[name] = False

    def input_Remove(self,name):
        try:
            self.inputs.pop(name)
        except:
            pass

    def color_Calc(self, scale):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        x = self.visuals[0]
        y = self.visuals[1]
        self.visuals = pygame.Rect(x,y,width*scale,height*scale)
        if self.output == True:
            self.imageon = pygame.transform.scale(self.imageon, (int(self.width*scale), int(self.height*scale)))
            return self.imageon
        self.imageoff = pygame.transform.scale(self.imageoff, (int(self.width*scale), int(self.height*scale)))
        return self.imageoff
    def image_Scale(self):
        width = self.imageoff.get_width()
        height = self.imageoff.get_height()
        return (width,height)
    
