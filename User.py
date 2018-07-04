class User(object):
	def __init__ (self, surfacei, xi, yi):
		self.surface = surfacei
		self.x = xi
		self.y = yi
		self.jumps = 2
		self.rect = None

	def leftMovement(self, moverate, usersize, obstacles):
		attemptedMovement = self.x-(usersize/2)-moverate
		print("x: ", self.x)
		print("attempt: ", attemptedMovement)
		i = 0
		moveX = attemptedMovement
		while (i < len(obstacles)):
			if (obstacles[i].x + obstacles[i].width < moveX):
				moveX = obstacles[i].x + obstacles[i].width
			i += 1
		self.x = moveX + (usersize/2)

	def rightMovement(self, moverate, usersize, obstacles):
		attemptedMovement = self.x+(usersize/2)+moverate
		i = 0
		rectangle = 0
		moveX = attemptedMovement
		while (i < len(obstacles)):
			if (obstacles[i].x - usersize/2 < moveX):
				moveX = obstacles[i].x - usersize/2
			i += 1

		#moveX 
		self.x = moveX - usersize/2