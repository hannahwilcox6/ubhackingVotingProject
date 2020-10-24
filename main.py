import pygame
pygame.init()

#  game window, with height and width
screen = pygame.display.set_mode((1500,600))
#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
pygame.display.set_caption("UBHacking Voting 2020")
icon = pygame.image.load("vote.png")
pygame.display.set_icon(icon)

running = True

class Player:
    playerX_change = 0
    playerY_change = 0
    quizScreen = False

    def __init__(self, img, x, y):
        self.playerImg = pygame.image.load(img)
        self.playerX = x
        self.playerY = y

    def actions(self):
        if player.playerX <= 0:
            player.playerX = 0
        elif player.playerX >= 1436:
            player.playerX = 1436
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change -= 0.2
            if event.key == pygame.K_RIGHT:
                self.playerX_change += 0.2
            if event.key == pygame.K_e:
                self.quizScreen = True
                #player.quizBackground()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                self.playerX_change = 0

    def player(self):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
        self.playerX += self.playerX_change
        self.playerY += self.playerY_change

    def quizBackground(self):
        if self.quizScreen:
            rect = pygame.Surface((1000, 750))  # the size of your rect
            rect.set_alpha(128)  # alpha level
            rect.fill((255, 255, 255))
            screen.blit(rect, (0, 0))



player = Player("standing-up-man-.png", 370, 480)
while running:
    screen.fill((128, 242, 233))
    # Window is closed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Checks if player is hitting buttons
    player.actions()

    player.player()
    player.quizBackground()
    pygame.display.update()