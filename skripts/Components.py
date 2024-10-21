#Default Components
import pygame

class Switch():
    def __init__(self,visuals):
        self.imageon = pygame.image.load("./sprits/Buttonon.png")
        self.imageoff = pygame.image.load("./sprits/Button.png")
        self.width = self.imageoff.get_width()
        self.height = self.imageoff.get_height()
        self.output = False
        self.inputs = {}
        self.visuals = visuals

    def out_Calc(self, list):
        return self.output
    
    def change_State(self):
        if self.output == True:
            self.output = False
        else: self.output = True

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
    
    def get_State(self):
        return self.output
    
class Bulb():
    def __init__(self,visuals):
        self.imageon = pygame.image.load("./sprits/Lampon.png")
        self.imageoff = pygame.image.load("./sprits/Lamp.png")
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
    
    def get_State(self):
        return self.output