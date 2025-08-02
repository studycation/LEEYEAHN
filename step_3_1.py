import pygame 
from step_1_1 import IN_DIR

def init_pygame(scr_size: tuple[int, int], font_size: int = 30):
    pygame.init() # pygame 패키지 초기화 
    pygame.display.set_caption("슬라이딩 퍼즐")
    screen = pygame.display.set_mode(scr_size)
    font = pygame.font.Font(IN_DIR / "Pretendard-Bold.ttf", size=font_size)
    clock = pygame.time.Clock()
    return screen, font, clock

if __name__ == "__main__":
    width, height = 800, 100
    screen, font, clock = init_pygame((width, height), 15)
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.fill((255, 255, 255)) 
            center = width /2, height / 2 
            text_img = font.render(f"{event=}", True, (0, 0, 0))
            text_bbox = text_img.get_rect(center=center)
            screen.blit(text_img, text_bbox)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# 아래 문단을 step_3_1.py 파일에 넣기 전에는 step_3_2.py가 오류남. 이래 문단 넣으니까 바로 됐는데 왜그런지 지피티한테 물어보셈 아마 변수 수 맞추는 거 땜시 그런듯ㅎ
import pygame

def init_pygame(screen_size):
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    font = pygame.font.SysFont(None, 72)
    clock = pygame.time.Clock()
    return screen, font, clock