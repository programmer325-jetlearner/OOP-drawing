import pygame

pygame.init()

screen=pygame.display.set_mode((600, 600))
screen.fill(("red"))
pygame.display.update()

class Circle:
    def __init__(self,radius,width,color,pos):
        self.radius=radius
        self.width=width
        self.color=color
        self.pos=pos
        self.surface=screen
    def draw(self):
        self.draw_circle=pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
    
    def grow(self,r):
        self.radius+=r
        self.draw_circle=pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)

circle=Circle(20,0,"green",(300,300))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill(("red"))
            circle.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill(("red"))
            circle.grow(20)
            pygame.display.update()

pygame.quit()

        




      


