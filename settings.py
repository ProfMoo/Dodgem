import pygame

global DISPLAYSURF, USER_IMG, DOUBLE_JUMP_POWER_IMG, TRIPLE_JUMP_POWER_IMG

#BIG GAME SETTINGS
FPS = 30 # frames per second to update the screen
WINWIDTH = 640 # width of the program's window, in pixels
WINHEIGHT = 480 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
LEVEL = 4



#user settings
USER_SIZE = 40
USERTYPE_NORMAL = "normal"
USERTYPE_EXTRAJUMP = "extra"
USERTYPE = USERTYPE_NORMAL
USER_MOVERATE_RATIO = 0.65
USER_JUMP_ACCELERATION_RATIO = (-7/8.)
USER_GRAVITY_RATIO = (1/8.)

#colors
OBSTACLECOLOR = (110, 110, 110)
USERCOLOR = (200, 210, 45)
BACKGROUNDCOLOR = (210, 210, 210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#lists used primarily for collision detection
RECTS_TO_UPDATE = []
OBSTACLELIST = []
POWER_LIST = []
POWER_OBJ_LIST = []

#keywords for powerups
EXTRA_JUMP = "extrajump"
TWO_JUMPS = "twojumps"