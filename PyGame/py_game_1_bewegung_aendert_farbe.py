import pygame
import random

pygame.init()

x = 0
y = 0
rotanteil = 50
blauanteil = 50

farbe_1 = (rotanteil,255,blauanteil)
farbe_2 = (rotanteil,255,blauanteil)


farbe_4 = (255,66,64)
farbe_5 = (255,66,64)

screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))

done = False
is_blue = True

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()

        #wenn pfeiltasten gedrückt, ändert sich x oder x
        #die x bzw y werte werden dann in die (r,g,b) werte
        #von farbe_1 und farbe_2 unten eingesetzt
        if pressed[pygame.K_UP]:
                y = y - 3
                
        if pressed[pygame.K_DOWN]:
                y = y + 3
                
        if pressed[pygame.K_LEFT]:
                x = x - 3
                
        if pressed[pygame.K_RIGHT]:
                x = x + 3

        #die r,g,b werte dürfen nur 0-255 sein sonst gbt es einen ValueError: invalid color argument
        farbe_1 = (x,y,64)
        farbe_2 = (x+x,y,x)
        print("x:",x,"x+x->",x+x,"y",y)
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)

        pygame.draw.rect(screen, farbe_1, pygame.Rect(30+x, 30+y, 20, 20))
        pygame.draw.rect(screen, farbe_1, pygame.Rect(100+x, 130+y, 30, 100))
        pygame.draw.rect(screen, farbe_2, pygame.Rect(300+x, 130+y, 100, 50))
        pygame.draw.rect(screen, farbe_2, pygame.Rect(600+x, 600+y, 100, 100))
        
        pygame.display.flip()
        
        
        
