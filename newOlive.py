#New Pygame explorations
import pygame
import sys

pygame.init()

sWidth = 1500
sHeight = 1000
size = (sWidth, sHeight)
FPS = 20
clock = pygame.time.Clock() #allows you to do a wait

#colors
skyColor = (66, 215, 244)

screen = pygame.display.set_mode(size) #display
pygame.display.set_caption('My New Game')

#game images
car1 = pygame.image.load("images/redCar.png").convert_alpha()
cDim = car1.get_rect()
cTSize = 0.60
car1IW = int(cDim[2] * cTSize)
car1IH = int(cDim[3] * cTSize)
car1 = pygame.transform.scale(car1, (car1IW, car1IH))

#game initial locations
carX = 10
carY = 10

done = False

while not done:

    # 1 -- Capture Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

        print(event)  #this is for bug checking
        
    # 2 -- Do Game Events
    

    # 3 -- Do Window drawing stuff
    screen.fill(skyColor)
    screen.blit(car1, (carX, carY))
    
    pygame.display.flip()
    clock.tick(FPS)
    




#probably redundant     
pygame.quit()
sys.exit()

