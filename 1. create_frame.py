import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("nos game")

# 이벤트 루프
running = True # 게임이 진행 중?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임은 진행 중이 아님

# 종료처리
pygame.quit()