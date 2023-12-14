import pygame
import os
import json
import asyncio
import time

# --- constants --- (UPPER_CASE names)
ICON = pygame.image.load("sprits/Icon.ico")
SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410
# - colors -
lineaktiv = "#3adff0"
lineinaktiv = "#003a40"

FPS = 60

# --- classses --- (CamelCase names)

from Gates import AndGate, OrGate, NotGate, BufferGate
from Components import Switch, Bulb

class Games():
    def __init__(self):
        self.y = True
    def game_running(self, x = "NON"):
        if x == "Close":
            self.y = False
        return self.y

# --- functions --- (lower_case names)
def on_start():
    objs = []
    objsco = 0
    lins = []
    linsco = 0

    absolute_path = os.path.dirname(__file__)
    absolute_path = absolute_path.strip("skripts")
    relative_path = "saves"
    path = os.path.join(absolute_path, relative_path)
    print(os.listdir(path))
    loadeFile = input("loade file / create file ...")+".json"
    fullpath = path+"\\"+loadeFile
    if os.path.exists(fullpath):
        os.chdir(path)
        try:
            with open(loadeFile, "r") as fp:
                file = json.load(fp)
                os.chdir(absolute_path)
        except:
            os.chdir(absolute_path)
            return fullpath, objs, objsco, lins, linsco

        for gate in file[0]:
            if gate["type"] == 0:
                objs.append(create_new_andGate(gate["name"],gate["visuals"]))
            if gate["type"] == 1:
                objs.append(create_new_orGate(gate["name"],gate["visuals"]))
            if gate["type"] == 2:
                objs.append(create_new_notGate(gate["name"],gate["visuals"]))
            if gate["type"] == 3:
                objs.append(create_new_switch(gate["name"],gate["visuals"]))
            if gate["type"] == 4:
                objs.append(create_new_bulb(gate["name"],gate["visuals"]))
            if gate["type"] == 5:
                objs.append(create_new_bufferGate(gate["name"],gate["visuals"]))

        for lin in file[2]:
            lins.append(draw_new_line(lin["name"], lin["start"], lin["stop"]))
            for gate in objs:
                if gate["name"] == lin["stop"]:
                    gate["gate"].input_Add(lin["start"])

        objsco = file[1]
        linsco = file[3]
        return fullpath, objs, objsco, lins, linsco
    else:
        with open(fullpath, 'w') as fp:
            return fullpath, objs, objsco, lins, linsco


def on_close(objs, objsco, lins, linsco, filepath):
    comps = []
    for obj in objs:
        visuals = (obj["gate"].visuals[0],obj["gate"].visuals[1],obj["gate"].visuals[2],obj["gate"].visuals[3])
        comps.append({
            "name" : obj["name"],
            "type" : obj["type"],
            "visuals" : visuals
        })
    linecomps = []
    for lin in lins:
        linecomps.append({
            "name": lin["name"],
            "start": lin["start"],
            "stop": lin["stop"],

        })
    liste = [comps, objsco, linecomps, linsco]
    safe = json.dumps(liste, indent=len(liste))
    with open(filepath, "w") as outfile:
        outfile.write(safe)
        print("-- File saved --")
    return

#types:
#0 = and
#1 = or 
#2 = not
#3 = switch
#4 = bulb
def create_new_andGate(counter, visuals = pygame.Rect(75, 75, 64 , 64)):
    if type(visuals) != pygame.rect.Rect:
        visuals = pygame.Rect(visuals[0],visuals[1],visuals[2],visuals[3])
    name = str(counter)
    gate = AndGate(visuals)
    andgateobj = {
        "name": name,
        "gate": gate,
        "type": 0
    }    
    return andgateobj

def create_new_orGate(counter, visuals = pygame.Rect(75, 75, 64 , 64)):
    if type(visuals) != pygame.rect.Rect:
        visuals = pygame.Rect(visuals[0],visuals[1],visuals[2],visuals[3])
    name = str(counter)
    gate = OrGate(visuals)
    orgateobj = {
        "name": name,
        "gate": gate,
        "type": 1
    }    
    return orgateobj

def create_new_notGate(counter, visuals = pygame.Rect(75, 75, 64 , 64)):
    if type(visuals) != pygame.rect.Rect:
        visuals = pygame.Rect(visuals[0],visuals[1],visuals[2],visuals[3])
    name = str(counter)
    gate = NotGate(visuals)
    notgateobj = {
        "name": name,
        "gate": gate,
        "type": 2,
    }    
    return notgateobj

def create_new_switch(counter, visuals = pygame.Rect(75, 75, 64 , 64)):
    if type(visuals) != pygame.rect.Rect:
        visuals = pygame.Rect(visuals[0],visuals[1],visuals[2],visuals[3])
    name = str(counter)
    gate = Switch(visuals)
    switchobj = {
        "name": name,
        "gate": gate,
        "type": 3
    }    
    return switchobj

def create_new_bulb(counter, visuals = pygame.Rect(75, 75, 64 , 64)):
    if type(visuals) != pygame.rect.Rect:
        visuals = pygame.Rect(visuals[0],visuals[1],visuals[2],visuals[3])
    name = str(counter)
    gate = Bulb(visuals)
    bulbobj = {
        "name": name,
        "gate": gate,
        "type": 4
    }    
    return bulbobj

def create_new_bufferGate(counter, visuals = pygame.Rect(75, 75, 64 , 64)):
    if type(visuals) != pygame.rect.Rect:
        visuals = pygame.Rect(visuals[0],visuals[1],visuals[2],visuals[3])
    name = str(counter)
    gate = BufferGate(visuals)
    bulbobj = {
        "name": name,
        "gate": gate,
        "type": 5
    }    
    return bulbobj

def draw_new_line(counter,startpos, stoppos):
    name = str(counter)
    lineobj = {
        "name": name,
        "start": startpos,
        "stop": stoppos,
        "linestate": printtrue
    }
    return lineobj

def printtrue(startpos):
    for obj in objcs:
        if startpos == obj["name"]:
            if obj["gate"].output == True:
                return lineaktiv
            return lineinaktiv

def abstand(objs):
    maxabstand = 0
    for obj in objs:
        for secobj in objs:
            abstand = ((obj["gate"].visuals[0]-secobj["gate"].visuals[0])**2+(obj["gate"].visuals[1]-secobj["gate"].visuals[1])**2)**(1/2)
            abstandx = (obj["gate"].visuals[0]-secobj["gate"].visuals[0])
            abstandy = (obj["gate"].visuals[1]-secobj["gate"].visuals[1])
            if abstand > maxabstand:
                maxabstand = abstand
                maxabstandx = abstandx
                maxabstandy = abstandy
    #print(maxabstand, maxabstandx, maxabstandy)
    return

def warheitstabelle(objs):
    set = True
    inputs = []
    outputs = []
    stateout = []
    statein = []
    line = []
    for obj in objs:
        if obj["type"] == 3:
            inputs.append(obj)
        if obj["type"] == 4:
            outputs.append(obj)
    if len(outputs) == 0 or len(inputs) == 0:
        print("--- Please have min one INPUT [4] and one OUTPUT [5] ---")
        return
    for ins in inputs:
        if ins["gate"].get_State():
            ins["gate"].change_State()
    for outs in outputs:
        line =[]
        for num in range(0,len(inputs)):
            line.append("x"+f"{num}")
        line.append("OUT")
        print(line)
        line = []
        for num in range(0,len(inputs)):
            line.append("0 ")
        line.append(outs["gate"].get_State())
        print(line)
    line = []
    for outs in outputs:
        counter = 0
        inputs[0]["gate"].change_State()
        sim_calc()
        print(["1 ","0 ", outs["gate"].get_State()])
        inputs[0]["gate"].change_State()
        inputs[1]["gate"].change_State()
        sim_calc()
        print(["0 ","1 ", outs["gate"].get_State()])
        inputs[0]["gate"].change_State()
        sim_calc()
        print(["1 ","1 ", outs["gate"].get_State()])


async def sim_calc():
    for obj in objcs:
        if obj["type"] == 5:
            asyncio.sleep(1)
        obj["gate"].out_Calc(objcs)

async def visuals_update():
    for line in lines:
        for obj in objcs:
            if line["start"] == obj["name"]:
                pos1 = (obj["gate"].visuals[0]+obj["gate"].image_Scale()[0],obj["gate"].visuals[1]+obj["gate"].image_Scale()[1]/2)
            if line["stop"] == obj["name"]:
                pos2 = (obj["gate"].visuals[0],obj["gate"].visuals[1]+obj["gate"].image_Scale()[1]/2)
        pygame.draw.line(screen, line["linestate"](line["start"]), pos1, pos2, 5*scale)
    
    for obj in objcs:
            screen.blit(obj["gate"].color_Calc(scale),(obj["gate"].visuals[0], obj["gate"].visuals[1]))
    pygame.display.flip()
            
async def main(running, screen, highlight,highlight2, aktive_obj, objcs, objscounter, start_obj, stop_obj, lines, linecounter,scale):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on_close(objcs, objscounter, lines, linecounter, saveFile)
            running.game_running("Close")
            await pygame.quit()
            await loop.close()       
            
            
            

        
        # - drag and drop -
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, obj in enumerate(objcs):
                    if obj["gate"].visuals.collidepoint(event.pos):
                            aktive_obj = num

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                aktive_obj = None
        if event.type == pygame.MOUSEMOTION:
            if aktive_obj != None:
                objcs[aktive_obj]["gate"].visuals.move_ip(event.rel)

        # - connect lines -
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                for num, obj in enumerate(objcs):
                    if obj["gate"].visuals.collidepoint(event.pos):
                            start_obj = num
                            scalew, scaleh = obj["gate"].image_Scale()
                            highlight = pygame.Rect(float(obj["gate"].visuals[0]- (5/2)*scale),float(obj["gate"].visuals[1]-(5/2)*scale), float(scalew+5*scale), float(scaleh+5*scale))
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                if stop_obj == None or start_obj == None or objcs[stop_obj]["type"] == 3:
                    start_obj = None
                    stop_obj = None
                    highlight = None
                    highlight2 = None
                    break
                exists = False
                exists_line = None
                if len(lines) != 0:
                    for num, line in enumerate(lines):
                        if line["start"] == objcs[start_obj]["name"] and line["stop"] == objcs[stop_obj]["name"]:
                            exists = True
                            exists_line = num
                if exists == True:
                    lines.pop(exists_line)
                    objcs[stop_obj]["gate"].input_Remove(objcs[start_obj]["name"])
                    start_obj = None
                    stop_obj = None
                    highlight = None
                    highlight2 = None
                    exists_line = None 

                if exists == False:
                    lines.insert(-1, draw_new_line(linecounter, objcs[start_obj]["name"],objcs[stop_obj]["name"]))
                    objcs[stop_obj]["gate"].input_Add(objcs[start_obj]["name"])
                    linecounter += 1
                    start_obj = None                        
                    stop_obj = None
                    highlight = None
                    highlight2 = None

        if event.type == pygame.MOUSEMOTION:
            if start_obj != None:
                for num, obj in enumerate(objcs):
                    if obj["gate"].visuals.collidepoint(pygame.mouse.get_pos()):
                        stop_obj = num
                        scalew, scaleh = obj["gate"].image_Scale()
                        highlight2 = pygame.Rect(float(obj["gate"].visuals[0]-(5/2)*scale),float(obj["gate"].visuals[1]-(5/2)*scale), float(scalew+5*scale), float(scaleh+5*scale))
                    try:
                        if not highlight2.collidepoint(pygame.mouse.get_pos()):
                            highlight2 = None
                            stop_obj = None
                    except:
                        pass
        

        # - key events -
        if event.type == pygame.KEYDOWN:
            
            # - create new gates -
            if event.key == pygame.K_1:
                objcs.append(create_new_andGate(objscounter))
                objscounter += 1
            if event.key == pygame.K_2:
                objcs.append(create_new_orGate(objscounter))
                objscounter += 1
            if event.key == pygame.K_3:
                objcs.append(create_new_notGate(objscounter))
                objscounter += 1
            if event.key == pygame.K_4:
                objcs.append(create_new_switch(objscounter))
                objscounter += 1
            if event.key == pygame.K_5:
                objcs.append(create_new_bulb(objscounter))
                objscounter += 1
            if event.key == pygame.K_6:
                objcs.append(create_new_bufferGate(objscounter))
                objscounter += 1
            if event.key == pygame.K_q:
                warheitstabelle(objcs)

            # -toggle switch -
            if event.key == pygame.K_t:
                for num, obj in enumerate(objcs):
                    if obj["gate"].visuals.collidepoint(pygame.mouse.get_pos()):
                        if obj["type"] != 3:
                            break
                        obj["gate"].change_State()

            # - full screen toggle -
            if event.key == pygame.K_F11:
                if fullscreen == True:
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
                    fullscreen = False
                elif fullscreen == False:
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    fullscreen = True

            # -destroy objcs -
            if event.key == pygame.K_DELETE:
                for num, obj in enumerate(objcs):
                    if obj["gate"].visuals.collidepoint(pygame.mouse.get_pos()):
                        toremovelines =[]
                        for line in lines:
                            if obj["name"] == line["stop"]:
                                toremovelines.append(line)
                            elif obj["name"] == line["start"]:
                                toremovelines.append(line)
                        for secobj in objcs:
                            if secobj["type"] == 3:
                                pass
                            else:
                                secobj["gate"].input_Remove(obj["name"])
                        objcs.pop(num)
                        for rev in toremovelines:
                            lines.remove(rev)

            
    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill("white")

    if highlight != None:
        pygame.draw.line(screen, lineinaktiv, (float(highlight[0]), float(highlight[1])), pygame.mouse.get_pos(), 5*scale)
        pygame.draw.rect(screen, "green", highlight)
    if highlight2 != None:
        pygame.draw.rect(screen, "green", highlight2)

    # - constant game speed / FPS -

    clock.tick(FPS)

    
# --- main ---

# - init -
pygame.display.set_icon(ICON)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
fullscreen = False
#screen_rect = screen.get_rect()

pygame.display.set_caption("Le Pain")

# - vars -
saveFile = ""
highlight = None
highlight2 = None
aktive_obj = None
objcs = []
objscounter = 0
start_obj = None
stop_obj = None
lines = []
linecounter = 0
scale = 1

# - mainloop -
saveFile, objcs, objscounter, lines, linecounter = on_start()
clock = pygame.time.Clock()

running = Games()

while running.game_running():
    # - events -
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(sim_calc()),
        loop.create_task(visuals_update()),
        loop.create_task(main(running, screen, highlight,highlight2, aktive_obj, objcs, objscounter, start_obj, stop_obj, lines, linecounter,scale)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))



# - end -