import pygame
pygame.init()
import time
import random

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("snake game")

back_ground = pygame.image.load("snake background.jpg")

# snake block
sImg = pygame.image.load("tennis-ball.png")
head_img = pygame.image.load("python (1).png")
sx = []
sy = []
no_block = 1
for i in range(no_block):
    sx.append(48)
    sy.append(48)


def snake(x, y):
    screen.blit(sImg, (x, y))

# food
def food(x, y):
    ll = pygame.image.load("orange-juice.png")
    screen.blit(ll, (x, y))

# random food
def random_food():
    return random.randint(3, 30) * 24, random.randint(3, 20) * 24

# text
font = pygame.font.Font("freesansbold.ttf", 32)
def text(x, y):
    ll = font.render("score :" + str(score), True, (0, 0, 0))
    if x != 0:
        screen.blit(ll, (x, y))
        return
    screen.blit(ll, (0,0))

# snake_collision
def snake_collision():
    for i in range(1, no_block):
         if sx[i] == sx[0] and sy[i] == sy[0]:
            return True
    return False

score, stop = 0, 0
position = "right"
running = True
collision = 0
fx, fy = random.randint(3, 30)*24, random.randint(3, 20)*24
while running:
    screen.fill((255, 255, 255))

    # back ground
    screen.blit(back_ground, (-1000, -1000))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if position == "right":
                    continue
                position = "left"
            if event.key == pygame.K_RIGHT:
                if position == "left":
                    continue
                position = "right"
            if event.key == pygame.K_UP:
                if position == "down":
                    continue
                position = "up"
            if event.key == pygame.K_DOWN:
                if position == "up":
                    continue
                position = "down"

    # snake display

    if position == "left":
        sx[0] -= 24
        if snake_collision():
            stop = 1
    if position == "right":
        sx[0] += 24
        if snake_collision():
            stop = 1
    if position == "up":
        sy[0] -= 24
        if snake_collision():
            stop = 1
    if position == "down":
        sy[0] += 24
        if snake_collision():
            stop = 1
    # fawarding the sanake body

    for i in range(no_block-1, 0, -1):
        sx[i] = sx[i-1]
        sy[i] = sy[i-1]

    for i in range(1, no_block):
        if stop == 1:
            text(350, 250)
            continue
        snake(sx[i], sy[i])

    # collision
    if fx <= sx[0]+15 <= fx+24 and fy <= sy[0]+15 <= fy+24:
        collision = 1
        score+=1
        no_block += 1
        sx.append(sx[no_block-2])
        sy.append([sy[no_block-2]])

        # food display and checking

        fx, fy = random_food()
        for i in range(1, no_block):
            if fx == sx[i] and fy == sy[i]:
                fx, fy = random_food()

    # boundries
    if sx[0]+24 >= 800 or sy[0]+24 >= 600:
        stop = 1
    if sx[0] <= 0 or sy[0] <= 0:
        stop = 1
    if stop == 0:
        text(0, 0)
        # food
        food(fx, fy)

    # snake head
    screen.blit(head_img, (sx[0] - 5, sy[0] + 2))
    time.sleep(0.13)
    pygame.display.update()














