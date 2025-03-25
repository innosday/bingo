import pygame

class Bingo:
    trun = 1

    def __init__(self,screen:pygame.Surface):
        self.__screen = screen
        self.__id = ""
        self.__flag = False

    @property
    def Id(self):
        return self.__id
    
    def place(self,x,y):
        pygame.draw.rect(self.__screen,[255,255,255],[x,y,100,100],3)
        self.__screen.blit(myFont.render(f"{self.__id}",True,[255,255,255]),[x+10,y])

    def click(self,mousePos,mouseClick,x,y):
        if mouseClick[0]:
            self.__flag = True
        
        if self.__flag and not mouseClick[0]:
            if (x < mousePos[0] < x + 100) and (y < mousePos[1] < y + 100) and self.__id == "":
                if Bingo.trun % 2 == 0:
                    self.__id = "X"
                else:
                    self.__id = "O"
                Bingo.trun += 1
            self.__flag = False

def line(x,a,size):
    for i in range(size):
        b = []
        for j in range(size):
            if a[i][j].Id != "":
                b.append(a[i][j].Id)
        # print(b)
        if b.count(x) != size:
            b =[]
        else:
            return f"{x} bingo"
    
    for i in range(size):
        b= []
        for j in range(size):
            if a[i][j].Id != "":
                b.append(a[j][i].Id)
        # print(b)
        if b.count(x) != size:
            b =[]
        else:
            return f"{x} bingo"

pygame.init()
myFont = pygame.font.SysFont( "arial", 100, True, False)
size=5
screen = pygame.display.set_mode([size*100,size*100])
gird = [[Bingo(screen) for _ in range(size)] for _ in range(size)]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos =pygame.mouse.get_pos()

    for ni,i in enumerate(gird):
        for nj,bingo in enumerate(i):
            bingo.place(ni*100,nj*100)
            bingo.click(mouse_pos,pygame.mouse.get_pressed(),ni*100,nj*100)
            screen.blit(myFont.render(f"{line(bingo.Id,gird,size) if line(bingo.Id,gird,size) != None else ""}",True,[0,255,255]),[screen.get_width()/2 - 100,screen.get_height()/2-80])
    pygame.display.flip()

pygame.quit()