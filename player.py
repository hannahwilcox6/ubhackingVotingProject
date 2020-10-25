import pygame

class Player:
    playerX_change = 0
    playerY_change = 0
    collidedObject = None
    interacting = False
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
        if event.type == pygame.KEYDOWN and self.interacting == False:
            if event.key == pygame.K_a:
                self.playerX_change -= 4
            if event.key == pygame.K_d:
                self.playerX_change += 4
            if event.key == pygame.K_e and self.collidedObject != None:
                self.quizScreen = True
                self.interacting = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                self.playerX_change = 0

    def draw(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
        self.playerX += self.playerX_change
        self.playerY += self.playerY_change

    def collision(self, other):
        if (self.playerX + 64) >= other.x and self.playerX <= (other.x + 64):
            self.collidedObject = other