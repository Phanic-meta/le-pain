import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410
# - colors -
lineaktiv = "#3adff0"
lineinaktiv = "#003a40"

FPS = 60

# --- classses --- (CamelCase names)

from Gates import AndGate, OrGate, NotGate
from Components import Switch, Bulb

# --- functions --- (lower_case names)

#types:
#0 = and
#1 = or 
#2 = not
#3 = switch
#4 = bulb
def create_new_andGate(counter):
    visuals = pygame.Rect(75, 75, 64 , 64)
    name = str(counter)
    gate = AndGate(visuals)
    andgateobj = {
        "name": name,
        "gate": gate,
        "type": 0
    }    
    return andgateobj

def create_new_orGate(counter):
    visuals = pygame.Rect(75, 75, 64 ,64)
    name = str(counter)
    gate = OrGate(visuals)
    orgateobj = {
        "name": name,
        "gate": gate,
        "type": 1
    }    
    return orgateobj

def create_new_notGate(counter):
    visuals = pygame.Rect(75, 75, 64 ,64)
    name = str(counter)
    gate = NotGate(visuals)
    notgateobj = {
        "name": name,
        "gate": gate,
        "type": 2,
    }    
    return notgateobj

def create_new_switch(counter):
    visuals = pygame.Rect(75, 75, 64 ,64)
    name = str(counter)
    gate = Switch(visuals)
    switchobj = {
        "name": name,
        "gate": gate,
        "type": 3
    }    
    return switchobj

def create_new_bulb(counter):
    visuals = pygame.Rect(75, 75, 64 ,64)
    name = str(counter)
    gate = Bulb(visuals)
    bulbobj = {
        "name": name,
        "gate": gate,
        "type": 4
    }    
    return bulbobj

def draw_new_line(counter,startpos, stoppos, lines):
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

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
fullscreen = False
#screen_rect = screen.get_rect()

pygame.display.set_caption("Le Pain")

# - vars -
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
clock = pygame.time.Clock()

running = True

while running:
    # - window scale -
    # scale = 1
    # w, h = pygame.display.get_surface().get_size()
    # a = (w*h)*(10**-5)
    # scale = scale * a

    # - sim clac -
    for obj in objcs:
        obj["gate"].out_Calc(objcs)

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #läuft alle möglichen events durch
            running = False

        
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
                    lines.insert(-1, draw_new_line(linecounter, objcs[start_obj]["name"],objcs[stop_obj]["name"], lines))
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

    

    for obj in objcs:
        screen.blit(obj["gate"].color_Calc(scale),(obj["gate"].visuals[0], obj["gate"].visuals[1]))

    for line in lines:
            for obj in objcs:
                if line["start"] == obj["name"]:
                    pos1 = (obj["gate"].visuals[0]+obj["gate"].image_Scale()[0],obj["gate"].visuals[1]+obj["gate"].image_Scale()[1]/2)
                if line["stop"] == obj["name"]:
                    pos2 = (obj["gate"].visuals[0],obj["gate"].visuals[1]+obj["gate"].image_Scale()[1]/2)
            pygame.draw.line(screen, line["linestate"](line["start"]), pos1, pos2, 5*scale)
    

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()