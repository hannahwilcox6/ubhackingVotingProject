import pygame
from player import Player
from Quiz import Quiz
import npc
pygame.init()


Prescreen = pygame.display.set_mode((1500,600))
#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
pygame.display.set_caption("UBHacking Voting 2020")
icon = pygame.image.load("vote.png")
pygame.display.set_icon(icon)

preRunning = True
while preRunning:
    bg = pygame.image.load("titlefinal.jpg")
    Prescreen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            preRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                preRunning = False


#  game window, with height and width
screen = pygame.display.set_mode((1500,600))
#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
pygame.display.set_caption("UBHacking Voting 2020")
icon = pygame.image.load("vote.png")
pygame.display.set_icon(icon)

running = True
quiz1 = {"When is the deadline to register to vote?": ["[A] November 3", "[B] October 3", "[C] October 9",
                                                           "[D] December 25"],
             "How old do you need to be to vote?": ["[A] 18", "[B] 21", "[C] 28", "[D] 16"],
             "How can you check your registration status?": ["[A] You can't", "[B] Call the government",
                                                             "[C] Various websites online",
                                                             "[D] Just remember when you did it"]}
ans1 = ["B","A","C"]
ansInd1 = [1,0,2]
quiz2 = {"Who isn't a current official presidential candidate?": ["[A] Joe Biden - Kamala Harris", "[B] Donald Trump - Mike Pence", "[C] Jo Jorgenson - Spike Cohen", "[D] Daniel Rotter - Grace Grenki"],
         "Who can you write in for the presidential candidate?": ["[A] Kanye West", "[B] Your mom", "[C] Your school principal", "[D] All of the above"],
         "How should you research candidates?": ["[A] Don't, just pick randomly.","[B] Only look from one news site", "[C] Check a variety of sources with different views", "[D] Ask your parents"]}
ans2 = ["D","D","C"]
ansInd2 = [3,3,2]
quiz3 = {"When does early voting occur in NYS?": ["[A] It doesn't","[B] October 2 - November 3", "[C] October 24 - November 3","[D] None of the above"],
         "How can you request a mail in ballot?": ["[A] Following the steps in websites like voteearlyny.org","[B] Through your local election office","[C] Going to vote.org and filling out the application online", "[D] All of the above"],
         "When is election day?": ["[A] November 3", "[B] 6AM - 9PM", "[C] During designated early voting periods", "[D] All of the above"]}
ans3 = ["C","D","D"]
ansInd3 = [2,3,3]

q1 = Quiz(screen,quiz1,ans1,ansInd1,0,1)
q2 = Quiz(screen, quiz2, ans2, ansInd2, 0, 1)
q3 = Quiz(screen, quiz3, ans2, ansInd2, 0, 1)

Y = 460
npc1 = npc.NPC("man1.png",355, Y, q1)
npc2 = npc.NPC("man2.png", 690, Y, q2)
npc3 = npc.NPC("person2.png", 1240, Y, q3)
p1 = Player("person1.png", 120, Y)

npcs = [npc1, npc2, npc3]
quizzes = [q1, q2, q3]

currentquiz = q1

def text_objects(text, font):
    black = (0, 0, 0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def voted():
    rect = pygame.Surface((700, 300))  # the size of your rect
    rect.set_alpha(200)  # alpha level
    rect.fill((255, 255, 255))  # Rectangle to appear behind the quiz questions
    screen.blit(rect, (375, 275))  # Call rectangle to be drawn
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    textSurf, textRect = text_objects("Thank you for voting!!", largeText)
    textRect.center = ((375 * 2), (275 + 30))
    screen.blit(textSurf, textRect)
    pygame.display.update()

while running:
    bg = pygame.image.load("finalbgrd.jpg")
    screen.blit(bg,(0,0))

    for i in npcs:
        i.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(p1.quizScreen)

        for i in npcs:
            p1.collision(i)
            if(p1.collidedObject != None and p1.quizScreen == False): #This is so 'e' doesn't break.
                p1.actions(event)
                print("AAAAAAAAAAAAAAA")
                for i in quizzes:
                    if(p1.collidedObject.quiz == i):
                        currentquiz = i
            if (p1.quizScreen == True and currentquiz.finished == False):
                currentquiz.quizActive = True
                if(currentquiz.quizActive == True):
                    currentquiz.draw()
                currentquiz.actions(event)
            else:
                p1.actions(event)

    p1.draw(screen)
    if(currentquiz.quizActive):
        currentquiz.draw()
    else:
        p1.quizScreen = False
        p1.interacting = False

    pygame.display.update()