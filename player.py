import pygame

class Player:
    playerX_change = 0
    playerY_change = 0
    quizScreen = False

    def __init__(self, img, x, y):
        self.playerImg = pygame.image.load(img)
        self.playerX = x
        self.playerY = y

    def actions(self, event):
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 1436:
            self.playerX = 1436
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change -= 0.2
            if event.key == pygame.K_RIGHT:
                self.playerX_change += 0.2
            if event.key == pygame.K_e:
                self.quizScreen = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                self.playerX_change = 0

    def draw(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
        self.playerX += self.playerX_change
        self.playerY += self.playerY_change

    def quizBackground(self,screen):
        if self.quizScreen:
            rect = pygame.Surface((1000, 750))  # the size of your rect
            rect.set_alpha(128)  # alpha level
            rect.fill((255, 255, 255))
            screen.blit(rect, (0, 0))
