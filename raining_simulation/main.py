
from raindrops import *

num_drops = 50
# Creating instance of Drop
drops = [MainDrop(3, WHITE) for i in range(num_drops)]

def setup():

	pass


def loop():
	
	[drops[i].update() for i in range(num_drops)]
	[drops[i].draw() for i in range(num_drops)]



if __name__ == '__main__':
	setup()
	backg_surf = pg.Surface(SCREENSIZE)
	backg_surf.set_alpha(BACKALPHA)
	backg_surf.fill(BACKGROUND)

	while True:
		CLOCK.tick(FPS) # control frequncy
		DISPSURFACE.blit(backg_surf, (0,0))
		# to track every events in pygame
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		loop()
		pg.display.update()










