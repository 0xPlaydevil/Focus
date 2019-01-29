import pygame
from pygame.locals import *
from sys import exit
import random
import time

pygame.init()
SCREENSIZE = (700,500)
screen = pygame.display.set_mode(SCREENSIZE,pygame.RESIZABLE)
pygame.display.set_caption("Empty and Focus")
pygame.display.set_icon(pygame.image.load("icon.jpg"))

fonts = ("Monaco","Segoe UI","微软雅黑","Times New Roman","Calibri","Cambria")
font = pygame.font.SysFont(fonts[5],50)
font_height = font.get_linesize()
numbers = list(range(1,26))
random.shuffle(numbers)
targetNum = 1
mouseDownPos = [0,0]
pressed = -1
showSummary = False
startTime = 0
countTime = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYUP:
			# 初始化新的一局
			if event.key == pygame.K_r:
				random.shuffle(numbers)
				targetNum = 1
				countTime =0
				showSummary = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseDownPos[0] = event.pos[0]//(font_height*1.5)
			mouseDownPos[1] = event.pos[1]//(font_height*1.5)
			pressed = mouseDownPos[1]*5+mouseDownPos[0]
			if numbers[int(pressed)] ==1 and targetNum ==1:
				startTime = time.time()
				print("开始")
			if numbers[int(pressed)] == targetNum:
				targetNum += 1
				if targetNum ==26:
					# 游戏结束，显示结果
					showSummary = True
					countTime = time.time()-startTime
					print(countTime)
		if event.type == pygame.MOUSEBUTTONUP:
			pressed = -1
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.fill((220,220,220))
	for i in range(25):
		screen.blit(font.render(str(numbers[i]),True,(0,160,0) if i==pressed else (5,5,5)),(i%5*font_height*1.5,i//5*font_height*1.5))
	screen.blit(font.render(str(targetNum),True,(220,192,0)),(5*font_height*1.5,30))
	if showSummary:
		screen.blit(font.render(str(countTime),True,(0,64,255)),(5*font_height*1.5,200))
	pygame.display.update()

