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

# # Project

# # - pygame 선언
# import pygame

# # - pygame에서 사용할 전역 변수 설정
# BLACK = (0,0,0)
# pad_width = 480
# pad_height = 640

# # - 게임 실행과 관련된 로직을 구현
# def runGame():
#     global gamepad, clock # 전역 변수
#     ongame = False
#     while not ongame: # while True문 True==not False 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 ongame = True # False 처리/break 지원 안하기 때문에 사용
    
#         gamepad.fill(BLACK)
#         pygame.display.update()
#         clock.tick(60)
#     pygame.quit()

# # - 게임 초기화와 관련된 로직을 구현
# def initGame():
#     global gamepad, clock
#     pygame.init()
#     gamepad = pygame.display.set_mode((pad_width, pad_height))
#     pygame.display.set_caption("☆MY PYGAME☆")
#     clock = pygame.time.Clock()

# initGame()
# runGame()

# # Quiz 1

# # 게임 화면 색상을 실행시 마다 랜덤으로 생성되게 하시오

# import pygame

# from random import randrange
# red = randrange(0,256,1)
# green = randrange(0,256,1)
# blue = randrange(0,256,1)
# COLOR = (red, green, blue)

# pad_width = 480
# pad_height = 640

# def runGame():
#     global gamepad, clock # 전역 변수
#     ongame = False
#     while not ongame: # while True문 True==not False 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 ongame = True # False 처리/break 지원 안하기 때문에 사용
    
#         gamepad.fill(COLOR)
#         pygame.display.update()
#         clock.tick(60)
#     pygame.quit()

# def initGame():
#     global gamepad, clock
#     pygame.init()
#     gamepad = pygame.display.set_mode((pad_width, pad_height))
#     pygame.display.set_caption("☆MY PYGAME☆")
#     clock = pygame.time.Clock()

# initGame()
# runGame()

# Quiz 2

# 전투기 배치하기

# pygame.KEYDOWN 키보드 버튼을 눌렀을 때 발생
# pygame.Keyup 키보드 버튼을 눌렀다 땠을 때 발생
# pygame.K_UP 윗쪽 방향키를 눌렀을 대 발생(KEYDOWN 중복)
# pygame.K_DOWN 아래쪽 방향키를 눌렀을 대 발생(KEYDOWN 중복)
# pygame.K_LEFT 왼쪽 방향키를 눌렀을 대 발생(KEYDOWN 중복)
# pygame.K_RIGHT 오른쪽 방향키를 눌렀을 대 발생(KEYDOWN 중복)
# pygame.K_LCTRL 왼쪽 컨트롤키를 눌렀을 대 발생(KEYDOWN 중복)

# import pygame

# from random import randrange
# red = randrange(0,256,1)
# green = randrange(0,256,1)
# blue = randrange(0,256,1)
# COLOR = (red, green, blue)

# pad_width = 480
# pad_height = 640

# fighter_width = 36
# fighter_height = 38

# def drawObject(obj, x, y):
#     global gamepad
#     gamepad.blit(obj, (x,y))

# def runGame():
#     global gamepad, clock, fighter # 전역 변수

#     x = pad_width * 0.45
#     y = pad_height * 0.9
#     x_change = 0

#     ongame = False
#     while not ongame: # while True문 True==not False 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 ongame = True # False 처리/break 지원 안하기 때문에 사용
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x_change -= 5
#                 if event.key == pygame.K_RIGHT:
#                     x_change += 5
            
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     x_change = 0

#         gamepad.fill(COLOR)

#         x += x_change
#         drawObject(fighter,x,y)
                
#         pygame.display.update()
#         clock.tick(60)
#     pygame.quit()

# def initGame():
#     global gamepad, clock, fighter
#     pygame.init()
#     gamepad = pygame.display.set_mode((pad_width, pad_height))
#     pygame.display.set_caption("☆MY PYGAME☆")
#     fighter = pygame.image.load('별의커비.jfif')
#     clock = pygame.time.Clock()

# initGame()
# runGame()

# # Quiz3

# # 화면 바깥으로 안나가게 하기

# import pygame

# from random import randrange
# red = randrange(0,256,1)
# green = randrange(0,256,1)
# blue = randrange(0,256,1)
# COLOR = (red, green, blue)

# pad_width = 480
# pad_height = 640

# fighter_width = 36
# fighter_height = 38

# def drawObject(obj, x, y):
#     global gamepad
#     gamepad.blit(obj, (x,y))

# def runGame():
#     global gamepad, clock, fighter # 전역 변수

#     x = pad_width * 0.45
#     y = pad_height * 0.9
#     x_change = 0

#     ongame = False
#     while not ongame: # while True문 True==not False 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 ongame = True # False 처리/break 지원 안하기 때문에 사용
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x_change -= 5
#                 if event.key == pygame.K_RIGHT:
#                     x_change += 5
            
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     x_change = 0

#         gamepad.fill(COLOR)

#         x += x_change

#         if x < 0:
#             x = 0
#         elif x > pad_width - fighter_width:  #444
#             x= pad_width - fighter_width

#         drawObject(fighter, x, y)
                
#         pygame.display.update()
#         clock.tick(60)
#     pygame.quit()

# def initGame():
#     global gamepad, clock, fighter
#     pygame.init()
#     gamepad = pygame.display.set_mode((pad_width, pad_height))
#     pygame.display.set_caption("☆MY PYGAME☆")
#     fighter = pygame.image.load('별의커비.jfif')
#     clock = pygame.time.Clock()

# initGame()
# runGame()

# # Quiz4

# # 적을 내려오게 하기

# import pygame

# from random import randrange
# red = randrange(0,256,1)
# green = randrange(0,256,1)
# blue = randrange(0,256,1)
# COLOR = (red, green, blue)

# pad_width = 480
# pad_height = 640

# fighter_width = 36
# fighter_height = 38

# enemy_width = 26
# eneymy_height = 20

# def drawObject(obj, x, y):
#     global gamepad
#     gamepad.blit(obj, (x,y))

# def runGame():
#     global gamepad, clock, fighter, enemy # 전역 변수

#     x = pad_width * 0.45
#     y = pad_height * 0.9
#     x_change = 0

#     enemy_x= randrange(0, pad_width-enemy_width)
#     enemy_y = 0
#     enemy_speed = 3

#     ongame = False
#     while not ongame: # while True문 True==not False 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 ongame = True # False 처리/break 지원 안하기 때문에 사용
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x_change -= 5
#                 if event.key == pygame.K_RIGHT:
#                     x_change += 5
            
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     x_change = 0

#         gamepad.fill(COLOR)

#         x += x_change

#         if x < 0:
#             x = 0
#         elif x > pad_width - fighter_width:  #444
#             x= pad_width - fighter_width

#         drawObject(fighter, x, y)

#         enemy_y += enemy_speed
#         drawObject(enemy, enemy_x, enemy_y)

#         pygame.display.update()
#         clock.tick(60)
#     pygame.quit()

# def initGame():
#     global gamepad, clock, fighter, enemy
#     pygame.init()
#     gamepad = pygame.display.set_mode((pad_width, pad_height))
#     pygame.display.set_caption("☆MY PYGAME☆")
#     fighter = pygame.image.load('별탄커비.png')
#     enemy = pygame.image.load('디디디대마왕.webp')
#     clock = pygame.time.Clock()

# initGame()
# runGame()

