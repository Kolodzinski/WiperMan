from variables import *
from messages import*

def score():
	score = Score
	score = str(score)
	scoremessage("Score: " + score)

def guycontrols():
	for event in pygame.event.get():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				guy1.run(guy1.guyx)
			if guy1.guyy == guy1.guyy:
				if event.key == pygame.K_UP:
					guy1.go_up = True

def everything_moves():
	guy1.jump()
	if not guy1.bythecar:
		guy1.run(guy1.guyx)
		background1.passing()
		car1.move()

def everything_appear():
	background1.appirance()
	guy1.guy_appirance()
	car1.car_appirance()
	scoremessage("Score: " + str(guy1.Score))
	#score()
