import viz

class Alien():
	def __init__(self, color):
		self.x = 0
		self.y = 0
		viz.startLayer(viz.POINTS)
		viz.pointSize(0)
		viz.vertexColor(color)
		viz.vertex(0, 0)
		viz.vertex(48, 0)
		viz.vertex(48, 32)
		viz.vertex(0, 32)
		image = viz.add('alien.png')
		self.vertices = viz.endLayer()
		self.quad = viz.addTexQuad()
		self.quad.setPosition([self.x+24, self.y+16, 0])
		self.quad.texture(image)
		self.quad.setScale(image.getSize())
		
		# Posts a translation to move the alien to new cordinates centered at x, y
	def translate(self, x, y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
		self.quad.setPosition([self.x+24, self.y+16, 0])
		
		# Returns true if the alien can move to the right without leaving the screen
	def canGoRight(self):
		if self.x + 48 + 5 < 320:
			return True
		else:
			return False
			
		# Returns false if the alien can move to the left without leaving the screen
	def canGoLeft(self):
		if self.x - 5 > -320:
			return True
		else:
			return False
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
		# Removes the alien
	def delete(self):
		self.vertices.remove()
		self.quad.remove()