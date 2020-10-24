import pygame

class NPC:
    def __init__(self, img, x, y):
        self.NPCImg = pygame.image.load(img)
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.NPCImg, (self.x, self.y))