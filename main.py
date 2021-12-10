import pygame
from pygame import Surface, surface
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# create the caption
pygame.display.set_caption("My First Game")
# create the icon
icon = pygame.image.load("tile_01.png")
pygame.display.set_icon(icon)

# display player
playerImg = pygame.image.load("ship (10).png")
playerX = 30
playerY = 40
playerchangeX = 0
playerchangeY = 0
# creat the player
def player(X, Y):
    Surface.blit(screen, playerImg, (X, Y))

# display the screen until the user clicks the close button
done = False
while not done:
    
    pygame.display.flip()
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # move the player by 4 arrows
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerchangeX = -0.2
            if event.key == pygame.K_RIGHT:
                playerchangeX = 0.2
            if event.key == pygame.K_UP:
                playerchangeY = -0.2
            if event.key == pygame.K_DOWN:
                playerchangeY = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerchangeX = 0
                playerchangeY = 0
    pygame.display.flip()
    # change screen color to white
    screen.fill((255, 255, 255))
    # display player
    
    # move player
    playerX += playerchangeX
    playerY += playerchangeY
    player(playerX, playerY)
    # update the screen

    pygame.display.update()

