import math
import pygame, sys
from pygame.locals import *
from pygame import mixer
import random


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load("Icono.png")
pygame.display.set_icon(icono)
background = pygame.image.load("background.png")
music = pygame.mixer.music.load("music.wav")
mixer.music.play(-1)

playerimg = pygame.image.load("ship2.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

score_value = 0
font = pygame.font.Font("04B_30__.TTF", 24)

textX = 600
textY = 10

over_font = pygame.font.Font("04B_30__.TTF", 64)

alienImg = []
alien1X = []
alien1Y = []
alien1X_change = []
alien1Y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    alienImg.append(pygame.image.load("alien.png"))
    alien1X.append(random.randint(8, 735))
    alien1Y.append(random.randint(50, 150))
    alien1X_change.append(4)
    alien1Y_change.append(40)


bulletImg = pygame.image.load("001-fitness-ball.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


alien2Img = []
alien2X = []
alien2Y = []
alien2X_change = []
alien2Y_change = []
num_of_enemies2 = 4


for r in range(num_of_enemies2):
    alien2Img.append(pygame.image.load("alien2.png"))
    alien2X.append(random.randint(8, 735))
    alien2Y.append(random.randint(50, 150))
    alien2X_change.append(4)
    alien2Y_change.append(40)

alien3Img = []
alien3X = []
alien3Y = []
alien3X_change = []
alien3Y_change = []
num_of_enemies3 = 3


for f in range(num_of_enemies3):
    alien3Img.append(pygame.image.load("alien3.png"))
    alien3X.append(random.randint(8, 735))
    alien3Y.append(random.randint(50, 150))
    alien3X_change.append(4)
    alien3Y_change.append(40)

alien4Img = []
alien4X = []
alien4Y = []
alien4X_change = []
alien4Y_change = []
num_of_enemies4 = 2


for a in range(num_of_enemies4):
    alien4Img.append(pygame.image.load("alien4.png"))
    alien4X.append(random.randint(8, 735))
    alien4Y.append(random.randint(50, 150))
    alien4X_change.append(4)
    alien4Y_change.append(40)

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (0,255,0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (150, 200))

def player(x, y):
    screen.blit(playerimg, (x, y))

def alien1(x, y, i):
    screen.blit(alienImg[i], (x, y))

def alien2(x, y, r):
    screen.blit(alien2Img[r], (x, y))

def alien3(x, y, f):
    screen.blit(alien3Img[f], (x, y))

def alien4(x, y, a):
    screen.blit(alien4Img[a], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(alien1X, alien1Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(alien1X - bulletX, 2) + (math.pow(alien1Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def opCollision(alien2X, alien2Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(alien2X - bulletX, 2) + (math.pow(alien2Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def omCollision(alien3X, alien3Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(alien3X - bulletX, 2) + (math.pow(alien3Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def ogCollision(alien4X, alien4Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(alien4X - bulletX, 2) + (math.pow(alien4Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

while True:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if score_value <= 50:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        elif score_value > 50:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
        elif score_value > 100:
            if event.key == pygame.K_LEFT:
                playerX_change = -9
            if event.key == pygame.K_RIGHT:
                playerX_change = 9
        elif score_value > 200:
            if event.key == pygame.K_LEFT:
                playerX_change = -11
            if event.key == pygame.K_RIGHT:
                playerX_change = 11


        if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):

        if alien1Y[i] > 440:
            for j in range(num_of_enemies):
                alien1Y[j] = 2000
            game_over_text()
            bullet_state = "ready"
            break


        alien1X[i] += alien1X_change[i]
        if alien1X[i] <= 0:
            if score_value < 75:
                alien1X_change[i] = 4
                alien1Y[i] += alien1Y_change[i]
            else:
                alien1X_change[i] = 5
                alien1Y[i] += alien1Y_change[i]
        elif alien1X[i] >= 736:
            if score_value < 2:
                alien1X_change[i] = -4
                alien1Y[i] += alien1Y_change[i]
            else:
                alien1X_change[i] = -5
                alien1Y[i] += alien1Y_change[i]

        collision = isCollision(alien1X[i], alien1Y[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            alien1X[i] = random.randint(8, 735)
            alien1Y[i] = random.randint(50, 150)

        alien1(alien1X[i], alien1Y[i], i)

    if score_value > 10:
       for r in range(num_of_enemies2):

            if alien2Y[r] > 480:
               for h in range(num_of_enemies2):
                    alien2Y[h] = 2000
               game_over_text()
               bullet_state = "ready"
               break

            alien2X[r] += alien2X_change[r]
            if alien2X[r] <= 0:
                if score_value < 100:
                    alien2X_change[r] = 5
                    alien2Y[r] += alien2Y_change[r]
                else:
                    alien2X_change[r] = 6
                    alien2Y[r] += alien2Y_change[r]
            elif alien2X[r] >= 736:
                if score_value > 100:
                    alien2X_change[r] = -5
                    alien2Y[r] += alien2Y_change[r]
                else:
                    alien2X_change[r] = -6
                    alien2Y[r] += alien2Y_change[r]

            collision = opCollision(alien2X[r], alien2Y[r], bulletX, bulletY)
            if collision:
                explosion_sound = mixer.Sound("explosion.wav")
                explosion_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 2
                alien2X[r] = random.randint(8, 735)
                alien2Y[r] = random.randint(100, 250)

            alien2(alien2X[r], alien2Y[r], r)

    if score_value >= 25:
        for f in range(num_of_enemies3):

            if alien3Y[f] > 480:
                for k in range(num_of_enemies3):
                    alien1Y[k] = 2000
                game_over_text()
                bullet_state= "ready"
                break

            alien3X[f] += alien3X_change[f]
            if alien3X[f] <= 0:
                if score_value < 150:
                    alien3X_change[f] = 6
                    alien3Y[f] += alien3Y_change[f]
                else:
                    alien3X_change[f] = 7
                    alien3Y[f] += alien3Y_change[f]
            elif alien3X[f] >= 736:
                if score_value < 150:
                    alien3X_change[f] = -6
                    alien3Y[f] += alien3Y_change[f]
                else:
                    alien3X_change[f] = -7
                    alien3Y[f] += alien3Y_change[f]

            collision = omCollision(alien3X[f], alien3Y[f], bulletX, bulletY)
            if collision:
                explosion_sound = mixer.Sound("explosion.wav")
                explosion_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 3
                alien3X[f] = random.randint(8, 735)
                alien3Y[f] = random.randint(50, 150)

            alien3(alien3X[f], alien3Y[f], f)

    if score_value >= 50:
        for a in range(num_of_enemies4):

            if alien4Y[a] > 480:
                for l in range(num_of_enemies4):
                    alien1Y[l] = 2000
                game_over_text()
                bullet_state = "ready"
                break

            alien4X[a] += alien4X_change[a]
            if alien4X[a] <= 0:
                if score_value < 200:
                    alien4X_change[a] = 7
                    alien4Y[a] += alien4Y_change[a]
                else:
                    alien4X_change[a] = 8
                    alien4Y[a] += alien4Y_change[a]
            elif alien4X[a] >= 736:
                if score_value > 200:
                    alien4X_change[a] = -7
                    alien4Y[a] += alien4Y_change[a]
                else:
                    alien4X_change[a] = -8
                    alien4Y[a] += alien4Y_change[a]


            collision = ogCollision(alien4X[a], alien4Y[a], bulletX, bulletY)
            if collision:
                explosion_sound = mixer.Sound("explosion.wav")
                explosion_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 4
                alien3X[a] = random.randint(8, 735)
                alien4Y[a] = random.randint(100, 250)

            alien4(alien4X[a], alien4Y[a], a)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
