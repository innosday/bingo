import pygame

class Bingo:
    def __init__(self,screen:pygame.Surface):
        self.__screen = screen
        self.__id = None
    def place(self,x,y):
        pygame.draw.rect(self.__screen,[255,255,255],[x,y,100,100],3)

    def click(self,mouse:tuple):



pygame.init()
size=3
screen = pygame.display.set_mode([size*100,size*100])
gird = []

for i in range(size):
    in_gird = []
    for j in range(size):
        in_gird.append(Bingo(screen))
    gird.append(in_gird)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ni,i in enumerate(gird):
        for nj,j in enumerate(i):
            j.place(ni*100,nj*100)
            print(j)

    mouse =pygame.mouse.get_pressed()
    

    pygame.display.flip()

pygame.quit()