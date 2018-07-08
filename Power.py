import settings
import time
import pygame

class Power(object):
	def __init__ (self, xi, yi, sizei, kindi, inactiveTimei):
		self.rect = pygame.Rect(xi, yi, sizei, sizei)
		self.x = xi
		self.y = yi
		self.size = sizei
		self.kind = kindi
		self.active = True #if the user can collected and see the powerup
		self.triggeredTime = time.time() - 1 #keeps track of when the user collected it
		self.inactiveTime = inactiveTimei #how long the item is supposed to stay inactive

	def draw(self):
		if (self.active):
			settings.DISPLAYSURF.blit(self.surface, self.rect)
			pygame.display.update(self.rect)
		else:
			coverRect = pygame.Rect(self.x, self.y, self.size, self.size)
			pygame.draw.rect(settings.DISPLAYSURF, settings.BACKGROUNDCOLOR, coverRect)
			pygame.display.update(coverRect)

	def hit(self, user):
		currentTime = time.time()
		newUser = user
		if (currentTime - self.triggeredTime > 0.25 and self.active == True): #if we're going to register this collision as a hit
			newUser = self.givePower(user)
			print("hit")
			self.active = False
			self.triggeredTime = time.time()
		return newUser

	def makeActive(self, currentTime):
		if (self.inactiveTime - 0.1 < currentTime - self.triggeredTime < self.inactiveTime + 0.1):
			self.active = True