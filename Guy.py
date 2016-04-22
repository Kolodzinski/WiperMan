import pygame
import math
from variables import *

class Guy():
	Score = 0
	'''klucze do katow w stawach'''
	bodyPos = 0
	changeBodyPos = 0

	shoulderPos = 0
	shoulderPos1 = 0
	changeShoulderPos = 0
	elbowPos = 0
	elbowPos1 = 0
	changeElbowPos = 0

	hipPos = 0
	hipPos1 = 0
	changeHipPos = 0

	kneePos = 0
	kneePos1 = 0
	changeKneePos = 0

	def __init__(self, gameDisplay, DISPLAY_WIDTH, DISPLAY_HEIGHT, LEVELZERO, movePerFrame, COLOURS):
		self.gameDisplay = gameDisplay
		self.guyx = int(DISPLAY_WIDTH * 0.1)
		self.guyy = LEVELZERO
		self.col = COLOURS
		self.size = DISPLAY_HEIGHT/10	#wielkosc tulowia guy wzgledem ktorej ustalana jest wielkosc reszty cila
		self.width = self.size / 5
		self.head = self.size / 5
		self.arm = self.size / 2
		self.tight = self.size / 1.7
		self.calf = self.size / 2
		self.forearm = self.size / 2.5
		self.levelzero = LEVELZERO
		self.spongeinhand = True
		self.bythecar = False
			#zmienne poruszania
		self.oncar = False
		self.go_up = False
		self.go_down = False
		self.spongeIMG = pygame.image.load('./graphics/sponge.png')
		self.maxJump = self.guyy - 2.2 * self.size
		self.movePerFrame = movePerFrame
	def bodyAngles(self):
		self.PossiblebodyAngle =       [ 270, 300, 330]

		self.PossibleshoulderAngle =   [90,   75,         70,    100,    130,    180,   130,    100]
		self.PossibleelbowAngle =      [90,  330,        300,    340,    350,    120,   350,    340]
		self.PossibleshoulderAngle1 =  [90,  140,        180,    130,     90,     70,   100,    130]
		self.PossibleelbowAngle1 =     [90,   60,         50,    350,    350,    300,   340,    350]

		self.PossiblehipAngle =        [90,   30,         10,     40,    100,    145,   100,     40]
		self.PossiblekneeAngle =       [90,  110,        130,    120,    160,    230,   160,    120]
		self.PossiblehipAngle1 =       [90,  130,        145,    105,     40,     10,    40,    105]
		self.PossiblekneeAngle1 =      [90,  180,        230,    160,    120,    130,   120,    160]

	def wholeBody(self):      # WYZNACZANIE WSPOLZEDNYCH PUNKTOW CIALA
		Guy.bodyAngles(self)
		self.neck_point = (
		    int(self.guyx + math.cos(math.radians(self.PossiblebodyAngle[self.bodyPos])) * self.size),    #wspolzedne szyi wzgledem biodra
		    int(self.guyy + math.sin(math.radians(self.PossiblebodyAngle[self.bodyPos])) * self.size)
		)
		self.head_point = (
			int(self.neck_point[0]),
			int(self.neck_point[1] - self.head)
		)
		self.knee1_point = (
		    self.guyx + math.cos(math.radians(self.PossiblehipAngle[self.hipPos])) * self.tight, #wspolzedne kolana wzgledem biodra
		    self.guyy + math.sin(math.radians(self.PossiblehipAngle[self.hipPos]))  * self.tight
		)
		self.knee2_point = (
			self.guyx + math.cos(math.radians(self.PossiblehipAngle1[self.hipPos])) * self.tight,  #wspolzedne kolana wzgledem biodra
			self.guyy + math.sin(math.radians(self.PossiblehipAngle1[self.hipPos]))  * self.tight
		)

		self.foot1_point = (
			self.knee1_point[0] + math.cos(math.radians(self.PossiblekneeAngle[self.kneePos])) * self.calf, # wspolzedna lydki wzgledem uda
			self.knee1_point[1] + math.sin(math.radians(self.PossiblekneeAngle[self.kneePos])) * self.calf
		)
		self.foot2_point = (
			self.knee2_point[0] + math.cos(math.radians(self.PossiblekneeAngle1[self.kneePos])) * self.calf, # wspolzedna lydki wzgledem uda
			self.knee2_point[1] + math.sin(math.radians(self.PossiblekneeAngle1[self.kneePos])) * self.calf
		)

		self.elbow1_point = (
			self.neck_point[0] + math.cos(math.radians(self.PossibleshoulderAngle[self.shoulderPos])) * self.arm,
			self.neck_point[1] + math.sin(math.radians(self.PossibleshoulderAngle[self.shoulderPos])) * self.arm
		)
		self.elbow2_point = (
			self.neck_point[0] + math.cos(math.radians(self.PossibleshoulderAngle1[self.shoulderPos])) * self.arm,
			self.neck_point[1] + math.sin(math.radians(self.PossibleshoulderAngle1[self.shoulderPos])) * self.arm
		)

		self.wrist1_point = (
			self.elbow1_point[0] + math.cos(math.radians(self.PossibleelbowAngle[self.elbowPos])) * self.forearm,
			self.elbow1_point[1] + math.sin(math.radians(self.PossibleelbowAngle[self.elbowPos])) * self.forearm
		)
		self.wrist2_point = (
			self.elbow2_point[0] + math.cos(math.radians(self.PossibleelbowAngle1[self.elbowPos])) * self.forearm,
			self.elbow2_point[1] + math.sin(math.radians(self.PossibleelbowAngle1[self.elbowPos])) * self.forearm
		)
	def	guy_appirance(self):	#RYSOWANIE CIALA
		Guy.wholeBody(self)
		# Most of these lines are the same when the dude has a sponge and when
		# he hasn't, so unify them
		pygame.draw.line(self.gameDisplay, self.col['BLACK'], (self.guyx,self.guyy), self.neck_point, int(self.width))

		pygame.draw.line(self.gameDisplay, self.col['GRAY'], (self.guyx, self.guyy), self.knee1_point, int(self.width))
		pygame.draw.line(self.gameDisplay, self.col['BLACK'], (self.guyx, self.guyy), self.knee2_point, int(self.width))

		pygame.draw.line(self.gameDisplay, self.col['GRAY'], self.knee1_point, self.foot1_point, int(self.width))
		pygame.draw.line(self.gameDisplay, self.col['BLACK'], self.knee2_point, self.foot2_point, int(self.width))

		pygame.draw.line(self.gameDisplay, self.col['GRAY'], self.neck_point, self.elbow1_point, int(self.width))

		if self.spongeinhand:
			pygame.draw.line(self.gameDisplay, self.col['GRAY'], self.elbow1_point, self.wrist1_point, int(self.width))

			pygame.draw.line(self.gameDisplay, self.col['BLACK'], self.neck_point, self.elbow2_point, int(self.width))
			pygame.draw.line(self.gameDisplay, self.col['BLACK'], self.elbow2_point, self.wrist2_point, int(self.width))
		else:
			pygame.draw.line(self.gameDisplay, self.col['BLACK'], self.elbow1_point, self.wrist1_point, int(self.width))

		pygame.draw.circle(self.gameDisplay, self.col['BLACK'], (int(self.head_point[0]),int(self.head_point[1])), int(self.head))
		pygame.draw.circle(self.gameDisplay, self.col['WHITE'], (int(self.head_point[0] + self.head - 4), int(self.head_point[1] - int(self.head/4))), int(self.head/4))

		if self.spongeinhand == True:
			self.gameDisplay.blit(self.spongeIMG, self.wrist2_point)
	def run(self, GUYX):
		if self.go_up or self.go_down == True:
			self.elbowPos = 2
			self.hipPos = 2
			self.kneePos = 2
			self.bodyPos = 2
			self.shoulderPos = 2
		else:
			self.bodyPos += 1
			self.shoulderPos += 1
			self.elbowPos += 1
			self.hipPos += 1
			self.kneePos += 1
			if self.shoulderPos >= 8:
				self.shoulderPos = 2
				self.elbowPos = 2
				self.hipPos = 2
				self.kneePos = 2
			if self.bodyPos >= 2:
				self.bodyPos = 2
		if self.guyx > GUYX:
			self.guyx -= self.movePerFrame/2
	def jump(self):
		def go_up(self):
			self.bythecar = False
			if self.guyy > self.maxJump:
				self.guyy -= self.movePerFrame
			else:
				self.go_down = True
				self.go_up = False
		def go_down(self):
			if self.guyy < self.levelzero:
				self.guyy += self.movePerFrame
			else:
				self.go_down = False
				self.go_up = False
		if self.go_up == True:
			go_up(self)
		if self.go_down == True:
			go_down(self)
