

class rover:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.range = 0
	def getRange(self): # Return the range (in units)
		return self.range
	def getCoords(self): # Retruns the co-ords as a tuple
		return (self.x,self.y)
	
