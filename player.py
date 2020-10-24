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
            if event.key == pygame.K_a:
                self.playerX_change -= 0.25
            if event.key == pygame.K_d:
                self.playerX_change += 0.25
            if event.key == pygame.K_e:
                self.quizScreen = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                self.playerX_change = 0

    def draw(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
        self.playerX += self.playerX_change
        self.playerY += self.playerY_change

    # Questions:
    quiz1 = {"When is the deadline to register to vote?": ["[A] November 3", "[B] October 3", "[C] October 9",
                                                           "[D] December 25"],
             "How old do you need to be to vote?": ["[A] 18", "[B] 21", "[C] 28", "[D] 16"],
             "How can you check your registration status?": ["[A] You can't", "[B] Call the government",
                                                             "[C] Various websites online",
                                                             "[D] Just remember when you did it"]}
    test1 = {"How old do you need to be to vote?": ["[A] 18", "[B] 21", "[C] 28", "[D] 16"]}

    display_width = 375
    display_height = 275
    def text_objects(self,text, font):
        black = (0, 0, 0)
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(self,text, fontSize,screen):
        # Quiz Question:
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = self.text_objects("Quiz Question: ", largeText)
        textRect.center = ((self.display_width * 2), (self.display_height + 30))
        screen.blit(textSurf, textRect)
        # [Actual Question]
        addH = 100
        for question in text:
            largeText = pygame.font.Font('freesansbold.ttf', fontSize)
            textSurf, textRect = self.text_objects(question, largeText)
            textRect.center = ((self.display_width * 2), (self.display_height + 70))
            screen.blit(textSurf, textRect)
            for answer in text[question]:
                largeText = pygame.font.Font('freesansbold.ttf', 20)
                textSurf, textRect = self.text_objects(answer, largeText)
                textRect.center = ((self.display_width * 2), (self.display_height + addH))
                screen.blit(textSurf, textRect)
                addH += 35
        pygame.display.update()

    def quizBackground(self,screen):
        if(self.quizScreen):
            rect = pygame.Surface((700, 300))  # the size of your rect
            rect.set_alpha(200)  # alpha level
            rect.fill((255, 255, 255))
            screen.blit(rect, (375, 275))
            self.message_display(self.test1, 25,screen)