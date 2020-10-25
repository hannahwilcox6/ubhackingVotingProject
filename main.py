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
test1 = {"How old do you need to be to vote?": ["[A] 18", "[B] 21", "[C] 28", "[D] 16"]}



Y = 480
npc1 = npc.NPC("npc-man1.png",690, Y)
npc2 = npc.NPC("npc-man2.png", 1240, Y)
p1 = Player("standing-up-man-.png", 370, Y)
q1 = Quiz(test1,screen)
npcs = [npc1,npc2]

while running:
    bg = pygame.image.load("placement.png")
    screen.blit(bg,(0,0))
    npc1.draw(screen)
    npc2.draw(screen)
    # Window is closed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        p1.actions(event)
    #Checks if player is hitting buttons
    for i in npcs:
        i.draw(screen)

    p1.collision(npc1)
    p1.collision(npc2)
    p1.draw(screen)
    p1.quizBackground(screen)
    pygame.display.update()