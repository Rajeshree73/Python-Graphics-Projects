from setup import *
from math import *


class Raindrop:

    def __init__(self, r, v_x, v_y, x, y):
        self.r = r
        self.v_init = [v_x, v_y]
        self.g = 1.0
        self.ground_height = 10
        self.ground_lev = int(SCREENSIZE[1] - self.ground_height)
        self.x = x
        self.y = y
        self.grounded = False

    def update(self):
        self.collision()
        self.x += self.v_init[0]
        self.y += self.v_init[1]
        self.v_init[1] += self.g

        if self.grounded:
            self.v_init = [0.0, 0.0]
            self.y = self.ground_lev

    def collision(self):
        if self.y >= self.ground_lev:
            self.v_init[1] = -0.9*self.v_init[1]
            self.grounded = True


class MainDrop(Raindrop):

    def __init__(self, r, color):
        self.r = r
        self.color = color
        self.sub_drops = None
        self.busted = False
        self.sub_drops_num = 100
        v_x, v_y = 0.0, 10.0*random.random()
        x, y = random.randint(0, SCREENSIZE[0]), 0.0
        super(MainDrop, self).__init__(r, v_x, v_y, x, y)
        # pg.mixer.music.load('drop.wav')

    def draw(self):
        # pg.draw.line(DISPSURFACE, self.color, (0, self.ground_lev), (SCREENSIZE[0], self.ground_lev), 1)
        self.burst()
        if self.busted:
            if self.sub_drops.grounded and self.grounded:
                self.resume()
        if self.busted:
            self.sub_drops.update()
            self.sub_drops.draw()
        else:
            pg.draw.circle(DISPSURFACE, self.color, (int(self.x), int(self.y)), self.r)

    def burst(self):
        if self.grounded and not self.busted:
            self.sub_drops = Subdrops(self.color, self.x, self.y, self.sub_drops_num)
            self.busted = True
            # pg.mixer.music.play()

    def resume(self):
        self.v_init = [0.0, 10.0*random.random()]
        self.x, self.y = random.randint(0, SCREENSIZE[0]), 0.0
        self.busted = False
        self.grounded = False
        self.sub_drops = None


class SubDrop(Raindrop):

    def __init__(self, color, x, y, vel):
        self.color = color
        v_x, v_y = vel[0], vel[1]
        r = 1
        super(SubDrop, self).__init__(r, v_x, v_y, x, y)

    def draw(self):
        if not self.grounded:
            pg.draw.circle(DISPSURFACE, self.color, (int(self.x), int(self.y)), self.r)


class Subdrops:
    def __init__(self, color, x, y, n):
        self.color = color
        self.x = x
        self.y = y
        self.n = n
        self.grounded = False
        self.sub_drops = [None for i in range(self.n)]
        for i in range(int(self.n/2)):
            vel = self.vel(i)
            self.sub_drops[i] = SubDrop(self.color, self.x, self.y-1, vel)
            self.sub_drops[self.n-i-1] = SubDrop(self.color, self.x, self.y-1, [-vel[0], vel[1]])

    def update(self):
        [self.sub_drops[i].update() for i in range(self.n)]
        if False not in [self.sub_drops[i].grounded for i in range(self.n)]:
            self.grounded = True

    def draw(self):
        co_ords = [(self.sub_drops[i].x, self.sub_drops[i].y) for i in range(self.n)]
        [pg.draw.line(DISPSURFACE, self.color, co_ords[i], co_ords[i+1], 1) for i in range(self.n-1)]
        pg.draw.line(DISPSURFACE, BACKGROUND, (self.sub_drops[int(self.n/3)].x, self.sub_drops[0].ground_lev),
                     (self.sub_drops[int(2*self.n/3)].x, self.sub_drops[0].ground_lev), 1)

    def vel(self, ind):
        vx = 10.0*cos(pi/self.n*ind)**3
        vy = -3.0*sin(pi/self.n*ind)+3.0*sin(3*pi/self.n*ind)-3.5*sin(5*pi/self.n*ind)-1.0*sin(7*pi/self.n*ind)
        return [random.random()*vx, random.random()*vy]
