import pygame
import random
from pygame.constants import BLEND_MULT, GL_RED_SIZE, MOUSEBUTTONDOWN
pygame.init()



# create the screen
screen = pygame.display.set_mode((800, 600))
# Set fps = 60
clock = pygame.time.Clock()
# create the caption
pygame.display.set_caption("My First Game")
# create the icon
icon = pygame.image.load("tile_01.png")
pygame.display.set_icon(icon)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# display the background
background = pygame.image.load("Sample.png")

# display player
playerImg = pygame.image.load("ship (10).png")
playerX = 370
playerY = 480
playerchangeX = 0
playerchangeY = 0
def player(X, Y):
    screen.blit(playerImg, (X, Y))

# create the enemy
enemyImg = pygame.image.load("crew (6).png")
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 536)
enemychangeX = 0.3
enemychangeY = 0.3
# create the enemy
def enemy(X, Y):
    screen.blit(enemyImg, (X, Y))

# create the bullet
# ready - you can't see the bullet on the screen
# fire - the bullet is currently moving
cannonBall = pygame.image.load("cannonBall.png")
cannonBallX = 0
cannonBallY = 0
cannonBallchangeX = 0
cannonBallchangeY = 10
cannoBallSpeed = 10
cannonBallState = "ready"
def fire_cannon(x, y):
    global cannonBallState
    cannonBallState = "fire"
    screen.blit(cannonBall, (x + 30, y ))

    


# display the screen until the user clicks the close button
done = False
while not done:
    
    # change screen color to white
    screen.fill((255, 255, 255))
    # set 60 frames per second
    clock = pygame.time.Clock()
    # display the background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # move the player by 4 arrows
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerchangeX = -3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerchangeX = 3
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerchangeY = -3
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerchangeY = 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                print(mouseX, mouseY)
                if cannonBallState == "ready":
            #         # bulletSound = mixer.Sound("laser.wav")
            #         # bulletSound.play()
            #         # Get the current x cordinate of the spaceship
                    cannonBallX = playerX
                    cannonBallY = playerY
                    fire_cannon(cannonBallX, cannonBallY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT  or event.key == pygame.K_a or event.key == pygame.K_d :
                playerchangeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                playerchangeY = 0
    pygame.display.flip()
    
    # move player
    playerX += playerchangeX
    playerY += playerchangeY
    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736
    if playerY < 0:
        playerY = 0
    if playerY > 536:
        playerY = 536  
    
    # move enemy 
    enemyX += enemychangeX
    enemyY += enemychangeY
    if enemyX < 0:
        enemychangeX = 0.3
    if enemyX > 736:
        enemychangeX = -0.3
    if enemyY < 0:
        enemychangeY = 0.3
    if enemyY > 536:
        enemychangeY = -0.3
    
    # rate of fire is 1 shoot per second

    

    if cannonBallState == "fire":
        fire_cannon(cannonBallX, cannonBallY)
        cannonBallY -= cannonBallchangeY
    if cannonBallY <= 50:
        cannonBallY = playerY
        cannonBallState = "ready"

    
    # check for collision
    if cannonBallX == enemyX and cannonBallY == enemyY:
        cannonBallState = "ready"
        cannonBallY = playerY
        enemyX = random.randint(0, 736)
        enemyY = random.randint(0, 536)
    # display player and enemy
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    
    # update the screen
    pygame.display.update()
    # set the frame rate
    # update the screen
# how to create a class player
# how to create a class enemy
# how to create a class bullet


