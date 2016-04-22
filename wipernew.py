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

	car1.createcar()		#GENEROWANIE AUT

	everything_appear()		#WYSWIETLANIE WSZYSTKICH KLAS NA EKRANIE

	guycontrols()			#STEROWANIE

	side_interact(guy1, car1)		#INTERAKCJA Z AUTEM - WBIEGANIE

	up_interact(guy1, car1)			#INTERAKCJA Z AUTEM - WSKAKIWANIE

	pygame.display.update()	#ODSWIEZANIE EKRANU

	everything_moves()		#RUCH

	time.tick(FPS)

pygame.quit()
quit()
