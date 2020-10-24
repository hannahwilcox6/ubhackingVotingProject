import pygame

pygame.init()

#  game window, with height and width
screen = pygame.display.set_mode((1500, 600))
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
pygame.display.set_caption("UBHacking Voting 2020")
icon = pygame.image.load("vote.png")
pygame.display.set_icon(icon)
running = True

# Player
playerImg = pygame.image.load("standing-up-man-.png")
playerX = 370
playerY = 480
playerMove = 0


def player():
    screen.blit(playerImg, (playerX, playerY))

def quizBackground():
    rect = pygame.Surface((1000, 750))  # the size of your rect
    rect.set_alpha(128)  # alpha level
    rect.fill((255, 255, 255))
    screen.blit(rect,(0,0))

quizScreen = False


while(running == True):
    screen.fill((128, 242, 233))
    # Keeping track of the state of the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If it closes, we quit.
            running = False
        # User interaction events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: #Left
                playerMove = -.2
            if event.key == pygame.K_d: #Right
                playerMove = .2
            if event.key == pygame.K_e: #AND collision
                quizScreen = True

        if event.type == pygame.KEYUP: #User interaction ends.
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerMove = 0
    playerX += playerMove
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1436:
        playerX = 1436
    player()
    if(quizScreen == True):
        quizBackground()
    pygame.display.update()