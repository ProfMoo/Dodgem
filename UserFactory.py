import settings
import pygame
import time
from pygame.locals import *
from User import *

class UserFactory(object):
	def __init__(self):
		pass

	def createUser(self, kind):
		STARTLOCATION = (settings.HALF_WINWIDTH, settings.HALF_WINHEIGHT - 100)
		if (kind == settings.USERTYPE_NORMAL):
			user = User(STARTLOCATION[0], STARTLOCATION[1])
		elif (kind == settings.USERTYPE_EXTRAJUMP):
			user = User(STARTLOCATION[0], STARTLOCATION[1])
			#TODO: put in changes to do triple jump
		return user

	def changeUser(self, user, toKind):
		userToReturn = User(user.x, user.y, user)
		if (toKind == settings.USERTYPE_NORMAL):
			if (userToReturn.numJumps == 3 and userToReturn.jumps > 0):
				userToReturn.jumps -= 1
			userToReturn.numJumps = 2
		elif (toKind == settings.USERTYPE_EXTRAJUMP):
			if (userToReturn.numJumps == 2 and userToReturn.jumps < 2):
				userToReturn.jumps += 1
			userToReturn.numJumps = 3

		return userToReturn
