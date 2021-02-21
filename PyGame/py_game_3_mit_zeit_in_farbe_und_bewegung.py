import pygame
import random
import time

print(time.time())
start = time.time()

pygame.init()

#lege anfangswerte fest
a = 0
b = 0
c = 0
x = 0
y = 0


rotanteil = 50
blauanteil = 50

farbe_1 = (rotanteil,255,blauanteil)
farbe_2 = (rotanteil,255,blauanteil)
farbe_3 = (rotanteil,255,blauanteil)

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
        
        pressed = pygame.key.get_pressed()
        
        #wenn tasten gedrückt werden ändere x und y
        if pressed[pygame.K_UP]:
                y = y - 3
        if pressed[pygame.K_DOWN]:
                y = y + 3
                
        if pressed[pygame.K_LEFT]:
                x = x - 3
                
        if pressed[pygame.K_RIGHT]:
                x = x + 3
                
        #ist und y ist jetzt in den farben drin
        farbe_3 = (x,y,255)
        farbe_4 = (x%255,(100+y//5)%255,0)
        farbe_5 = (255,(100+y//5)%255,100)
        
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        end = time.time()
##        print(end)
        print(round(end - start))

##        print(time.time()-1613230994)
        pygame.draw.rect(screen, (round(end - start)*10, round(end - start)*10, 255-round(end - start)*10), pygame.Rect(30+x, 30+y, 20, 20))
        pygame.draw.rect(screen, farbe_5, pygame.Rect(100+round(end - start)*10, 130+round(end - start)*10, 30, 100))
        pygame.draw.rect(screen, farbe_3, pygame.Rect(100, 500, 100, 50))
        pygame.draw.rect(screen, farbe_4, pygame.Rect(600+x, 600+y, 100+round(end - start)*10, 100-round(end - start)*10))
        
        pygame.display.flip()
        
        
        
