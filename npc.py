import pygame

class NPC:
    def __init__(self, img, x, y, quiz):
        self.NPCImg = pygame.image.load(img)
        self.x = x
        self.y = y
        self.quiz = quiz

    def draw(self, screen):
        screen.blit(self.NPCImg, (self.x, self.y))