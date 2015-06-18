#importing modules
import pygame
from pygame.locals import *  
  
#initializing variables
pygame.init()
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Key Press Test")
f1=pygame.font.SysFont("comicsansms",24)
  
#main loop which displays the pressed keys on the screen
while True:
    event = pygame.event.poll()
    if event.type == pygame.NOEVENT:
        continue
    if event.type == pygame.QUIT:
        break
    if not pygame.key.get_focused():
        continue

    names = [pygame.key.name(i) for i, is_pressed in enumerate(pygame.key.get_pressed()) if is_pressed]
    if 'escape' in names:
        break

    ys = [100 * i for i in range(1, 1 + len(names))]
    screen.fill((255,255,255))
    for name, y in zip(names, ys):
        text = f1.render(name, True, (0, 0, 0))
        screen.blit(text, (100, y))

    pygame.display.update()
          
          
