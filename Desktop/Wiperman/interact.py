from variables import *
from messages import*
from cleaning import cleaningLoop
from other import *
from variables import *

def up_interact(guy, car):
	d = 0                    #numer auta w liscie is_dirty
	cleaningy = car.cary	#cleaningY is on the same level as carY
	foot1_x, foot1_y = guy.foot1_point	#seting the foot coordinates
	foot2_x, foot2_y = guy.foot2_point
	for i in car.everycarx:
		#if i <= foot1_x < i + car.width and foot2_y >= car.cary or i <= foot2_x < i + car.width and foot2_y >= car.cary:
		#if guy1.feetX >= i and guy1.feetX < i + car1.car_width and guy1.feetY >= car1.cary or guy1.feetX1 >= i and guy1.feetX1 < i + car1.car_width and guy1.feetY1 >= car1.cary:
		if foot1_x >= i and foot1_x < i + car1.width and foot1_y >= car1.cary or foot2_x >= i and foot2_x < i + car1.width and foot2_y >= car1.cary:
			guy.go_down = False                    #if guys feet gets on the car guy stops getting down
			if car.is_dirty[d]:                    #sprawdzamy rodzaj auta na ktore aktualnie wskoczylismy: 1 - brudne
				guy.spongeinhand = False            #obiekt guy1 przestaje rysowac reke z gabka
				cleaningLoop((i), cleaningy, gameDisplay, neckX, neckY, everything_appear)#starting cleaning loop
				guy.Score += 30
				guy.spongeinhand = True            #guy has a sponge in his hand
				guy.guyx = i + car.width +30    #moveing guy in fron of the car
			else:
				guy.Score -= 1					#if car wasnt dirte player loses points
		if foot1_x and foot2_x >= i + car.width:
			if guy.go_up == False:                    #if guy went over the car and he is not getting up he starts getting down
				guy.go_down = True
			guy.oncar = False
		d += 1                                        #adding the is dirty car index


def side_interact(guy, car):
	foot1_x, foot1_y = guy.foot1_point
	foot2_x, foot2_y = guy.foot2_point
	knee1_x, knee1_y = guy.knee1_point
	knee2_x, knee2_y = guy.knee2_point
	for i in car.everycarx:    #with every carX we check a car left surface if a guys foot hit it
		if foot1_x >= i and foot1_x < i + car1.width and foot1_y >= car1.cary or foot2_x >= i and foot2_x < i + car1.width and foot2_y >= car1.cary:
			if guy.guyy == LEVELZERO:

		#if foot1_y > car.cary and (i <= foot1_x -10 and i >= foot1_x +10) or foot2_y > car.cary  and  (i <= foot2_x -10 and i >= foot2_x +10):
		#	if knee1_y > car.cary and  (i <= knee1_x -10 and i >= knee1_x +10) or knee2_y > car.cary  and  (i <= knee1_x -10 and i >= knee1_x +10):
				crash()
				guy.Score-= 1
				guy.bythecar = True

		#if guy1.kneeX >= i and guy1.feetY > car1.cary + 5 and guy1.kneeX <= i + car1.car_width or guy1.kneeX1 >= i and guy1.feetY1 > car1.cary + 5 and guy1.kneeX1 <= i + car1.car_width:

def crash():
	message("You hit a car!")
