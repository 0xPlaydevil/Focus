import pygame
# from pygame.locals import QUIT
from sys import exit

pygame.init()
SCREEN_SIZE = (768,384)
screen = pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
pygame.display.set_caption("this is my first pygame!")

background = pygame.image.load("effect.jpg")
cursor = pygame.image.load("cube100.png").convert_alpha()
font = pygame.font.SysFont("arial",16)

# 事件循环(main loop)
while True:
	# screen.blit(background,(0,0))
	screen.fill((0,160,0))
	
	# event = pygame.event.wait()
	for event in pygame.event.get():
		screen.blit(font.render("Show a line",True,(0,0,0)),(0,16))

		x,y = pygame.mouse.get_pos()
		x -= cursor.get_width()/2
		y -= cursor.get_height()/2
		screen.blit(cursor,(x,y))

		pygame.display.update()

		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		

