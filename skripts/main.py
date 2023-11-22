import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410
ANDIMAGE = pygame.image.load("sprits/andGate.png")
ORIMAGE = pygame.image.load("sprits/orGate.png")
NOTIMAGE = pygame.image.load("sprits/notGate.png")

ANDIMAGE = pygame.transform.scale(ANDIMAGE, (50, 50))
ORIMAGE = pygame.transform.scale(ORIMAGE, (50, 50))
NOTIMAGE = pygame.transform.scale(NOTIMAGE, (50, 50))
# - colors -
lineaktiv = "#3adff0"
lineinaktiv = "#003a40"

FPS = 30

# --- classses --- (CamelCase names)

from Gates import AndGate, OrGate, NotGate
from Components import Switch, Bulb

# --- functions --- (lower_case names)

#types:
#0 = and
#1 = or 
#2 = not
def create_new_andGate(counter):
    visuals = pygame.Rect(75, 75, 50 , 50)
    name = str(counter)
    gate = AndGate()
    andgateobj = {
        "name": name,
        "gate": gate,
        "visuals": visuals,
        "type": 0
    }    
    return andgateobj

def create_new_orGate(counter):
    visuals = pygame.Rect(75, 75, 50 ,50)
    name = str(counter)
    gate = OrGate()
    andgateobj = {
        "name": name,
        "gate": gate,
        "visuals": visuals,
        "type": 1
    }    
    return andgateobj

def create_new_notGate(counter):
    visuals = pygame.Rect(75, 75, 50 ,50)
    name = str(counter)
    gate = NotGate()
    andgateobj = {
        "name": name,
        "gate": gate,
        "visuals": visuals,
        "type": 2,
        "output": False,
    }    
    return andgateobj

def draw_new_line(counter,startpos, stoppos, lines):
    name = str(counter)
    lineobj = {
        "name": name,
        "start": startpos,
        "stop": stoppos,
    }
    return lineobj
# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
fullscreen = False
#screen_rect = screen.get_rect()

pygame.display.set_caption("Tracking System")

# - objects -
highlight = None
highlight2 = None
aktive_obj = None
objcs = []
objscounter = 0
start_obj = None
stop_obj = None
lines = []
linecounter = 0

# - mainloop -
clock = pygame.time.Clock()

running = True

while running:

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
                       if obj["visuals"].collidepoint(event.pos):
                            aktive_obj = num

        if event.type == pygame.MOUSEBUTTONUP:
             if event.button == 1:
                  aktive_obj = None
        if event.type == pygame.MOUSEMOTION:
             if aktive_obj != None:
                objcs[aktive_obj]["visuals"].move_ip(event.rel)

        # - connect lines -
        if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 3:
                  for num, obj in enumerate(objcs):
                       if obj["visuals"].collidepoint(event.pos):
                            start_obj = num
                            highlight = pygame.Rect(float(obj["visuals"][0]-5),float(obj["visuals"][1]-5), float(obj["visuals"][2]+10), float(obj["visuals"][3]+10))
        if event.type == pygame.MOUSEBUTTONUP:
             if event.button == 3:
                if stop_obj != None and start_obj != None:
                    exists = False
                    exists_line = None
                    for num, line in enumerate(lines):
                        if line["start"] == objcs[start_obj]["name"] and line["stop"] == objcs[stop_obj]["name"]:
                            exists = True
                            exists_line = num
                            #print(line["start"],line["stop"], "obj:", objcs[start_obj]["name"],objcs[stop_obj]["name"])
                    if exists == True:
                        lines.pop(num)
                        objcs[stop_obj]["gate"].input_Remove(objcs[start_obj]["name"])
                        start_obj = None
                        highlight = None
                        stop_obj = None
                        highlight2 = None
                        #print("Pop")
                    if exists == False:
                        lines.append(draw_new_line(linecounter, objcs[start_obj]["name"],objcs[stop_obj]["name"], lines))
                        objcs[stop_obj]["gate"].input_Add(objcs[start_obj]["name"])
                        linecounter += 1
                        start_obj = None
                        highlight = None
                        stop_obj = None
                        highlight2 = None
                        #print("Add")
                else:
                    start_obj = None
                    highlight = None
                    stop_obj = None
                    highlight2 = None
        if event.type == pygame.MOUSEMOTION:
             if start_obj != None:
                 for num, obj in enumerate(objcs):
                    if obj["visuals"].collidepoint(pygame.mouse.get_pos()):
                        stop_obj = num
                        highlight2 = pygame.Rect(float(obj["visuals"][0]-5),float(obj["visuals"][1]-5), float(obj["visuals"][2]+10), float(obj["visuals"][3]+10))
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
                    if obj["visuals"].collidepoint(pygame.mouse.get_pos()):
                        objcs.pop(num)
            
    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill("white")

    if highlight != None:
        pygame.draw.rect(screen, "green", highlight)
        pygame.draw.line(screen, lineinaktiv, (float(highlight[0]+30), float(highlight[1])+30), pygame.mouse.get_pos(), 5)
    if highlight2 != None:
        pygame.draw.rect(screen, "green", highlight2)

    

    for obj in objcs:
        if obj["type"] == 0:
            pygame.draw.rect(screen, obj["gate"].color_Calc(), obj["visuals"])
            screen.blit(ANDIMAGE,(obj["visuals"][0], obj["visuals"][1]))
        if obj["type"] == 1:
            pygame.draw.rect(screen, obj["gate"].color_Calc(), obj["visuals"])
            screen.blit(ORIMAGE,(obj["visuals"][0], obj["visuals"][1]))
        if obj["type"] == 2:
            pygame.draw.rect(screen, obj["gate"].color_Calc(), obj["visuals"])
            screen.blit(NOTIMAGE,(obj["visuals"][0], obj["visuals"][1]))

    for line in lines:
            for obj in objcs:
                if line["start"] == obj["name"]:
                    pos1 = (obj["visuals"][0]+38,obj["visuals"][1]+25)
                if line["stop"] == obj["name"]:
                    pos2 = (obj["visuals"][0]+12,obj["visuals"][1]+25)
            pygame.draw.line(screen, lineaktiv, pos1, pos2, 5)
    

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()