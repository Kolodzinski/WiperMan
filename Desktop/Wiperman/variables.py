import pygame
from Guy import Guy
from Car_and_Background import Car, Background
gameExit = False

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = int(DISPLAY_WIDTH/2)
COLOURS = {
	'BLACK': (0,0,0),
	'GRAY': (45,45,45),
	'WHITE': (255,255,255),
	}

movePerFrame = int(10)

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
spongeinhand = True
bythecar = False
LEVELZERO = DISPLAY_HEIGHT*0.8	#on this level guy and car appears
FPS = 50
time = pygame.time.Clock()	#need it to set the frame rate
				#seting the objects
guy1 = Guy(gameDisplay, DISPLAY_WIDTH, DISPLAY_HEIGHT, LEVELZERO, movePerFrame, COLOURS)
car1 = Car(gameDisplay, DISPLAY_WIDTH, LEVELZERO, movePerFrame, spongeinhand)
background1 = Background(gameDisplay, DISPLAY_WIDTH, movePerFrame )
