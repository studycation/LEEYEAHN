import pygame, sys
from pygame.locals import*
import random, time

pygame.init()

#초당 프레임 설정
FPS = 60 
FramePerSec = pygame.time.Clock()

#색상 세팅(RGB코드)
RED = (255, 0, 0)
ORANGE = (255, 153, 51)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SEAGREEN = (60, 179, 113)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (204, 153, 255)
PINK = (255, 153, 153)

#게임 진행에 필요한 변수들 설정
SPEED = 5 #게임 진행 속도 
SCORE = 0 # 플레이어 점수 

#폰트 설정 
font = pygame.font.SysFont('Tahoma', 60)  # 기본 폰트 및 사이즈 설정(폰트1)
small_font = pygame.font.SysFont('Malgun Gothic', 20)  # 작은 사이즈 폰트(폰트2)
game_over = font.render("GG", True, BLACK)  # 게임 종료시 문구

#게임 배경화면 
background = pygame.image.load('background1.jpg') #배경화면 사진 로드 

#게임 화면 생성 및 설정
GameDisplay = pygame.display.set_mode((640, 440))
GameDisplay.fill(PINK)
pygame.display.set_caption("Mini Game") #이 줄 무슨 뜻인지 지피티한테 물어봥 

