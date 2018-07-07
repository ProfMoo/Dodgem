import settings
import time
from Power import *

class DoubleJumpPower(Power):
	def __init__ (self, surfacei, xi, yi, sizei, kindi):
		Power.__init__(self, surfacei, xi, yi, sizei, kindi, 4)
		self.inactiveTime = 5