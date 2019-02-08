import viz
from PlayerShip import *
from Bullet import *

class Controller(viz.EventClass):
	def __init__(self):
		viz.EventClass.__init__(self)
		self.player = PlayerShip()
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		self.callback(viz.TIMER_EVENT, self.onTimer)
		self.player.translate(0, -220)
		self.bullets = list()
		self.timer = False
		self.canFire = True #Stops a continuous stream of bullets from being fired
		self.starttimer(3, 1, viz.FOREVER)
		
	def onKeyDown(self, key):
		if key == "a" or key == viz.KEY_LEFT:
			self.player.translate(self.player.getX()-5, self.player.getY())
			
		if key == "d" or key == viz.KEY_RIGHT:
			self.player.translate(self.player.getX()+5, self.player.getY())
		
		if key == " " and self.canFire:
			self.bullets.append(Bullet(self.player.getX() + 23, self.player.getY() + 41))
			self.canFire = False
				
			if not self.timer:
				self.starttimer(1, 1/25, viz.FOREVER)
				self.timer = True
				
	def onTimer(self, num):
		if num == 1:
			for bullet in self.bullets:
				bullet.translate(bullet.getX(), bullet.getY()+1)
				if bullet.getY() > 240:
					bullet.delete()
					self.bullets.remove(bullet)
		elif num == 2:
			pass
			
		elif num == 3:
			self.canFire = True