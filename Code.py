import random
import pygame
from pygame.locals import *
import math

pygame.init()

width = 800
height = 800

WHITE = [255, 255, 255]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System")

stars = []

angle1 = 0
angle2 = 0
angle3 = 0
angle4 = 0
angle5 = 0
angle6 = 0
angle7 = 0
angle8 = 0

for i in range(60):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    stars.append([x, y])

clock = pygame.time.Clock()
done = False


sun = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\\Planet_Images\\sun.png")
sun = pygame.transform.scale(sun, (100, 100))  # Decreased sun size

mercury = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\P3_Multimedia\\Planet_Images\\mercury.png")
mercury = pygame.transform.scale(mercury, (40, 40))  # Decreased mercury size
mRect = mercury.get_rect()

venus = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\\Planet_Images\\venus.png")
venus = pygame.transform.scale(venus, (20, 20))  # Decreased venus size
vRect = venus.get_rect()

earth = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\\Planet_Images\\earth.png")
earth = pygame.transform.scale(earth, (50, 50))  # Decreased earth size
eRect = earth.get_rect()

mars = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\\Planet_Images\\mars.png")
mars = pygame.transform.scale(mars, (50, 50))  # Decreased earth size
msRect = mars.get_rect()

jupiter = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\\Planet_Images\\jupiter.png")
jupiter = pygame.transform.scale(jupiter, (50, 50))  # Decreased earth size
jRect = jupiter.get_rect()

saturn = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\Planet_Images\\saturn.png")
saturn = pygame.transform.scale(saturn, (50, 50))  # Decreased saturn size
sRect = saturn.get_rect()

uranus= pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\\Planet_Images\\uranus.png")
uranus = pygame.transform.scale(uranus, (50, 50))  # Decreased earth size
uRect = uranus.get_rect()

neptune = pygame.image.load("C:\\Users\\agarw\\OneDrive\\Desktop\\P3_Multimedia\\Planet_Images\\neptune.png")
neptune = pygame.transform.scale(neptune, (50, 50))  # Decreased earth size
nRect = neptune.get_rect()

rect = saturn.get_rect()
earthRect = earth.get_rect()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    for i in range(len(stars)):
        pygame.draw.circle(screen, (255, 255, 255), stars[i], random.randrange(1, 5))

        stars[i][1] += 1
        if stars[i][1] > height:
            y = random.randrange(-50, -10)
            stars[i][1] = y
            x = random.randrange(0, 800)
            stars[i][0] = x

    p1 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 260, 2)
    p2 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 230, 2)
    p3 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 200, 2)
    p4 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 170, 2)
    p5 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 140, 2)
    p6 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 110, 2)
    p7 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 80, 2)
    p8 = pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 50, 2)

    screen.blit(sun, (350, 350))
   
    mRect.center = (50 * math.cos(angle1) + 400, 50 * math.sin(angle1) + 400)
    screen.blit(mercury,mRect)
    vRect.center = (80 * math.cos(angle2) + 400, 80 * math.sin(angle2) + 400)
    screen.blit(venus,vRect)
    eRect.center  = (110 * math.cos(angle3) + 400, 110 * math.sin(angle3) + 400)
    screen.blit(earth,eRect)
    msRect.center  = (140 * math.cos(angle4) + 400, 140 * math.sin(angle4) + 400)
    screen.blit(mars,msRect)
    jRect.center  = (170 * math.cos(angle5) + 400, 170 * math.sin(angle5) + 400)
    screen.blit(jupiter,jRect)
    sRect.center  =  (200 * math.cos(angle6) + 400, 200 * math.sin(angle6) + 400)
    screen.blit(saturn,sRect)
    uRect.center  = (230 * math.cos(angle7) + 400, 230 * math.sin(angle7) + 400)
    screen.blit(uranus,uRect)
    nRect.center  =  (260 * math.cos(angle8) + 400, 260 * math.sin(angle8) + 400)
    screen.blit(neptune,nRect)
   
    angle1 += 0.06
    angle2 += 0.03
    angle3 += 0.01
    angle4 += 0.009
    angle5 += 0.006
    angle6 += 0.004
    angle7 += 0.002
    angle8 += 0.001
   
    clock.tick(60)
    pygame.display.update()

pygame.quit()