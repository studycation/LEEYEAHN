#병아리(플레이어)에 적용될 클래스를 생성. 
# 플레이어 클래스 객체가 생성되면 자동으로 사진을 불러오고 위치 설정을 해 준다음 move 함수를 만들어 왼쪽 키보드를 누르고 왼쪽으로 이동하고, 오른쪽 키보드를 누르면 오른쪽으로 이동하는 함수를 만들어주겠음. 
# 그리고 추후 폭탄이랑 부딫혔을 때 다른 이미지로 바꿔주기 위해 충돌 시 위치를 return받도록 하겠다. 

## 게임 내에서 동작할 클래스 설정 ##

###pygame 불러오기 필수!!!!
import pygame
from pygame.locals import *

## 플레이어에게 적용할 클래스 
class Player(pygame.sprite.Sprite):
    #플레이어 이미지 로딩 및 설정 함수 
    def __init__(self):
        super().__init__()
        #플레이어 사진 불러오기 
        self.image=pygame.image.load('chick.png')
        #이미지 크기의 직사각형 모양 불러오기 
        self.rect=self.image.get_rect()
        #rec 크기 축소(충돌판전 이미지에 맞추기 위함)
        self.rect=self.rect.inflate(-20,-20)
        print("플레이어:", self.rect)
        #이미지 시작 위치 설정 
        self.rect.center=(540, 390)

    #플레이어 키보드움직임 설정 함수 
    def move(self):
        prssdKeys=pygame.key.get_pressed()
        #왼쪽 방향키를 누르면 5만큼 왼쪽 이동 
        if self.rect.left>0:
            if prssdKeys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                position_p=self.rect.center
                return position_p
        #오른쪽을 누르면 만큼 오른쪽으로 이동 
        if self.rect.right < 640:
            if prssdKeys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                position_p = self.rect.center
                return position_p