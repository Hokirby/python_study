# 라이브러리:

# 프로그래밍을 쉽게 도와주는 도구모음
# 다양한 라이브러리를 자신의 목적에 맞게 사용하면 프로그래밍이 좀 더 쉬워짐

# Pygame(파이게임):

# Python으로 작성 가능한 게임 등의 멀티미디어 표현을 위한 라이브러리

# 공식 사이트: https://www.pygame.org

# 파이게임 설치방법

# pip install 라이브러리명(설치)
# pip install Pygame(Mac은 pip3 사용)
# pip list(확인)

# Pygame 순서

# 1. Pygame 선언 (import)

# 2. pygame 초기화 (pygame.init())

# 3. pygame에서 사용할 전역 변수 선언
# - screen size(x,y)
# - screen(pygame.display.set_mode(size))
# - clock (pygame.time.Clock())

# 4. pygame 메인 루프 (while문)
# - pygame Event 설정
# - pygame 화면 설정
# - 사용자 행위

# 게임 화면 구성

# Red Green Blue (RGB) (0,0,0) ~ (255,255,255)
# 빛의 삼원색으로 빨간색 녹색 파란색을 이용해서 색을 표시하는 방식

# Frame for secopnd (FPS)
# 1초에 화면이 얼마나 다시 그려지느냐의 단위
# 60프레임의 게임: 1초에 60번 화면을 새로 그리는 것

# Project

# - pygame 선언
import pygame

# - pygame에서 사용할 전역 변수 설정
BLACK=(0,0,0)
pad_width=480
pad_height=640

# - 게임 실행과 관련된 로직을 구현
def runGame():
    global gamepad, clock
    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                ongame-True
        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


# - 게임 초기화와 관련된 로직을 구현
def initGame():
    global gamepad, clock
    pygame.init()
    gamepad=pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caution("MY PYGAME")
    clock=pygame.time.Clock()

    runGame()
    initGame()