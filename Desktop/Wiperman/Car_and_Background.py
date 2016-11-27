import pygame
import random

'''WE CAN ADD AS MANY SURFACES AS WE WANT, ONLY IMAGE BY ADDIN APPROPIATE IMAGE'''

class Background:
	def __init__(self,gameDisplay,DISPLAY_WIDTH, movePerFrame):
		self.gameDisplay = gameDisplay
		self.DISPLAY_WIDTH = DISPLAY_WIDTH
		self.surfaces = [		#here You can add a surface only by adding an image into a new list
						[pygame.image.load('./graphics/clouds.png')],
						[pygame.image.load('./graphics/buildings.png')],
						]

		for i in range(len(self.surfaces)):
			self.surfaces[i].append([DISPLAY_WIDTH - DISPLAY_WIDTH, DISPLAY_WIDTH])#we are adding surfaces_points to every urface image, points are background start and background end
			self.surfaces[i].append(movePerFrame/(i+1)) #we are adding third value which is moving speed, first surface val has the fastest

	def appirance(self):
		for i in self.surfaces:
			for j in i[1]:
				self.gameDisplay.blit(i[0], (j,0))

	def passing(self):
		i = 0
		while i in range(len(self.surfaces)):
			x = 0
			while x in range(2):
				if self.surfaces[i][1][x] <= -self.DISPLAY_WIDTH:
					self.surfaces[i][1][x] = self.DISPLAY_WIDTH
				x+=1
			x=0
			while x in range(2):
				self.surfaces[i][1][x] -= self.surfaces[i][2]
				x+=1
			i+=1
class Car:
	def __init__(self,gameDisplay, DISPLAY_WIDTH, LEVELZERO, movePerFrame, spongeinhand):
		self.cleaningy = LEVELZERO
		self.cary = LEVELZERO
		self.display_width = DISPLAY_WIDTH
		self.height = 60		#dimensions are appropriate to the img
		self.width = 120
		self.gameDisplay = gameDisplay
		self.movePerFrame = movePerFrame
		self.clean = pygame.image.load('./graphics/alfa.png')
		self.dirty = pygame.image.load('./graphics/alfa2.png')
		self.spongeinhand = spongeinhand
		self.everycarx = [self.display_width]				# list of Xs
		self.is_dirty = [False]                                     # lista = False - auto czyste, True - auto brudne									# lista = 0 - auto czyste, 1 - auto brudne
	def createcar(self):
		for i in self.everycarx:
			if i == self.display_width * 0.7:                 # if car get to this point
				# get if car is dirty randomly
				is_dirty = (random.randint(0, 4) == 4) #it puts true only if we get 4 (so false is 4 times more possible)
				self.is_dirty.append(is_dirty)

				self.newcarx = random.randrange(self.display_width, self.display_width + 100, self.display_width * 0.4)
				self.everycarx.append(self.newcarx)                  # dadding a new carx to everycarx list

	def car_appirance(self):
		for i, is_dirty in enumerate(self.is_dirty):
			img = self.dirty if is_dirty else self.clean  #if isdirty == true img is dirtyapfa else clean one
			self.gameDisplay.blit(img, (self.everycarx[i], self.cary))    # we display what w got

	def move(self):
		if not self.spongeinhand:
			return

		for i, x in enumerate(self.everycarx):
			self.everycarx[i] = x - self.movePerFrame

		#if self.spongeinhand == True:
		#	x = 0
		#	for i in self.everycarx:
		#		self.everycarx[x] = i - self.movePerFrame
		#		x += 1
