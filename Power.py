import settings
import time

class Power(object):
	def __init__ (self, surfacei, xi, yi, sizei, kindi):
		self.surface = surfacei
		self.x = xi
		self.y = yi
		self.size = sizei
		self.lastHit = time.time()
		self.kind = kindi