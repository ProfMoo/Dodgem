import random, sys, time, math, pygame
from pygame.locals import *

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
    moveUp    = False
    moveDown  = False

    playerObj = {'surface': pygame.transform.scale(USER_IMG, (USERSIZE, USERSIZE)),
             'x': HALF_WINWIDTH,
             'y': (WINHEIGHT-FLOORHEIGHT) - USERSIZE,
             'inAir': False,
             'inDubAir': False}

    while True: # main game loop
        # draw the green background
        DISPLAYSURF.fill(BACKGROUNDCOLOR)
        pygame.draw.rect(DISPLAYSURF, OBSTACLECOLOR, FLOORRECT)

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    moveRight = False
                    moveLeft = True
                elif event.key in (K_RIGHT, K_d):
                    moveLeft = False
                    moveRight = True
                elif event.key is K_SPACE:
                    if playerObj['inAir'] is False:
                        playerObj['inAir'] = True
                        verticalMovement = -40
                    if playerObj['inAir'] is True:
                        if playerObj['inDubAir'] is False and verticalMovement > -15:
                            playerObj['inDubAir'] = True
                            verticalMovement = -40

            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a):
                    moveLeft = False
                elif event.key in (K_RIGHT, K_d):
                    moveRight = False

                elif event.key == K_ESCAPE:
                    terminate()

        if not gameOverMode:
            # actually move the player
            if moveLeft:
                playerObj['x'] -= MOVERATE
            if moveRight:
                playerObj['x'] += MOVERATE

            if playerObj['inAir'] is True:
                print("inAir: ", playerObj['inAir'])
                print("inDubAir: ", playerObj['inDubAir'])
                playerObj['y'] += verticalMovement
                verticalMovement += 5
                if playerObj['y'] >= ((WINHEIGHT-FLOORHEIGHT) - USERSIZE):
                    playerObj['inAir'] = False
                    playerObj['inDubAir'] = False
                    playerObj['y'] = ((WINHEIGHT-FLOORHEIGHT) - USERSIZE)
            elif playerObj['inDubAir'] is True:
                playerObj['y'] += verticalMovement
                verticalMovement += 5
                if playerObj['y'] >= ((WINHEIGHT-FLOORHEIGHT) - USERSIZE):
                    playerObj['inAir'] = False
                    playerObj['inDubAir'] = False
                    playerObj['y'] = ((WINHEIGHT-FLOORHEIGHT) - USERSIZE)

            playerObj['rect'] = pygame.Rect( playerObj['x'], playerObj['y'], USERSIZE, USERSIZE)
            DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()