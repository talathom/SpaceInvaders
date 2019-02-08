import viz

class Bullet():
	def __init__(self, x, y):
		viz.startLayer(viz.POLYGON)
		viz.vertexColor(1, 1, 1)
		viz.vertex(0, 0)
		viz.vertex(5, 0)
		viz.vertex(5, 5)
		viz.vertex(0, 5)
		self.x = x
		self.y = y
		self.vertices = viz.endLayer()
		self.translate(self.x, self.y)
		
	def delete(self):
		self.vertices.remove()
		
	def translate(self, x, y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y