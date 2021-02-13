import pygame
import random

pygame.init()

a = 0
b = 0
c = 0

rotanteil = 50
blauanteil = 50
farbe_1 = (rotanteil,255,blauanteil)
farbe_2 = (rotanteil,255,blauanteil)
farbe_3 = (rotanteil,255,blauanteil)

screen = pygame.display.set_mode((500, 300))

done = False
is_blue = True

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                #leertaste ändert farbe
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    a = a + 15
                    if a > 240:
                      a = 255
                      b = b + 15
                      farbe_2 = (rotanteil,255-b,blauanteil)
                      if b > 240:
                        b = 255
                        c = c + 15
                        farbe_2 = (rotanteil,0,blauanteil)
                        farbe_3 = (rotanteil,255-c,blauanteil)
                        if c > 240:
                          c= 255
                          farbe_3 = (rotanteil,0,blauanteil)
                    farbe_1 = (rotanteil, 255-a, blauanteil)

                    print("a=", a,"b=",b, "c=",c)
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, farbe_1, pygame.Rect(30, 30, 60, 60))
        pygame.draw.rect(screen, farbe_2, pygame.Rect(100, 130, 30, 100))
        pygame.draw.rect(screen, farbe_3, pygame.Rect(300, 130, 100, 50))
        pygame.display.flip()
        
        
        
