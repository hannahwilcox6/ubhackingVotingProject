import pygame

class Player:
    playerX_change = 0
    playerY_change = 0
    quizScreen = False
    canMove = True

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
            if event.key == pygame.K_a:
                self.playerX_change -= 2
            if event.key == pygame.K_d:
                self.playerX_change += 2
            if event.key == pygame.K_e:
                self.quizScreen = True
                self.canMove = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                self.playerX_change = 0

    def draw(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
        self.playerX += self.playerX_change
        self.playerY += self.playerY_change

    # Questions:
