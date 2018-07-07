import settings
import pygame
import time
from pygame.locals import *
from User import *

class UserFactory(object):
	def __init__(self):
		pass

	def createUser(self, kind):
		#when creating user, these are the variables:
		#(surface, x, y, moverate, size, jump_accel, gravity, numjumps)
		STARTLOCATION = (settings.HALF_WINWIDTH, settings.HALF_WINHEIGHT - 100)
		if (kind == settings.USERTYPE_NORMAL):
			# USER_MOVERATE = 20
			# USER_SIZE = 40
			# USER_JUMPACCELERATION = -35
			# USER_GRAVITY = 5
			# NUM_JUMPS = 2
			USER_SIZE = 40
			user = User(pygame.transform.scale(settings.USER_IMG, (USER_SIZE, USER_SIZE)), \
				STARTLOCATION[0], STARTLOCATION[1], USER_SIZE * settings.USER_MOVERATE_RATIO, USER_SIZE, \
				USER_SIZE * settings.USER_JUMP_ACCELERATION_RATIO, USER_SIZE * settings.USER_GRAVITY_RATIO, 2)
		elif (kind == settings.USERTYPE_EXTRAJUMP):
			USER_SIZE = 40
			user = User(pygame.transform.scale(settings.USER_IMG, (USER_SIZE, USER_SIZE)), \
				STARTLOCATION[0], STARTLOCATION[1], USER_SIZE * settings.USER_MOVERATE_RATIO, USER_SIZE, \
				USER_SIZE * settings.USER_JUMP_ACCELERATION_RATIO, USER_SIZE * settings.USER_GRAVITY_RATIO, 3)
			
		return user

	def changeUser(self, user, toKind):
		if (toKind == settings.USERTYPE_NORMAL):
			userToReturn = User(pygame.transform.scale(settings.USER_IMG, (user.size, user.size)), \
				user.x, user.y, user.moverate, user.size, user.jumpAcceleration, user.gravity, 2)
		elif (toKind == settings.USERTYPE_EXTRAJUMP):
			userToReturn = User(pygame.transform.scale(settings.USER_IMG, (user.size, user.size)), \
				user.x, user.y, user.moverate, user.size, user.jumpAcceleration, user.gravity, 3)

		return userToReturn
