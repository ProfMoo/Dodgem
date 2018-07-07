import settings
import time
from Power import *

class TripleJumpPower(Power):
	def __init__ (self, surfacei, xi, yi, sizei, kindi):
		Power.__init__(self, surfacei, xi, yi, sizei, kindi, 2)
		self.inactiveTime = 2
