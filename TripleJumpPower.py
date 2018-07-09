import settings
import time
from Power import *
from UserFactory import *

# load the image files

class TripleJumpPower(Power):
	def __init__ (self, xi, yi, sizei, kindi):
		Power.__init__(self, xi, yi, sizei, kindi, 2)
		self.surface = pygame.transform.scale(settings.TRIPLE_JUMP_POWER_IMG, (self.size, self.size))

	def givePower(self, user):
		userFactory = UserFactory()
		newUser = userFactory.changeUser(user, settings.USERTYPE_EXTRAJUMP)
		return newUser