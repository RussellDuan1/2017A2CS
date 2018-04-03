import pygame 
from pygame.locals import *
from sys import exit 
   
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
   
# 初始化游戏 
pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32) 
pygame.display.set_caption('Can you survive 50 seconds?')
points = []
   
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            # 按任意键可以清屏并把点回复到原始状态
            points = []
            screen.fill((255,255,255))
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            pygame.draw.rect(screen,(0,0,255),Rect(200,200,120,120),0)
            pygame.draw.rect(screen,(0,0,255),Rect(800,200,120,120),0)
            pygame.draw.rect(screen,(0,0,255),Rect(200,800,120,120),0)
            pygame.draw.rect(screen,(0,0,255),Rect(800,800,120,120),0)
            pygame.draw.rect(screen,(255,0,0),Rect(400,400,120,120),0)
     

