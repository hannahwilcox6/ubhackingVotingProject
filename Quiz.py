import pygame

class Quiz:
    display_width = 375
    display_height = 275

    def __init__(self,text,screen):
        self.text = text
        self.screen = screen

    def text_objects(self, text, font):
        black = (0, 0, 0)
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, fontSize):
        # Quiz Question:
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = self.text_objects("Quiz Question: ", largeText)
        textRect.center = ((self.display_width * 2), (self.display_height + 30))
        self.screen.blit(textSurf, textRect)
        # [Actual Question]
        addH = 100
        for question in text:
            largeText = pygame.font.Font('freesansbold.ttf', fontSize)
            textSurf, textRect = self.text_objects(question, largeText)
            textRect.center = ((self.display_width * 2), (self.display_height + 70))
            self.screen.blit(textSurf, textRect)
            for answer in text[question]:
                largeText = pygame.font.Font('freesansbold.ttf', 20)
                textSurf, textRect = self.text_objects(answer, largeText)
                textRect.center = ((self.display_width * 2), (self.display_height + addH))
                self.screen.blit(textSurf, textRect)
                addH += 35
        pygame.display.update()

    def quizBackground(self):
        if (self.quizScreen):
            rect = pygame.Surface((700, 300))  # the size of your rect
            rect.set_alpha(200)  # alpha level
            rect.fill((255, 255, 255))
            self.screen.blit(rect, (375, 275))
            self.message_display(self.test1, 25, self.screen)