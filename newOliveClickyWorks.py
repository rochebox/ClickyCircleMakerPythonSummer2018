#New Pygame explorations
import pygame
import sys
from random import randint

pygame.init()

sWidth = 1500
sHeight = 1000
size = (sWidth, sHeight)
FPS = 40
clock = pygame.time.Clock() #allows you to do a wait

#colors
olive = (29, 122, 51)

#dots
dots = []

screen = pygame.display.set_mode(size) #display
pygame.display.set_caption('The New and Improved')

done = False

def addCircle(newX, newY):
    dotTuple = []
    dotTuple.append(newX)
    dotTuple.append(newY)
    dots.append(dotTuple)
    
def drawCircles():
    #print("drawing circles")
    for dot in dots:
        myColor = (randint(140, 255), randint(140, 255), 255)
        pygame.draw.circle(screen, myColor, dot, randint(40,100))
        

while not done:

    # 1 -- Capture Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

        #print(event)  #this is for bug checking
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseX, mouseY = event.pos
                addCircle(mouseX, mouseY)
            
        
    # 2 -- Do Game Events
    

    # 3 -- Do Window drawing stuff
    screen.fill(olive)
    drawCircles()
    
    pygame.display.flip()
    clock.tick(FPS)
    




#probably redundant     
pygame.quit()
sys.exit()

