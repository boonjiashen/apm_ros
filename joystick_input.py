#importing modules
import pygame
from pygame.locals import *
from sys import exit
  
  
#initializing variables
pygame.init()
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Key Press Test")
f1=pygame.font.SysFont("comicsansms",24)
  
#main loop which displays the pressed keys on the screen
while True:
    for i in pygame.event.get():
        #print i
        if i.type==QUIT:
            exit()
        a=100
        screen.fill((255,255,255))

        if not pygame.key.get_focused():
            continue

        names = [pygame.key.name(i) for i, is_pressed in enumerate(pygame.key.get_pressed()) if is_pressed]
        #print names
        if 'escape' in names:
            exit()
        ys = [100 * i for i in range(1, 1 + len(names))]
        for name, y in zip(names, ys):
            text = f1.render(name, True, (0, 0, 0))
            screen.blit(text, (100, y))
        # press=pygame.key.get_pressed()
        # for i in xrange(0,len(press)): 
        #     if press[i]==1:
        #         name=pygame.key.name(i) 
        #         text=f1.render(name,True,(0,0,0))
        #         screen.blit(text,(100,a))
        #         a=a+100
        pygame.display.update()
          
          
