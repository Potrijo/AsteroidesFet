from turtle import circle
import pygame,sys
from threading import Thread
import threading
# Inicial pygame
pygame.init()
# Finestra de 800x600
eX = 150
eY = 0
e2X = 300
e2Y = 400
e3X = 100
e3Y = 260
e4X = 180
e4Y = 300
size = 800, 600
screen = pygame.display.set_mode(size)
# Títol
pygame.display.set_caption('ASTEROIDES')
# Vars
width, height = 800, 600
width2, height2 = 800, 600
speed = [1, 1]
speed2 = [1, 1]
white = 255, 255, 255
black = 0,0,0
# asteroide + rectangle
ball = pygame.image.load('asteroide.png')
ballrect = ball.get_rect()
ball2 = pygame.image.load('asteroide.png')
ballrect2 = ball.get_rect()
# nau + rectangle
nave = pygame.image.load('halcon.png')
naverect = nave.get_rect()
#posso la nau al centre de la pantalla abaix
ballrect2.move_ip(200, 0)
naverect.move_ip(400, 500)
# iniciem el joc
run=True

def mouEstrella():
    global eY
    global e2Y
    global e3Y
    global e4Y

    eY = eY + 1
    e2Y = e2Y + 1
    e3Y = e3Y + 1
    e4Y = e4Y + 1

    if(eY > height):
        eY = 0
    if(e2Y > height):
        e2Y = 0
    if(e3Y > height):
        e3Y = 0
    if(e4Y > height):
        e4Y = 0
    estrellaHilo = threading.Timer(0.1, mouEstrella)
    estrellaHilo.start()
    
def asterMoving1():
    global ballrect
    global run
    global speed
    global height
    global naverect
    while True:
        pygame.time.delay(1)
        ballrect = ballrect.move(speed)

        if ballrect.left < 0 or ballrect.right>width:
            speed[0] = - speed[0]
            speed[1] = - speed[1]

        if ballrect.top <0:
            speed[1] = 1
        
        if (naverect.colliderect(ballrect)):
            speed[1]=-1

        if ballrect.bottom >height:
            #final programa
            #aqui s'ha de posar una explosio o algo
            run=False

def asterMoving2():
    global ballrect2
    global run
    global speed2
    global height2
    global naverect

    while True:
        pygame.time.delay(1)
        ballrect2 = ballrect2.move(speed2)

        if ballrect2.left < 0 or ballrect2.right>width2:
            speed2[0] = - speed2[0]
            speed2[1] = - speed2[1]

        if ballrect2.top <0:
            speed2[1] = 1
        if (naverect.colliderect(ballrect2)):
            speed2[1]=-1

        if ballrect2.bottom >height:
            #final programa
            #aqui s'ha de posar una explosio o algo
            run=False

filAstre1 = Thread(target=asterMoving1)
filAstre2 = Thread(target=asterMoving2)
estrellaHilo = threading.Timer(0.1, mouEstrella)

filAstre1.start()
filAstre2.start()
estrellaHilo.start()

print(run)
while run:
    # Delay en milisecons
    pygame.time.delay(1)
    # Events
    for event in pygame.event.get():
        #Sortir?
        if event.type == pygame.QUIT: run = False
    # S'ha pulsat una tecla?
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        naverect=naverect.move(-10, 0)
    if keys[pygame.K_RIGHT]:
        naverect=naverect.move(10, 0)
    # Hi ha colisio?


    # Bellugo el asteroide
    
    #Pinto el fons de negre, dibuixo l’ asteroide i la nau
    screen.fill(black)
    pygame.draw.circle(screen, (255,255,255), (eX, eY), 3)
    pygame.draw.circle(screen, (255,255,255), (e2X, e2Y), 3)
    pygame.draw.circle(screen, (255,255,255), (e3X, e3Y), 3)
    pygame.draw.circle(screen, (255,255,255), (e4X, e4Y), 3)

    screen.blit(ball, ballrect)
    screen.blit(ball2, ballrect2)
    screen.blit(nave,naverect)
    pygame.display.flip()
# Surto de pygame
pygame.quit()