class User(object):
	def __init__ (self, surfacei, xi, yi):
		self.surface = surfacei
		self.x = xi
		self.y = yi
		self.jumps = 2
		self.rect = None