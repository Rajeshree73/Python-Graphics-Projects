from setup import *



class Raindrop:

	def __init__(self, r, v_x, v_y ,x, y):

		self.r = r
		self.v_init = [v_x, v_y]
		self.x = x
		self.y = y
		self.g = 1
		self.ground_height = 10
		self.ground_level = int(SCREENSIZE[1]-self.ground_height)
		self.grounded = False

	def update(self):
		self.collision()
		self.x += self.v_init[0]
		self.y += self.v_init[1]
		self.v_init[1] += self.g

		if self.grounded:
			self.v_init = [0,0]


	def collision(self):
		if self.y >= self.ground_level:
			self.v_init[1] = -0.9*self.v_init[1]
			self.grounded = True


class MainDrop(Raindrop):
	def __init__(self, r, colour):
		self.r = r
		self.colour = colour
		self.sub_drops = None
		self.busted = None
		self.sub_drops_num = 100
		v_x, v_y = 0.0, 10.0*random.random()
		x, y = random.randint(0, SCREENSIZE[0]), 0.0
		super(MainDrop, self).__init__(r, v_x, v_y ,x, y)
		pg.mixer.music.load('drop.wav')

	def draw(self):
		self.burst()
		if self.busted:
			if False not in [self.sub_drops[i].grounded for i in range(self.sub_drops_num)] and self.grounded:
				self.resume()

		if self.busted:
			[self.sub_drops[i].update() for i in range(self.sub_drops_num)]
			[self.sub_drops[i].draw() for i in range(self.sub_drops_num)]
		else:
			pg.draw.circle(DISPSURFACE, self.colour, (int(self.x), int(self.y)), self.r)
	

	def burst(self):
		if self.grounded and not self.busted:
			self.sub_drops = [SubDrop(self.colour,self.x, self.y) for i in range(self.sub_drops_num)]
			self.busted = True
			pg.mixer.music.play()

	def resume(self):
		
		self.v_init = [0.0, 10.0*random.random()]
		self.x, self.y = random.randint(0, SCREENSIZE[0]), 0.0
		self.busted = False
		self.grounded = False
		self.sub_drops = None
			

class SubDrop(Raindrop):
	def __init__(self, colour, x, y):
		self.colour = colour
		v_x, v_y = 10.0*(1-2*random.random()), -10.0*random.random()
		r = 1
		super(SubDrop, self).__init__(r, v_x, v_y ,x, y)

	def draw(self):
		pg.draw.circle(DISPSURFACE, self.colour, (int(self.x), int(self.y)), self.r)	


# class Rain:
#	def __init__(self):
#		self.drop = MainDrop(10, WHITE)
#		self.sub_drops = None
#
#	def updte(self):
#		self.drop.updte()

		



