import pygame
from player import Player
from Quiz import Quiz
import npc
pygame.init()

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
quiz2 = {"Who isn't a current official presidential candidate?": ["[A] Joe Biden - Kamala Harris", "[B] Donald Trump - Mike Pence", "[C] Jo Jorgenson - Spike Cohen", "[D] Daniel Rotter - Grace Grenki"],
         "Who can you write in for the presidential candidate?": ["[A] Kanye West", "[B] Your mom", "[C] Your school principal", "[D] All of the above"],
         "How should you research candidates?": ["[A] Don't, just pick randomly.","[B] Only look from one news site", "[C] Check a variety of sources with different views", "[D] Ask your parents"]}
ans2 = ["D","D","C"]
quiz3 = {"When does early voting occur in NYS?": ["[A] It doesn't","[B] October 2 - November 3", "[C] October 24 - November 3","[D] None of the above"],
         "How can you request a mail in ballot?": ["[A] Following the steps in websites like voteearlyny.org","[B] Through your local election office","[C] Going to vote.org and filling out the application online", "[D] All of the above"],
         "When is election day?": ["[A] November 3", "[B] 6AM - 9PM", "[C] During designated early voting periods", "[D] All of the above"]}
ans3 = ["C","D","D"]

Y = 460
npc1 = npc.NPC("man1.png",690, Y)
npc2 = npc.NPC("man2.png", 1240, Y)
p1 = Player("person1.png", 370, Y)

q1 = Quiz(screen,quiz1,ans1,0,1)
npcs = [npc1,npc2]
while running:
    bg = pygame.image.load("finalbgrd.jpg")
    screen.blit(bg,(0,0))
    npc1.draw(screen)
    npc2.draw(screen)
    # Window is closed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (p1.quizScreen == True):
            q1.quizActive = True
            if(q1.quizActive == True):
                q1.draw()
            q1.actions(event)
        else:
            p1.actions(event)
    #Checks if player is hitting buttons
    for i in npcs:
        i.draw(screen)
    p1.collision(npc1)
    p1.collision(npc2)
    p1.draw(screen)
    if(q1.quizActive):
        q1.draw()
    else:
        p1.quizScreen = False
        p1.interacting = False


    pygame.display.update()