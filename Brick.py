import pygame

class Brick:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
	self.color = color

    def render(self, window):
        img = pygame.image.load('Assets/brick.png')
        #pygame.draw.rect(window,self.color,(self.x, self.y, self.width, self.height))
        window.blit(img, (self.x, self.y))
