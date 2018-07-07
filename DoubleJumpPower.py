import settings
import time
from Power import *

class DoubleJumpPower(Power):
	def __init__ (self, surfacei, xi, yi, sizei, kindi):
		Power.__init__(self, surfacei, xi, yi, sizei, kindi, 2)

	def givePower(self, user):
		if (user.numJumps == 3 and user.jumps > 0):
			user.jumps -= 1
		user.numJumps = 2