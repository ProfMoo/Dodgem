import settings
import time
from Power import *
from UserFactory import *

class DoubleJumpPower(Power):
	def __init__ (self, xi, yi, sizei, kindi):
		Power.__init__(self, xi, yi, sizei, kindi, 2)
		self.surface = pygame.transform.scale(settings.DOUBLE_JUMP_POWER_IMG, (self.size, self.size))

	def givePower(self, user):
		userFactory = UserFactory()
		newUser = userFactory.changeUser(user, settings.USERTYPE_NORMAL)
		if (user.numJumps == 3 and newUser.jumps > 0):
			newUser.jumps -= 1
		newUser.numJumps = 2
		return newUser