import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("nos game")

# 배경 이미지 불러오기
background = pygame.image.load("C:/PyCharm Community Edition 2021.1.2/pycharm_project/pygame/background.jpg")

# 이벤트 루프
running = True # 게임이 진행 중?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 프레임당 게임 화면 그려주기 업데이트

# 종료처리
pygame.quit()