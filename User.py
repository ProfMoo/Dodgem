import settings
import pygame
import time
from pygame.locals import *

class User(object):
	def __init__ (self, xi, yi, oldUser = None):
		if (oldUser is None): #default user
			#location and size
			self.surface = pygame.transform.scale(settings.USER_IMG, (settings.USER_SIZE, settings.USER_SIZE))
			self.x = xi
			self.y = yi
			self.rect = None
			self.size = settings.USER_SIZE

			#controls movement, but these are from settings
			self.jumpAcceleration = settings.USER_JUMP_ACCELERATION_RATIO * self.size
			self.gravity = settings.USER_GRAVITY_RATIO * self.size
			self.moverate = settings.USER_MOVERATE_RATIO * self.size

			#controls jumping and collision
			self.numJumps = 2
			self.jumps = 2
			self.vertSpeed = 0
			self.sitting = False

			#controls movement left and right
			self.horizontalAcceleration = 0
			self.moveLeft = False
			self.moveRight = False
		else:
			self.surface = oldUser.surface
			self.x = oldUser.x
			self.y = oldUser.y
			self.rect = oldUser.rect
			self.size = oldUser.size

			#controls movement, but these are from settings
			self.moverate = oldUser.moverate
			self.jumpAcceleration = oldUser.jumpAcceleration
			self.gravity = oldUser.gravity

			#controls jumping and collision
			self.numJumps = oldUser.numJumps
			self.jumps = oldUser.jumps
			self.vertSpeed = oldUser.vertSpeed
			self.sitting = oldUser.sitting

			#controls movement left and right
			self.horizontalAcceleration = oldUser.horizontalAcceleration
			self.moveLeft = oldUser.moveLeft
			self.moveRight = oldUser.moveRight

	def move(self):
		#print("everytime: ", self.horizontalAcceleration)
		self.zeroHorizontalAcceleration()
		self.leftMovement(settings.OBSTACLELIST)
		self.zeroHorizontalAcceleration()
		self.rightMovement(settings.OBSTACLELIST)
		self.vertMovement(settings.OBSTACLELIST)

	def zeroHorizontalAcceleration(self):
		if (abs(self.horizontalAcceleration) < 0.01):
			self.horizontalAcceleration = 0

	def leftMovement(self, obstacles):
		if (self.moveLeft):
			if (self.horizontalAcceleration > -1.1):
				self.horizontalAcceleration -= 0.33
		else: 
			if (self.horizontalAcceleration < 0 and self.moveRight is False):
				self.horizontalAcceleration += 0.33

		if (self.horizontalAcceleration < 0):
			attemptedMovement = self.x + (self.moverate * self.horizontalAcceleration)
			#print("attempt: ", attemptedMovement)
			i = 0
			moveX = attemptedMovement
			while (i < len(obstacles)): #checking for obstacle collision
				obs = obstacles[i]
				# print("first: ", obs.x + obs.width < moveX)
				# print("second: ", obs.x - self.size/2 > moveX)
				#inside right wall, below top wall, above bottom wall, inside left wall
				if (obs.x + obs.width > moveX and obs.y < (self.y + self.size) and obs.y + obs.height > self.y and obs.x < moveX):
					self.horizontalAcceleration = 0
					moveX = obs.x + obs.width
				i += 1
			self.x = moveX

	def rightMovement(self, obstacles):
		if (self.moveRight):
			if (self.horizontalAcceleration < 1.1):
				self.horizontalAcceleration += 0.33
		else: 
			if (self.horizontalAcceleration > 0 and self.moveLeft is False):
				self.horizontalAcceleration -= 0.33

		if (self.horizontalAcceleration > 0):
			attemptedMovement = self.x + (self.size/2) + (self.moverate * self.horizontalAcceleration)
			i = 0
			rectangle = 0
			moveX = attemptedMovement
			while (i < len(obstacles)): #checking for obstacle collision
				obs = obstacles[i]
				if (obs.x - self.size/2 < moveX and obs.y < (self.y + self.size) and obs.y + obs.height > self.y and obs.x + obs.width > self.x):
					self.horizontalAcceleration = 0
					moveX = obs.x - self.size/2
				i += 1
			self.x = moveX - self.size/2

	def vertMovement(self, obstacles):
		#calculate center of where user wants to be
		#see if it is inside of any obstacle
		#move right above/below block
		attemptedMovement = self.y + self.vertSpeed
		if (self.vertSpeed > 0): #going down
			i = 0
			moveY = attemptedMovement
			while (i < len(obstacles)): #checking for obstacle collision
				obs = obstacles[i]
				leftSide = obs.x
				rightSide = obs.x + obs.width
				topSide = obs.y
				bottomSide = obs.y + obs.height
				if (moveY + self.size > topSide and moveY + self.size < bottomSide and self.x + self.size > leftSide and self.x < rightSide):
					moveY = obs.y - self.size
					self.vertSpeed = 0
					self.jumps = self.numJumps
					self.sitting = True
				i += 1
			if (self.sitting is False):
				self.vertSpeed += self.gravity
			self.y = moveY
		elif (self.vertSpeed < 0): #going up
			i = 0
			moveY = attemptedMovement
			while (i < len(obstacles)): #checking for obstacle collision
				obs = obstacles[i]
				leftSide = obs.x
				rightSide = obs.x + obs.width
				topSide = obs.y
				bottomSide = obs.y + obs.height
				if (moveY > topSide and moveY < bottomSide and self.x + self.size > leftSide and self.x < rightSide):
					moveY = obs.y + obs.height
					self.vertSpeed = 0
				i += 1
			if (self.sitting is False):
				self.vertSpeed += self.gravity
			self.y = moveY
		elif (self.sitting is True): #on an obstacle
			freeToFall = True
			i = 0
			while (i < len(obstacles)):
				obs = obstacles[i]
				leftSide = obs.x
				rightSide = obs.x + obs.width
				topSide = obs.y
				bottomSide = obs.y + obs.height
				if (self.y + self.size > topSide and self.y + self.size < bottomSide and self.x > leftSide and self.x < rightSide):
					freeToFall = False
				i += 1

			if freeToFall:
				self.vertSpeed += self.gravity
				self.sitting = False
		else:
			self.vertSpeed += self.gravity

	def checkIfCaptured(self, powers):
		userRect = pygame.Rect(self.x, self.y, self.size, self.size)
		return userRect.collidelist(powers)