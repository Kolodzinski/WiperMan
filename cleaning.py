import pygame
pygame.init()
import time
from messages import *
from other import *
def cleaningLoop(cleaningx, cleaningy, gameDisplay, neckX, neckY, everything_appear):
	black = (0,0,0)
	grey = (80,80,80)
	cleaning_display_width = 120	#szerokosc i wysokosc dobrane odpowiednio do wielosci obrazkow
	cleaning_display_height = 60

	cleanpart = []			#lista X i Y gdzie byla gabka
	cleanpart1 = []			#lista X i Y gdzie byla gabka bez powtorzen
	sponge_size = 20		#wielnosc gabki
	cleaningExit = False
	spongeX = cleaningx		#wspolrzedne gabki
	spongeY = cleaningy
	spongemoveX = 0 		#przesuniecie poziome
	spongemoveY = 0			#przesuniecie pionowe
	cleaning_clock = pygame.time.Clock()
	cleaninc_FPS = 15

	def cleaning(sponge_size, sponge):
		cleanpieces = []		#tablica na kawalki obrazka czystego auta
		sponge_size = 20		#wielkosc gabki = wys i szer kawalka
		x, y = 0,0				#x i y wycinania z gory i z lewej, zaczyamy od odsuniecia czyli krawedzi obrazka
		d, z = 0,0				#zakres wycinania z gory i z lewej, od x i y do wycinanego kwadratu
		x1, y1 = 20, 20			#x i y wycinania z dolu i z prawej
		d1, z1 = 140, 60		#zakres wycinania z dolu i z prawej
		carsurface = (cleaning_display_height*cleaning_display_width)/(sponge_size*sponge_size)#powierzchania auta podzielona na powierzchnie gabki
		cleanalfa = pygame.image.load('./graphics/alfa.png')
		while len(cleanpieces) <= carsurface:
			img = cleanalfa		#za kazdym razem ladujemy od nowa obrazek
			cleanpieces.append(pygame.transform.chop(pygame.transform.chop(img,(x1,y1, d1,z1)),(x,y,d,z)))#dodajemy wyciety kawalek do tablicy
			d += 20				#wycinamy kawalki wzdluz wierszy, presuwajac zakres wyciecia w prawo
			x1 += 20			#przesowamy x od ktorego wycinamy z prawej
			if x1 == 140:		#dochodzac do krawedzi wiersza
				x1 = 20			#zaczynamy od poczatku krawec wyciecia z prawej
				d = 0			#od poczatku wyciecie z lewej
				z +=20			#zwiekszamy zakres wyciecia z gory usowajac wiersz znajdujacy sie wyzej
				y1+=20			#obnizamy y wyciecia z dolu

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
		# reka myjaca auto

		gameDisplay.blit(spongeIMG, ((cleanpart[-1][0], cleanpart[-1][1])))
		#wklejanie zdjecia w miejsce - [0] i [1] z ostatniej listy w cleanpart


	while cleaningExit == False:
		if spongeX <= cleaningx:	#zatrzymywanie gabki na brzegach auta
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
					if not spongeX <= cleaningx:					#ograniczenie dalszego ruchu po dotarciu do brzegu
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
		#wklejanie wszystkiego, zaslania poprzednie miejsca myjacej reki
		carsurface = (cleaning_display_height*cleaning_display_width)/(sponge_size*sponge_size)
		#wszystkie mozliwe miejsca dla gabki

		sponge = []						#lista ze wspolrzednych gabki
		sponge.append(spongeX)			#dodajemy wspolrzedna x
		sponge.append(spongeY)			#dodajemy wspolrzedna y
		cleanpart.append(sponge)		#lista ze wspolrzednymu gdzie znajdowala sie gabka
		if sponge not in cleanpart1:
			cleanpart1.append(sponge)	#bez powtorzen lista ze wspolrzednymu gdzie znajdowala sie gabka
		if len(cleanpart1) == carsurface:#jezeli dlugosc listy bez powtorzen == wszystkie
			cleaningExit = True			#wylaczamy mycie szyby

		cleaning(sponge_size,sponge)
		pygame.display.update()
		cleaning_clock.tick(cleaninc_FPS)
