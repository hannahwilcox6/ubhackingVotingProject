import pygame

class Quiz:
    display_width = 375
    display_height = 275
    quizActive = False

    def __init__(self,screen,text):
        self.screen = screen
        self.text = text

    def actions(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                d = 4
            if event.key == pygame.K_b:
                d = 4
            if event.key == pygame.K_c:
                d = 4
            if event.key == pygame.L_d:
                d = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                self.playerX_change = 0

    def text_objects(self, text, font):
        black = (0, 0, 0)
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def draw(self,message):
        if(message == "C"):
            self.correctAnswer(self)
        elif(message == "I"):
            self.incorrectAnswer(self)

    def message_display(self):
        # Quiz Question:
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = self.text_objects("Quiz Question: ", largeText)
        textRect.center = ((self.display_width * 2), (self.display_height + 30))
        self.screen.blit(textSurf, textRect)
        # [Actual Question]
        addH = 100
        for question in self.text:
            largeText = pygame.font.Font('freesansbold.ttf', 25)
            textSurf, textRect = self.text_objects(question, largeText)
            textRect.center = ((self.display_width * 2), (self.display_height + 70))
            self.screen.blit(textSurf, textRect)
            for answer in self.text[question]:
                largeText = pygame.font.Font('freesansbold.ttf', 20)
                textSurf, textRect = self.text_objects(answer, largeText)
                textRect.center = ((self.display_width * 2), (self.display_height + addH))
                self.screen.blit(textSurf, textRect)
                addH += 35
        pygame.display.update()

    def correctAnswer(self):
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = self.text_objects("Correct!", largeText)
        textRect.center = ((self.display_width * 2), (self.display_height + 30))
        self.screen.blit(textSurf, textRect)
        pygame.display.update()

    def incorrectAnswer(self):
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = self.text_objects("Incorrect!", largeText)
        textRect.center = ((self.display_width * 2), (self.display_height + 30))
        self.screen.blit(textSurf, textRect)
        pygame.display.update()

    def quizBackground(self):
        if (self.quizScreen and self.quizActive):
            rect = pygame.Surface((700, 300))  # the size of your rect
            #rect.set_alpha(300)  # alpha level
            rect.fill((255, 255, 255))
            self.screen.blit(rect, (375, 275))
            self.message_display(self.test1)