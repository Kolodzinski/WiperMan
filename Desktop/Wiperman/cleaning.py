import pygame
pygame.init()
import time
from messages import *
from other import *
def cleaningLoop(cleaningx, cleaningy, gameDisplay, neckX, neckY, everything_appear):
	black = (0,0,0)
	grey = (80,80,80)
	cleaning_display_width = 120	#heith and widht set the same as are img dimensions
	cleaning_display_height = 60

	cleanpart = []			#list of Xs and Ys where the sponge has been
	cleanpart1 = []			#the same list with no duplicates
	sponge_size = 20		#sponge size
	cleaningExit = False
	spongeX = cleaningx		#sponge coordinates
	spongeY = cleaningy
	spongemoveX = 0 		#horizontally movement
	spongemoveY = 0			#perpacidulary movement
	cleaning_clock = pygame.time.Clock()
	cleaninc_FPS = 15

	def cleaning(sponge_size, sponge):
		cleanpieces = []		#list for the clean car pices
		sponge_size = 20		#sponge size = height and width
		x, y = 0,0				#X and Y, top left of the cleaning display
		d, z = 0,0				#scope of cutting, left and top, od x i y do wycinanego kwadratu
		x1, y1 = 20, 20			#x and y of cutting on the bottom and on the righ
		d1, z1 = 140, 60		#scope of cutting on the buttom and on the right
		carsurface = (cleaning_display_height*cleaning_display_width)/(sponge_size*sponge_size)#car surface divided by sponge surface
		cleanalfa = pygame.image.load('./graphics/alfa.png')
		while len(cleanpieces) <= carsurface:
			img = cleanalfa		#getting a new img
			cleanpieces.append(pygame.transform.chop(pygame.transform.chop(img,(x1,y1, d1,z1)),(x,y,d,z)))#chopping a piece and put it into the clean pieces list
			d += 20				#cut pieces along the row moveing cuting scope right
			x1 += 20			#moveing x right
			if x1 == 140:		#when we get to the end of the row
				x1 = 20			#setting the right edge on the beggining
				d = 0			#setting the left edg on the begginging
				z +=20			#getting upper cutting scope one level lower
				y1+=20			#getting bottom scope of cutting

		r = cleanpart1[0][0]
		for i in cleanpart1:		#wstawianie kwadratu po kolei w umyte miejsce
			Rows = [
				[0, cleaningy], [6, cleaningy + sponge_size], [12, cleaningy + 2*sponge_size]
				]
			for j in Rows:
				if i[1] == j[1]:
					x = 0
					while x < 6*sponge_size:
						if i[0] == r + x:
							gameDisplay.blit(cleanpieces[j[0]], (i[0],i[1]))
						x += sponge_size
						j[0] += 1

		spongeIMG = pygame.image.load('./graphics/sponge.png')
		pygame.draw.line(gameDisplay, black, (neckX, neckY), (cleanpart[-1][0], cleanpart[-1][1]), 10)
		# hand which cleans the car

		gameDisplay.blit(spongeIMG, ((cleanpart[-1][0], cleanpart[-1][1])))
		#putting the sponge on the last place where is was


	while cleaningExit == False:
		if spongeX <= cleaningx:	#wer stoping the sponge when it gets to the end of the car
			spongemoveX = 0
		if spongeX >= cleaningx + cleaning_display_width - sponge_size:
			spongemoveX = 0
		if spongeY <= cleaningy:
			spongemoveY = 0
		if spongeY >= cleaningy + cleaning_display_height - sponge_size:
			spongemoveY = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if not spongeX <= cleaningx:					#checkng if sponge is not at the end of the car
						spongemoveX =  - sponge_size
						spongemoveY = 0
				elif event.key == pygame.K_RIGHT:
					if not spongeX >= cleaningx + cleaning_display_width - sponge_size:
						spongemoveX = + sponge_size
						spongemoveY = 0
				elif event.key == pygame.K_UP:
					if not spongeY <= cleaningy:
						spongemoveX = 0
						spongemoveY = - sponge_size
				elif event.key == pygame.K_DOWN:
					if not spongeY >= cleaningy + cleaning_display_height - sponge_size:
						spongemoveX = 0
						spongemoveY = + sponge_size

		spongeX += spongemoveX
		spongeY += spongemoveY

		everything_appear()
		message("Clean!!!")
		#we have to appear everything to cover what was there before
		carsurface = (cleaning_display_height*cleaning_display_width)/(sponge_size*sponge_size)
		#wszystkie mozliwe miejsca dla gabki

		sponge = [spongeX, spongeY]
		cleanpart.append(sponge)		#list of places where sponge has been
		if sponge not in cleanpart1:
			cleanpart1.append(sponge)	#list with no duplicates
		if len(cleanpart1) == carsurface:#if the carsurface == list there sponge has been with no duplicates it means that the car is cleaned
			cleaningExit = True			#so we turn off the cleaning loop

		cleaning(sponge_size,sponge)
		pygame.display.update()
		cleaning_clock.tick(cleaninc_FPS)
