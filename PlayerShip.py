import viz   

class PlayerShip():
	def __init__(self):
		viz.startLayer(viz.POINTS)
		viz.vertexColor(viz.BLACK)
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
		image = viz.add('player.png')
		self.quad = viz.addTexQuad()
		self.quad.setPosition([self.x+24, self.y+20, 0])
		self.quad.texture(image)
		self.quad.setScale(image.getSize())
		self.vertices = viz.endLayer()
		
		# Deletes the ship
	def delete(self):
		self.vertices.remove()
		
		#Moves the ship to a new center at x, y
	def translate(self, x, y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
		self.quad.setPosition([self.x+24, self.y+20, 0])
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
	