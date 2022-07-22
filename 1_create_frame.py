import pygame

pygame.init()#초기화

#화면 크기
screen_width = 480
screen_height = 640
pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀
pygame.display.set_caption('kimsd')

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:#창 닫을 시
            running = False#게임이 진행중이 아님
            
#pygame 종료
pygame.quit()
