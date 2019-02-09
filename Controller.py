import viz
from PlayerShip import *
from Bullet import *
from Alien import *

class Controller(viz.EventClass):
	def __init__(self):
		viz.EventClass.__init__(self)
		self.player = PlayerShip() # Initializes the player ship
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown) # Callback for key press
		self.callback(viz.TIMER_EVENT, self.onTimer) # Callback for timers
		self.player.translate(0, -220) # Moves the player to the correct position to start the game
		self.bullets = list() # list of active bullets on the screen
		self.timer = False #Whether the bullet timer has started, false if no bullets fired yet
		self.moveRight = True #Whether the aliens can move right
		self.moveDown = False # Whether the aliens should move down
		self.canFire = True #Stops a continuous stream of bullets from being fired
		self.pause = False # Controls whether the game is paused
		self.starttimer(3, .75, viz.FOREVER) # Timer to stop the continous stream of bullets
		self.aliens = list() #List of aliens active on scren
		numAliensPerRow = 6 #Number of aliens to spawn per row
		spacing = 640 / numAliensPerRow #Proper spacing between aliens
		colorCounter = 0 #Counts the aliens spawned to color them properly
		y = 180 #Default Y spawn for aliens
		x = -290 #Default X spawn for aliens
		color = viz.GREEN # Start by painting green aliens
		while x <= 320 and colorCounter <= numAliensPerRow*3:
			self.aliens.append(Alien(color)) #Add a new alien to the list
			self.aliens[colorCounter].translate(x, y)
			colorCounter += 1
			if colorCounter == numAliensPerRow: # When a new row begins
				color = viz.BLUE # Change color
				x = -290 # Reset X
				y -= 60 # Move Y down
			elif colorCounter == numAliensPerRow*2:
				color = viz.RED # Change color
				x = -290 # Reset X
				y -= 60 # Move Y down
			else:
				x += spacing # Continues increasing X to ensure proper spacing
		self.starttimer(2, .25, viz.FOREVER) # Starts the movement timer for aliens once they're all spawned
		
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
		
		if key == " " and self.canFire and not self.pause: #Player fires a bullet
			viz.playSound("laser.wav")
			self.bullets.append(Bullet(self.player.getX() + 23, self.player.getY() + 41))
			self.canFire = False
				
			if not self.timer: # Start bullet timer on first fire
				self.starttimer(1, 1/25, viz.FOREVER)
				self.timer = True
				
	def onTimer(self, num):
		if num == 1 and not self.pause: # Bullet Control Timer
			for bullet in self.bullets: # Move all bullets
				bullet.translate(bullet.getX(), bullet.getY()+1)
				if bullet.getY() > 240: # if bullet off screen remove it from memory
					bullet.delete()
					self.bullets.remove(bullet)
				else:
					for alien in self.aliens: #Check all aliens for each bullet and verify whether collisions exists
						if bullet.getX()+5 > alien.getX() and bullet.getY()+5 > alien.getY() and bullet.getX() < alien.getX() + 48 and bullet.getY() < alien.getY() + 32:
							bullet.delete() # If a collision exists remove the colliding objects
							self.bullets.remove(bullet)
							alien.delete()
							self.aliens.remove(alien)
							viz.playSound("boop.wav")
							if len(self.aliens) == 0: # When no aliens remain after a collision
								print("You Win!")
		elif num == 2 and not self.pause: #Alien movement timer
			for alien in self.aliens: # Check to see where the aliens can move
				if (not self.moveRight and not alien.canGoLeft()) or (self.moveRight and not alien.canGoRight()):
					self.moveDown = True # Flags that the aliens need to move down
					self.moveRight = True # Aliens can move right
				if not alien.canGoRight():
					self.moveRight = False # Aliens can move left
			for alien in self.aliens:
				if self.moveDown: # Attempt move down if necessary
					alien.translate(alien.getX(), alien.getY()-15)
				elif self.moveRight: # If no move down try moving right
					alien.translate(alien.getX() + 15, alien.getY())
				elif not self.moveRight: # If not moving right or down move left
					alien.translate(alien.getX() - 15, alien.getY())
				#Check Collisions
				if alien.getX()+48 > self.player.getX() and alien.getY()+32 > self.player.getY() and alien.getX() < self.player.getX() + 48 and alien.getY() < self.player.getY() + 32:
					print("GAME OVER") #Remove player ship if a collision exists
					viz.playSound("explosion.wav")
					self.player.delete()
					self.pause = True
			self.moveDown = False # Reset the movedown once all aliens have been processed
				
					
		elif num == 3 and not self.pause: #Firing timer
			self.canFire = True