import pygame

pygame.init()#초기화

#화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀
pygame.display.set_caption('kimsd')
#배경이미지 불러오기
background = pygame.image.load('C:/Users/SungYul Kim/Desktop/파이썬 공부  파일/gameproject_pygame/background.png')

#캐릭터(스프라이트) 불러오기
character = pygame.image.load('C:/Users/SungYul Kim/Desktop/파이썬 공부  파일/gameproject_pygame/character.png')
character_size = character.get_rect().size # 이미지의 크기 구하기
character_width = character_size[0]#캐릭터의 가로 크기
character_height = character_size[1]#캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height#화면 세로크기 가장 아래에 해당되는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:#창 닫을 시
            running = False#게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:#키가 사라졌는지 확인
            if event.key == pygame.K_LEFT:# 캐릭터를 왼쪽으로
                to_x -= 1
            elif event.key == pygame.K_RIGHT:#캐릭터를 오른쪽으로
                to_x += 1
            elif event.key == pygame.K_UP:#캐릭터를 위로
                to_y -= 1
            elif event.key == pygame.K_DOWN:#캐릭터를 아래로
                to_y += 1

        if event.type == pygame.KEYUP:#방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값 처리:
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height



    screen.blit(background, (0, 0))#배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))#캐릭터 그리기


    pygame.display.update()#게임 화면을 다시 그리기!
            
#pygame 종료
pygame.quit()