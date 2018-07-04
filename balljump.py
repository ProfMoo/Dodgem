import random, sys, time, math, pygame
from pygame.locals import *
from User import *


FPS = 30 # frames per second to update the screen
WINWIDTH = 1280 # width of the program's window, in pixels
WINHEIGHT = 720 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

OBSTACLECOLOR = (110, 110, 110)
USERCOLOR = (200, 210, 45)
BACKGROUNDCOLOR = (210, 210, 210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#CAMERASLACK = 90     # how far from the center the squirrel moves before moving the camera
MOVERATE = 30        # how fast the player moves
BOUNCERATE = 6       # how fast the player bounces (large is slower)
BOUNCEHEIGHT = 30    # how high the player bounces
USERSIZE = 70
FLOORHEIGHT = 100
JUMPACCELERATION = -50
GRAVITY = 6

OBSTACLELIST = []

LEFT = 'left'
RIGHT = 'right'

FLOORRECT = pygame.Rect(0, WINHEIGHT-FLOORHEIGHT, WINWIDTH, FLOORHEIGHT)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, USER_IMG

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Dodgem')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    # load the image files
    USER_IMG = pygame.image.load('user.png')

    while True:
        runGame()


def runGame():
    gameOverMode = False

    moveLeft  = False
    moveRight = False
    
    vertMovement = 0

    leftDown = False
    rightDown = False

    playerObj = User(pygame.transform.scale(USER_IMG, (USERSIZE, USERSIZE)), HALF_WINWIDTH, (WINHEIGHT-FLOORHEIGHT) - USERSIZE)

    while True: # main game loop
        DISPLAYSURF.fill(BACKGROUNDCOLOR)
        pygame.draw.rect(DISPLAYSURF, BLACK, FLOORRECT)
        drawLevelOne()

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    moveRight = False
                    if rightDown is not True:
                        moveLeft = True
                    leftDown = True
                elif event.key in (K_RIGHT, K_d):
                    moveLeft = False
                    if leftDown is not True:
                        moveRight = True
                    rightDown = True
                elif event.key is K_SPACE:
                    print("space pressed: ")
                    if playerObj.jumps != 0:
                        playerObj.jumps -= 1
                        vertMovement = JUMPACCELERATION

            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a):
                    if rightDown is True:
                        moveRight = True
                    moveLeft = False
                    leftDown = False
                elif event.key in (K_RIGHT, K_d):
                    if leftDown is True:
                        moveLeft = True
                    moveRight = False
                    rightDown = False

                elif event.key == K_ESCAPE:
                    terminate()

        # actually move the player
        if playerObj.y + vertMovement < (WINHEIGHT-FLOORHEIGHT) - USERSIZE:
            playerObj.y += vertMovement
            vertMovement += GRAVITY
        else:
            playerObj.jumps = 2
            playerObj.y = (WINHEIGHT-FLOORHEIGHT) - USERSIZE            

        #check if it can move normally
        #if it can, do it
        #if not, give restricted x or y
        if moveLeft:
            playerObj.leftMovement(MOVERATE, USERSIZE, OBSTACLELIST)
        if moveRight:
            playerObj.rightMovement(MOVERATE, USERSIZE, OBSTACLELIST)

        playerObj.rect = pygame.Rect( playerObj.x, playerObj.y, USERSIZE, USERSIZE)
        DISPLAYSURF.blit(playerObj.surface, playerObj.rect)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def drawRectangle(x, y, width, height):
    OBSTACLE1_1 = pygame.Rect(x, y, width, height)
    OBSTACLELIST.append(OBSTACLE1_1)
    pygame.draw.rect(DISPLAYSURF, OBSTACLECOLOR, OBSTACLE1_1)

def drawLevelOne():
    drawRectangle(800, WINHEIGHT-FLOORHEIGHT-250, 100, 250)

if __name__ == '__main__':
    main()