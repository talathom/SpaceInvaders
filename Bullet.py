import viz

class Bullet():
	def __init__(self, x, y):
		viz.startLayer(viz.POLYGON)
		viz.vertexColor(1, 1, 1)
		# Creates the bullet centered at 0, 0
		viz.vertex(0, 0)
		viz.vertex(5, 0)
		viz.vertex(5, 5)
		viz.vertex(0, 5)
		#Uses the arguments passed to the bullet to translate it to where ship is/was when it fired
		self.x = x
		self.y = y
		self.vertices = viz.endLayer()
		self.translate(self.x, self.y)
		
		#Removes the bullet
	def delete(self):
		self.vertices.remove()
		
		#Posts a translation to the bullet which moves it to a new center of x, y
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