import pygame
from pygame.locals import *
from sys import exit
import random
import time

# 窗口准备
pygame.init()
SCREENSIZE = (600,500)
screen = pygame.display.set_mode(SCREENSIZE,pygame.RESIZABLE)
pygame.display.set_caption("Empty and Focus")
pygame.display.set_icon(pygame.image.load("icon.jpg"))

fonts = ("Monaco","Calibri","microsoftyaheimicrosoftyaheiui","dengxian","simsunnsimsun","kaiti","Times New Roman")
font = pygame.font.SysFont(fonts[6],50)
font_height = font.get_linesize()
line_width = font_height*1.5

numbers = list(range(1,26))
random.shuffle(numbers)
targetNum = 1
mouseDownPos = [0,0]
pressed = -1
showSummary = False
startTime = 0
countTime = 0
tick = pygame.time.Clock()

btnFont = pygame.font.SysFont(fonts[5],20)
# btnFontPath = pygame.font.match_font(fonts[9])
# print(btnFontPath)
# btnFont = pygame.font.Font(btnFontPath,20)
btnText = "重新开始"
btnRect = pygame.Rect(5*line_width+font_height/4,400,80,40)

while True:
	for event in pygame.event.get():
		# 处理键盘事件
		if event.type == pygame.KEYUP:
			# 初始化新的一局
			if event.key == pygame.K_r:
				random.shuffle(numbers)
				targetNum = 1
				countTime =0
				showSummary = False
		# 处理鼠标键按下事件
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseDownPos[0] = event.pos[0]//line_width
			mouseDownPos[1] = event.pos[1]//line_width
			# 限定响应范围
			if mouseDownPos[0]<=4 and mouseDownPos[1]<=4:
				pressed = mouseDownPos[1]*5+mouseDownPos[0]
				# 响应点击数字
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
		# 处理鼠标键抬起事件
		if event.type == pygame.MOUSEBUTTONUP:
			pressed = -1
			# 初始化新一局
			if btnRect.collidepoint(event.pos):
				random.shuffle(numbers)
				targetNum = 1
				countTime =0
				showSummary = False
		# 处理退出事件
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.fill((220,220,220))
	# 画表格
	for i in range(5):
		pygame.draw.line(screen,(255,160,0),((i+1)*line_width-1,0),((i+1)*line_width-1,5*line_width),2)
		pygame.draw.line(screen,(255,160,0),(0,(i+1)*line_width-1),(5*line_width,(i+1)*line_width-1),2)
	# 写数字
	for i in range(25):
		screen.blit(font.render(str(numbers[i]),True,(0,160,0) if i==pressed else (5,5,5)),(i%5*line_width+font_height/4,i//5*line_width+font_height/4))
	# 显示下一个数
	screen.blit(font.render(str(targetNum),True,(220,192,0)),(5*line_width+font_height/2,20))
	# 游戏结束，显示结果
	if showSummary:
		screen.blit(font.render(str(countTime),True,(0,64,255)),(5*line_width+font_height/4,320))
		btnText = "再试一次"
	else:
		btnText = "重新开始"
	# 绘制按钮
	pygame.draw.rect(screen,(240,240,240),btnRect)
	screen.blit(btnFont.render(btnText,True,(5,5,5)),btnRect.topleft)
	# 刷新画面
	pygame.display.update()
	# 控制帧率，减少性能消耗
	# pygame.time.wait(30)
	tick.tick(10)

