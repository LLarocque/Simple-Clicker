import pygame
import random

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Simple Clicker')

font = pygame.font.SysFont(None, 32)
bigfont = pygame.font.SysFont(None, 128)

clicks=0
masternum=0
clickchance=1

running = True
while (running):
    window.fill((0,0,0))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            roll = random.randint(1,clickchance)
            clicks+=1
            if roll == 1:
                masternum +=1
                clickchance *= 10
            
                

    text = font.render(f'You have clicked {clicks} times. Chance to increment is 1/{clickchance}',True,(0,255,0))
    text_rect = text.get_rect(center = (400,200))
    window.blit(text,text_rect)

    bignum = bigfont.render(f'{masternum}',True,(0,255,0))
    bignum_rect = bignum.get_rect(center = (400,350))
    window.blit(bignum,bignum_rect)

    pygame.display.update()


clock.tick(120)
pygame.quit()
