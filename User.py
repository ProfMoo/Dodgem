import settings
import pygame
import time
from pygame.locals import *

class User(object):
	def __init__ (self, surfacei, xi, yi, moveratei, sizei, jumpAccelerationi, gravityi, numJumpsi):
		self.surface = surfacei
		self.x = xi
		self.y = yi
		self.moverate = moveratei
		self.size = sizei
		self.jumpAcceleration = jumpAccelerationi
		self.gravity = gravityi
		self.numJumps = numJumpsi
		self.jumps = numJumpsi
		self.rect = None
		self.vertSpeed = 0
		self.sitting = True

	def leftMovement(self, obstacles):
		attemptedMovement = self.x - (self.size/2) - self.moverate
		i = 0
		moveX = attemptedMovement
		while (i < len(obstacles)):
			obs = obstacles[i]
			# print("first: ", obs.x + obs.width < moveX)
			# print("second: ", obs.x - self.size/2 > moveX)
			if (obs.x - self.size/2 < moveX and obs.y < (self.y + self.size) and obs.y + obs.height > self.y and obs.x + obs.width > moveX):
				moveX = obs.x + obs.width - self.size/2
			i += 1
		self.x = moveX + self.size/2

	def rightMovement(self, obstacles):
		attemptedMovement = self.x + (self.size/2) + self.moverate
		i = 0
		rectangle = 0
		moveX = attemptedMovement
		while (i < len(obstacles)):
			obs = obstacles[i]
			if (obs.x - self.size/2 < moveX and obs.y < (self.y + self.size) and obs.y + obs.height > self.y and obs.x + obs.width > self.x):
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
			while (i < len(obstacles)):
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
			while (i < len(obstacles)):
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