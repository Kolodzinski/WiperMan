import pygame
import time
import random
pygame.init()
from variables import *
from interact import *
from other import *
from Guy import *
from Car_and_Background import *

while not gameExit:

	car1.createcar()		#generate the car

	everything_appear()		#display everything on the screen

	guycontrols()			#STEROWANIE

	side_interact(guy1, car1)		#interact with the car - runing into

	up_interact(guy1, car1)			#interact with the car - jumping on

	pygame.display.update()	#refreashing the screen

	everything_moves()		#movement

	time.tick(FPS)			#frames

pygame.quit()
quit()
