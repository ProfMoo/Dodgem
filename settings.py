import pygame

global DISPLAYSURF

FPS = 30 # frames per second to update the screen
WINWIDTH = 640 # width of the program's window, in pixels
WINHEIGHT = 480 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
LEVEL = 4

USERTYPE = 1

OBSTACLECOLOR = (110, 110, 110)
USERCOLOR = (200, 210, 45)
BACKGROUNDCOLOR = (210, 210, 210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RECTS_TO_UPDATE = []
OBSTACLELIST = []
POWER_LIST = []
POWER_OBJ_LIST = []

POWERBACKEVENT = pygame.USEREVENT + 1
POWERBACKEVENT2 = pygame.USEREVENT + 2

EXTRA_JUMP = "extrajump"
TWO_JUMPS = "twojumps"