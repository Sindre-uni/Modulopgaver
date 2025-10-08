import pygame
import math
from datetime import datetime


# Lav skærmen
pygame.init()
screen_size = (640,480)
screen = pygame.display.set_mode(screen_size)
screen.fill((255,255,255))

# Definer centrum og farve
centrum = (screen_size[0]/2,screen_size[1]/2)
farve = [0,0,0]

# Tegn uret
while True:
    screen.fill((255, 255, 255))

# Tegn timemarkeringer
    for i in range(1,13):
        radius = 220
        angle = 360/12 * i
        end_offset = [radius*math.cos(math.radians(angle)),radius*math.sin(math.radians(angle))]
        end_pos = [centrum[0]+end_offset[0],centrum[1]+end_offset[1]]
        start_pos = [centrum[0]+end_offset[0] * 0.8,centrum[1]+end_offset[1] * 0.8]
        pygame.draw.line(screen,farve,start_pos,end_pos)

# Tegn time-, minut- og sekundvisere
    enheder = ["second","minute","hour"]
    for enhed in enheder:
        tid = getattr(datetime.now(),enhed)
        if enhed == "second":
            angle = 360/60*tid - 90
            radius = 220
            bredde = 3
        elif enhed == "minute":
            angle = 360/60*tid - 90
            radius = 200
            bredde = 5
        else:
            angle = 360/12*tid - 90
            radius = 120
            bredde = 8
        end_offset = [radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle))]
        end_position = (centrum[0]+end_offset[0], centrum[1]+end_offset[1])
        pygame.draw.line(screen, farve, centrum, end_position, bredde)
    pygame.display.flip()

# Lader os lukke programmet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()