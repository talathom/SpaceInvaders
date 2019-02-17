import threading
import viz

class Thread(threading.Thread):
	def __init__(self, num, name, counter):
		threading.Thread.__init__(self)
		self.threadNum = num
		self.name = name
		self.counter = counter
		
	def run(self, event):
		self.onKeyDown(event)
		
	def onKeyDown(self, key):
		if key == "a" or key == viz.KEY_LEFT and not self.pause: #Move player left
			if self.player.getX() - 5 > -320:
				self.player.translate(self.player.getX()-5, self.player.getY())
			
		if key == "d" or key == viz.KEY_RIGHT and not self.pause: #Move player right
			if self.player.getX() + 53 < 320:
				self.player.translate(self.player.getX()+5, self.player.getY())
				
		if key == "p":
			if not self.pause:
				self.pause = True
			else:
				self.pause = False
		
		if (key == " ") and self.canFire and not self.pause: #Player fires a bullet
			viz.playSound("laser.wav")
			self.bullets.append(Bullet(self.player.getX() + 23, self.player.getY() + 41))
			self.canFire = False
				
			if not self.timer: # Start bullet timer on first fire
				self.starttimer(1, 1/25, viz.FOREVER)
				self.timer = True
		
		