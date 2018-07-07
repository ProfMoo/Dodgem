import settings
import time
from Power import *

class TripleJumpPower(object):
	def __init__ (self, surfacei, xi, yi, sizei, kindi):
		self.surface = surfacei
		self.x = xi
		self.y = yi
		self.size = sizei
		self.lastHit = time.time()
		self.kind = kindi