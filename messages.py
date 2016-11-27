from variables import *

def textMessages(text, font):
	textSurface = font.render(text, True, COLOURS['BLACK'])
	return textSurface, textSurface.get_rect()

def message(text):
	biggerText = pygame.font.Font('freesansbold.ttf', 150) 	#rodzaj czcionki i wielkosc
	textSurf, textRect = textMessages(text, biggerText)		# powierzchnia i prostokat ktory zawiera text
	textRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
	gameDisplay.blit(textSurf, textRect)
	pygame.display.update()

def scoremessage(text):
	biggerText = pygame.font.Font('freesansbold.ttf', 30) 	#rodzaj czcionki i wielkosc
	textSurf, textRect = textMessages(text, biggerText)		# powierzchnia i prostokat ktory zawiera text
	textRect.center = ((DISPLAY_WIDTH*0.8), (DISPLAY_HEIGHT*0.1))
	gameDisplay.blit(textSurf, textRect)
	pygame.display.update()
