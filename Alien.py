import viz

class Alien():
	def __init__(self, color):
		self.x = 0
		self.y = 0
		viz.startLayer(viz.POLYGON)
		viz.vertexColor(color)
		viz.vertex(0, 0)
		viz.vertex(48, 0)
		viz.vertex(48, 32)
		viz.vertex(0, 32)
		self.vertices = viz.endLayer()
		
	def translate(self, x, y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
		
	def canGoRight(self):
		if self.x + 48 + 5 < 320:
			return True
		else:
			return False
			
	def canGoLeft(self):
		if self.x - 5 > -320:
			return True
		else:
			return False
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def delete(self):
		self.vertices.remove()