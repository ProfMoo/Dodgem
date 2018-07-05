import random, sys, time, math, pygame
from pygame.locals import *
from User import *
import settings

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, USER_IMG

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    DISPLAYSURF = pygame.display.set_mode((settings.WINWIDTH, settings.WINHEIGHT))
    pygame.display.set_caption('Dodgem')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    # load the image files
    USER_IMG = pygame.image.load('user.png')

    while True:
        runGame()

def runGame():
    moveLeft  = False
    moveRight = False
    moveVert = False
    
    vertMovement = 0

    leftDown = False
    rightDown = False

    USER_MOVERATE = 30
    USER_SIZE = 70
    STARTLOCATION = (settings.HALF_WINWIDTH, settings.HALF_WINHEIGHT)
    playerObj = User(pygame.transform.scale(USER_IMG, (USER_SIZE, USER_SIZE)), STARTLOCATION[0], STARTLOCATION[1], USER_MOVERATE, USER_SIZE)

    while True: # main game loop
        DISPLAYSURF.fill(settings.BACKGROUNDCOLOR)
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
                    if playerObj.jumps != 0:
                        playerObj.jumps -= 1
                        playerObj.vertSpeed = settings.JUMPACCELERATION
                        playerObj.sitting = False
                        moveVert = True

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

        if moveLeft:
            playerObj.leftMovement(settings.OBSTACLELIST)
        if moveRight:
            playerObj.rightMovement(settings.OBSTACLELIST)
        playerObj.vertMovement(settings.OBSTACLELIST)

        playerObj.rect = pygame.Rect( playerObj.x, playerObj.y, playerObj.size, playerObj.size)
        DISPLAYSURF.blit(playerObj.surface, playerObj.rect)

        pygame.display.update()
        FPSCLOCK.tick(settings.FPS)

def terminate():
    pygame.quit()
    sys.exit()

def drawRectangle(x, y, width, height, color):
    OBSTACLE = pygame.Rect(x, y, width, height)
    settings.OBSTACLELIST.append(OBSTACLE)
    pygame.draw.rect(DISPLAYSURF, color, OBSTACLE)

def drawLevelOne():

    FLOORHEIGHT = 100
    # FLOORRECT = pygame.Rect(0, settings.WINHEIGHT-FLOORHEIGHT, settings.WINWIDTH, FLOORHEIGHT)
    # settings.OBSTACLELIST.append(FLOORRECT)
    drawRectangle(0, settings.WINHEIGHT - FLOORHEIGHT, settings.WINWIDTH, FLOORHEIGHT, settings.BLACK)
    drawRectangle(800, settings.WINHEIGHT-FLOORHEIGHT-250, 100, 250, settings.OBSTACLECOLOR)
            # pygame.draw.rect(DISPLAYSURF, settings.BLACK, FLOORRECT)

if __name__ == '__main__':
    main()