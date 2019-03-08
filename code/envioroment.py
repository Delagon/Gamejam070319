import random as rand

class enviorment_object:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.life_time = 0
		self.type = 0
	def move(self, world):
		# 0: Up
		# 1: Right
		# 2: Down
		# 3: Left
		direction = rand.randint(0,3)
		newX = self.x
		newY = self.y
		if direction == 0:
			newY -= 1
		elif direction == 1:
			newX += 1
		elif direction == 2:
			newY += 1
		else:
			newX -= 1
		if not world[newX][newY].blocks(self):
			self.x = newX
			slef.y = newY

class tile:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.tile = None
	def blocks(self, other):
		if self.tile == None:
			return True

class level:
	def __init__(self):
		self.map = []
	def dist(self, pointa, pointb):
		# Takes pointa and pointb as tuples (xa,ya) (xb,yb)
		# Finds the shortest distance between them on the current map

