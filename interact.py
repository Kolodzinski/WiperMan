from variables import *
from messages import*
from cleaning import cleaningLoop
from other import *
from variables import *

def up_interact(guy, car):
	d = 0                    #numer auta w liscie is_dirty
	neckX, neckY = guy.neck_point        #z neck guy pobieramy wspolrzedne karku aby rysowac reke w cleaningLoop
	cleaningy = car.cary
	foot1_x, foot1_y = guy.foot1_point
	foot2_x, foot2_y = guy.foot2_point
	for i in car.everycarx:
		#if i <= foot1_x < i + car.width and foot2_y >= car.cary or i <= foot2_x < i + car.width and foot2_y >= car.cary:
		#if guy1.feetX >= i and guy1.feetX < i + car1.car_width and guy1.feetY >= car1.cary or guy1.feetX1 >= i and guy1.feetX1 < i + car1.car_width and guy1.feetY1 >= car1.cary:
		if foot1_x >= i and foot1_x < i + car1.width and foot1_y >= car1.cary or foot2_x >= i and foot2_x < i + car1.width and foot2_y >= car1.cary:
			guy.go_down = False                    #jezeli na nim stoimy na wyznaczonym dachu samochodu czlowiek przestaje opadac
			if car.is_dirty[d]:                    #sprawdzamy rodzaj auta na ktore aktualnie wskoczylismy: 1 - brudne
				guy.spongeinhand = False            #obiekt guy1 przestaje rysowac reke z gabka
				cleaningLoop((i), cleaningy, gameDisplay, neckX, neckY, everything_appear)#wlaczamy petle mycia
				guy.Score += 30
				guy.spongeinhand = True            #guy1 znowu rysuje reke z gabka
				guy.guyx = i + car.width +30    #przesowamy guy1 przed auto
			else:
				guy.Score -= 1
		if foot1_x and foot2_x >= i + car.width:
			if guy.go_up == False:                    #gdy guy znajdzie sie przed car znowu zaczyna opadac
				guy.go_down = True
			guy.oncar = False
		d += 1                                        #dodajemy nr auta aby pokrywal sie on z nr samochodu ktory sprawdzamy


def side_interact(guy, car):
	foot1_x, foot1_y = guy.foot1_point
	foot2_x, foot2_y = guy.foot2_point
	knee1_x, knee1_y = guy.knee1_point
	knee2_x, knee2_y = guy.knee2_point
	for i in car.everycarx:    #dla kazdego x car1 definiujemy bok samochodu w ktory nie wolno wbiegac
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
