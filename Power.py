import settings
import time
import pygame

class Power(object):
	def __init__ (self, surfacei, xi, yi, sizei, kindi, inactiveTimei):
		self.surface = surfacei
		self.rect = pygame.Rect(xi, yi, sizei, sizei)
		self.x = xi
		self.y = yi
		self.size = sizei
		self.lastHit = time.time()
		self.kind = kindi
		self.active = True
		self.triggeredTime = None
		self.inactiveTime = inactiveTimei

	def draw(self):
		if (self.active):
			settings.DISPLAYSURF.blit(self.surface, self.rect)
			pygame.display.update(self.rect)
		else:
			coverRect = pygame.Rect(self.x, self.y, self.size, self.size)
			pygame.draw.rect(settings.DISPLAYSURF, settings.BACKGROUNDCOLOR, coverRect)
			pygame.display.update(coverRect)

	def hit(self, user, powerBackEvent):
		currentTime = time.time()
		if (currentTime - self.lastHit > 0.25 and self.active == True): #if we're going to register this collision as a hit
			self.lastHit = time.time()
			user.givePower(self.kind)
			print("hit")

			# coverRect = pygame.Rect(self.x, self.y, self.size, self.size)
			# pygame.draw.rect(settings.DISPLAYSURF, settings.BACKGROUNDCOLOR, coverRect)
			# settings.RECTS_TO_UPDATE.append(coverRect)


			# self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
			# settings.DISPLAYSURF.blit(self.surface, self.rect)
			self.active = False
			self.triggeredTime = time.time()
			pygame.time.set_timer(powerBackEvent, self.inactiveTime * 1000)

	def makeActive(self):
		currentTime = time.time()
		if (self.inactiveTime - 0.1 < currentTime - self.triggeredTime < self.inactiveTime + 0.1):
			self.active = True