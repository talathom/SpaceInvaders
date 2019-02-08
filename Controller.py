import viz
from PlayerShip import *
from Bullet import *
from Alien import *

class Controller(viz.EventClass):
	def __init__(self):
		viz.EventClass.__init__(self)
		self.player = PlayerShip()
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		self.callback(viz.TIMER_EVENT, self.onTimer)
		self.player.translate(0, -220)
		self.bullets = list()
		self.timer = False
		self.moveRight = True
		self.moveDown = False
		self.canFire = True #Stops a continuous stream of bullets from being fired
		self.starttimer(3, 1, viz.FOREVER)
		self.aliens = list()
		numAliensPerRow = 6
		spacing = 640 / numAliensPerRow
		colorCounter = 0
		y = 180
		x = -290
		self.xMax = 240
		self.xMin = -184
		color = viz.GREEN
		while x <= 320 and colorCounter <= numAliensPerRow*3:
			self.aliens.append(Alien(color))
			self.aliens[colorCounter].translate(x, y)
			colorCounter += 1
			if colorCounter == numAliensPerRow:
				color = viz.BLUE
				x = -290
				y -= 60
			elif colorCounter == numAliensPerRow*2:
				color = viz.RED
				x = -290
				y -= 60
			else:
				x += spacing
		self.starttimer(2, .5, viz.FOREVER)
		
	def onKeyDown(self, key):
		if key == "a" or key == viz.KEY_LEFT:
			if self.player.getX() - 5 > -320:
				self.player.translate(self.player.getX()-5, self.player.getY())
			
		if key == "d" or key == viz.KEY_RIGHT:
			if self.player.getX() + 53 < 320:
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
				else:
					for alien in self.aliens:
						if bullet.getX()+5 > alien.getX() and bullet.getY()+5 > alien.getY() and bullet.getX() < alien.getX() + 48 and bullet.getY() < alien.getY() + 32:
							bullet.delete()
							self.bullets.remove(bullet)
							alien.delete()
							self.aliens.remove(alien)
		elif num == 2:
			for alien in self.aliens:
				if (not self.moveRight and not alien.canGoLeft()) or (self.moveRight and not alien.canGoRight()):
					self.moveDown = True
					self.moveRight = True
				if not alien.canGoRight():
					self.moveRight = False
			for alien in self.aliens:
				if self.moveDown:
					alien.translate(alien.getX(), alien.getY()-15)
				elif self.moveRight:
					alien.translate(alien.getX() + 15, alien.getY())
				elif not self.moveRight:
					alien.translate(alien.getX() - 15, alien.getY())
				#Check Collisions
				if alien.getX()+48 > self.player.getX() and alien.getY()+32 > self.player.getY() and alien.getX() < self.player.getX() + 48 and alien.getY() < self.player.getY() + 32:
					print("GAME OVER")
			self.moveDown = False
				
					
		elif num == 3:
			self.canFire = True