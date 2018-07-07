import random, sys, time, math, pygame
from pygame.locals import *
from User import *
from Power import *
import settings

def main():
    global FPSCLOCK, BASICFONT, USER_IMG, POWER_IMG

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    settings.DISPLAYSURF = pygame.display.set_mode((settings.WINWIDTH, settings.WINHEIGHT))
    pygame.display.set_caption('Dodgem')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    # load the image files
    USER_IMG = pygame.image.load('user.png').convert_alpha()
    POWER_IMG = pygame.image.load('power.png').convert_alpha()

    while True:
        runGame()

def runGame():
    moveLeft  = False
    moveRight = False
    moveVert = False
    
    vertMovement = 0

    leftDown = False
    rightDown = False

    playerObj = userFactory(settings.USERTYPE)
    size = 32
    kind = settings.EXTRA_JUMP
    POWERLOCATION = (580, 110)
    global powerObj
    powerObj = Power(pygame.transform.scale(POWER_IMG, (size, size)), POWERLOCATION[0], POWERLOCATION[1], size, kind)
    settings.POWER_OBJ_LIST.append(powerObj)
    settings.POWER_LIST.append(powerObj.rect)

    settings.DISPLAYSURF.fill(settings.BACKGROUNDCOLOR)
    pickLevel(settings.LEVEL)
    pygame.display.update()

    while True: # main game loop
        settings.RECTS_TO_UPDATE = []
        oldX = playerObj.x
        oldY = playerObj.y
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
                        playerObj.vertSpeed = playerObj.jumpAcceleration
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

            elif event.type == settings.POWERBACKEVENT:
                pygame.time.set_timer(settings.POWERBACKEVENT, 0)
                powerObj.makeActive()
                print("power_list: ", settings.POWER_LIST)

        if moveLeft:
            playerObj.leftMovement(settings.OBSTACLELIST)
        if moveRight:
            playerObj.rightMovement(settings.OBSTACLELIST)
        playerObj.vertMovement(settings.OBSTACLELIST)

        #checking if the user hit a powerup/down
        powerCollected = playerObj.checkIfCaptured(settings.POWER_LIST)
        if (powerCollected != -1): #we have collided with a powerup
            (settings.POWER_OBJ_LIST)[powerCollected].hit(playerObj, settings.POWERBACKEVENT)

        powerObj.draw()

        updatePlayerImages(oldX, oldY, playerObj)

        pygame.display.update(settings.RECTS_TO_UPDATE)
        FPSCLOCK.tick(settings.FPS)

def terminate():
    pygame.quit()
    sys.exit()

def updatePlayerImages(oldX, oldY, playerObj):
    movePlayerRect = pygame.Rect(oldX, oldY, playerObj.size, playerObj.size)
    pygame.draw.rect(settings.DISPLAYSURF, settings.BACKGROUNDCOLOR, movePlayerRect)
    settings.RECTS_TO_UPDATE.append(movePlayerRect)
    playerObj.rect = pygame.Rect(playerObj.x, playerObj.y, playerObj.size, playerObj.size)
    settings.RECTS_TO_UPDATE.append(playerObj.rect)
    settings.DISPLAYSURF.blit(playerObj.surface, playerObj.rect)

def userFactory(userType):
    USER_MOVERATE = 20
    USER_SIZE = 40
    USER_JUMPACCELERATION = -35
    USER_GRAVITY = 5
    STARTLOCATION = (settings.HALF_WINWIDTH, settings.HALF_WINHEIGHT - 100)
    NUM_JUMPS = 2
    if (userType == 1):
        playerObj = User(pygame.transform.scale(USER_IMG, (USER_SIZE, USER_SIZE)), STARTLOCATION[0], STARTLOCATION[1], USER_MOVERATE, USER_SIZE, USER_JUMPACCELERATION, USER_GRAVITY, NUM_JUMPS)
    elif (userType == 2):
        playerObj = User(pygame.transform.scale(USER_IMG, (USER_SIZE, USER_SIZE)), STARTLOCATION[0], STARTLOCATION[1], USER_MOVERATE, USER_SIZE, USER_JUMPACCELERATION, USER_GRAVITY, 3)

    return playerObj

def pickLevel(level):
    if level == 1:
        drawLevelOne()
    if level == 2:
        drawLevelTwo()
    if level == 3:
        drawLevelThree()

def drawRectangle(x, y, width, height, color):
    OBSTACLE = pygame.Rect(x, y, width, height)
    settings.OBSTACLELIST.append(OBSTACLE)
    pygame.draw.rect(settings.DISPLAYSURF, color, OBSTACLE)

def drawLevelOne():
    FLOORHEIGHT = 100
    drawRectangle(0, settings.WINHEIGHT - FLOORHEIGHT, settings.WINWIDTH, FLOORHEIGHT, settings.BLACK)
    drawRectangle(200, settings.WINHEIGHT-FLOORHEIGHT-250, 100, 250, settings.OBSTACLECOLOR)

def drawLevelTwo():
    FLOORHEIGHT = 40
    drawRectangle(0, settings.WINHEIGHT - FLOORHEIGHT, settings.WINWIDTH, FLOORHEIGHT + 40, settings.BLACK)
    drawRectangle(100, settings.WINHEIGHT-FLOORHEIGHT-100, 100, 100, settings.OBSTACLECOLOR)
    drawRectangle(250, settings.WINHEIGHT-FLOORHEIGHT-200, 100, 200, settings.OBSTACLECOLOR)
    drawRectangle(400, settings.WINHEIGHT-FLOORHEIGHT-200, 100, 100, settings.OBSTACLECOLOR)

def drawLevelThree():
    FLOORHEIGHT = 40
    drawRectangle(0, settings.WINHEIGHT - FLOORHEIGHT, settings.WINWIDTH, FLOORHEIGHT + 40, settings.BLACK)
    drawRectangle(100, settings.WINHEIGHT-FLOORHEIGHT-100, 100, 100, settings.OBSTACLECOLOR)
    drawRectangle(250, settings.WINHEIGHT-FLOORHEIGHT-200, 100, 200, settings.OBSTACLECOLOR)
    drawRectangle(400, settings.WINHEIGHT-FLOORHEIGHT-200, 100, 100, settings.OBSTACLECOLOR)

if __name__ == '__main__':
    main()

#check the rect and surf
#only make them GLOBALLY.
#dont make them every FRAME