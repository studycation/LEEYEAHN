###pygame 불러오기 필수!!!!
import pygame
from pygame.locals import *
import random
 

#적에게 적용할 클래스 
class Enemy(pygame.spirite.Sprite):

    #적의 이미지 로딩 및 설정 함수 
    def __init__(self):
        super().__init__()
        #적 사진 불러오기 
        self.image = pygame.image.load('boom2.png')
        #이미지 크기의 직사각형 모양 불러오기 
        self.rect=self.rect.inflate(-20,-20)
        print("wjr: ", self.rect)
        #이미지 시작 위치 설정 
        self.rect.center=(random.randint(40,600), 0)

    #적의 움직임 설정 함수 + 플레이어 점수 측정 
    def move(self):
        global SCORE

        #적을 10픽셀 크기만큼 위에서 아래로 떨어지도록 설정 
        self.rect.move_ip(0, SPEED) #x, y좌표 설정 
        #이미지가 화면 끝에 있으면(플레이어가 물체를 피하면)다시 이미지 위치 세팅 + 1점 추가 
        if (self,rect,bottom>440):
            SCORE +=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 610), 0)
            return self.rect.center
