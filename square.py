import pygame

pygame.init()

screen=pygame.display.set_mode((600, 600))
screen.fill(("blue"))
pygame.display.update()

class Square:
    def __init__(self,width,height,color,pos):
        self.width=width
        self.height=height
        self.color=color
        self.pos=pos
    def draw(self,screen):
        self.draw_square=pygame.draw.rect(screen,self.color,(self.pos[0],self.pos[1],self.width,self.height))
    
    def grow(self,g):
        self.width+=g
        self.height+=g
        self.draw_square=pygame.draw.rect(screen,self.color,(self.pos[0],self.pos[1],self.width,self.height))
        


square=Square(20,20,"green",(300,300))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("blue")
            square.draw(screen)
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill("blue")
            square.grow(20)
            pygame.display.update()

pygame.quit()
