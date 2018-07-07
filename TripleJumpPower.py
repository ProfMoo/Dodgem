import settings
import time
from Power import *
from UserFactory import *

class TripleJumpPower(Power):
	def __init__ (self, surfacei, xi, yi, sizei, kindi):
		Power.__init__(self, surfacei, xi, yi, sizei, kindi, 2)

	def givePower(self, user):
		userFactory = UserFactory()
		user = userFactory.changeUser(user, settings.USERTYPE_EXTRAJUMP)
		if (user.numJumps == 2 and user.jumps < 2):
			user.jumps += 1
		user.numJumps = 3