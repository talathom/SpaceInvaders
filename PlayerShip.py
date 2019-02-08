import viz

class PlayerShip():
	def __init__(self):
		viz.startLayer(viz.LINE_LOOP)
		viz.vertexColor(1, 1, 1)
		self.x = 0
		self.y = 0
		viz.vertex(0, 0)
		viz.vertex(48, 0)
		viz.vertex(48, 20)
		viz.vertex(32, 20)
		viz.vertex(32, 40)
		viz.vertex(16, 40)
		viz.vertex(16, 20)
		viz.vertex(0, 20)
		self.vertices = viz.endLayer()
		
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
	