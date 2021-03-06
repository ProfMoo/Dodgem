import random, sys, time, math, pygame
from User import *
from Power import *
from TripleJumpPower import *
from DoubleJumpPower import *
from UserFactory import *
import settings

def main():
    global FPSCLOCK, BASICFONT, POWER_IMG

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    settings.DISPLAYSURF = pygame.display.set_mode((settings.WINWIDTH, settings.WINHEIGHT))
    settings.USER_IMG = pygame.image.load('user.png').convert_alpha()
    pygame.display.set_caption('Dodgem')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    settings.TRIPLE_JUMP_POWER_IMG = pygame.image.load('power.png').convert_alpha()
    settings.DOUBLE_JUMP_POWER_IMG = pygame.image.load('pikachu.png').convert_alpha()

    while True:
        runGame()

def runGame():
    leftDown = False
    rightDown = False

    userFactoryObject = UserFactory()
    playerObj = userFactoryObject.createUser(settings.USERTYPE)

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
                    playerObj.moveRight = False
                    if rightDown is not True:
                        playerObj.moveLeft = True
                    leftDown = True
                elif event.key in (K_RIGHT, K_d):
                    playerObj.moveLeft = False
                    if leftDown is not True:
                        playerObj.moveRight = True
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
                        playerObj.moveRight = True
                    playerObj.moveLeft = False
                    leftDown = False
                elif event.key in (K_RIGHT, K_d):
                    if leftDown is True:
                        playerObj.moveLeft = True
                    playerObj.moveRight = False
                    rightDown = False

                elif event.key == K_ESCAPE:
                    terminate()

        #print("user.vertSpeed: ", playerObj.vertSpeed)

        #moving the user
        playerObj.move()

        #checking if the user hit a powerup/down
        powerCollected = playerObj.checkIfCaptured(settings.POWER_LIST)
        if (powerCollected != -1): #we have collided with a powerup
            playerObj = (settings.POWER_OBJ_LIST)[powerCollected].hit(playerObj)

        #checking if any powerups need to come back
        currentTime = time.time()
        for power in settings.POWER_OBJ_LIST:
            power.makeActive(currentTime)

        #drawing the powers
        for power in settings.POWER_OBJ_LIST:
            power.draw()

        #updating the user
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

def pickLevel(level):
    if level == 1:
        drawLevelOne()
    if level == 2:
        drawLevelTwo()
    if level == 3:
        drawLevelThree()
    if level == 4:
        drawLevelFour()

def drawPower(x, y, size, kind):
    POWERLOCATION = (x, y)
    if (kind == settings.EXTRA_JUMP):
        powerObj = TripleJumpPower(POWERLOCATION[0], POWERLOCATION[1], size, kind)
    if (kind == settings.TWO_JUMPS):
        powerObj = DoubleJumpPower(POWERLOCATION[0], POWERLOCATION[1], size, kind)
    settings.POWER_OBJ_LIST.append(powerObj)
    settings.POWER_LIST.append(powerObj.rect)


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
    drawPower(580, 110, 32, settings.EXTRA_JUMP)

def drawLevelFour():
    FLOORHEIGHT = 40
    drawRectangle(0, settings.WINHEIGHT - FLOORHEIGHT, settings.WINWIDTH, FLOORHEIGHT + 40, settings.BLACK)
    drawRectangle(100, settings.WINHEIGHT-FLOORHEIGHT-100, 100, 100, settings.OBSTACLECOLOR)
    drawPower(580, 120, 32, settings.EXTRA_JUMP)
    drawPower(180, 140, 32, settings.TWO_JUMPS)

if __name__ == '__main__':
    main()

#check the rect and surf
#only make them GLOBALLY.
#dont make them every FRAME