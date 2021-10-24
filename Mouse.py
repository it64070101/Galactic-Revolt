"""Mouse"""
# import
import pygame , sys
from pygame import display

# หน้าต่าง
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Mouse")
screen = pygame.display.set_mode((728,410), 0, 40)
bg = pygame.image.load('Testbg.png')
img = pygame.image.load('Test2.png').convert()
offset = [0, 0]
font = pygame.font.SysFont(None, 20)
clicking = False
right_click = False
middle_click = False

# เชคว่ากดป่าว

def text(text, font, color , surface, x, y):
        """Textsurface"""
        textobj = font.render(text, 1, color)
        textreat = textobj.get_rect()
        textreat.topleft = (x, y)
        surface.blit(textobj, textreat)

def cardselect():
        """Selectcard"""
        while True:
            screen.fill((0, 0, 0))
            text("Card", font, (255, 255, 255), screen, 20, 20)

            mx, my = pygame.mouse.get_pos()
            card1 = pygame.Rect(50, 100, 200, 50)
            card2 = pygame.Rect(50, 200, 200, 50)
            card3 = pygame.Rect(50, 300, 200, 50)
            if card1.collidepoint((mx, my)):
                if clicking:
                    card_1()
            if card2.collidepoint((mx, my)):
                if clicking:
                    card_2()
            if card3.collidepoint((mx, my)):
                if clicking:
                    card_3()
            
            pygame.draw.rect(screen, (255, 0, 0), card_1)
            pygame.draw.rect(screen, (255, 0, 0), card_2)
            pygame.draw.rect(screen, (255, 0, 0), card_3)

            clicking = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
 
            pygame.display.update()
            mainClock.tick(60)
def card_1():
        """c1"""
        running = True
        while running:
            screen.fill((0, 0, 0))

            text('Card_1', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()
            mainClock.tick(60)

def card_2():
        """c2"""
        running = True
        while running:
            screen.fill((0, 0, 0))

            text('Card_1', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()
            mainClock.tick(60)

def card_3():
        """c3"""
        running = True
        while running:
            screen.fill((0, 0, 0))

            text('Card_1', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()
            mainClock.tick(60)

pygame.display.update()
mainClock.tick(60)
cardselect()
