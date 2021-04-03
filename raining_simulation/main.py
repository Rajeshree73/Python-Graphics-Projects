from raindrop import *
from pixel_processing import renderer

num_drops = 50
drops = [MainDrop(2, (240, 255, 255)) for i in range(num_drops)]


def setup():
    pass


def loop():
    # renderer()
    [drops[i].update() for i in range(num_drops)]
    [drops[i].draw() for i in range(num_drops)]


if __name__ == "__main__":
    setup()
    back_surf = pg.Surface(SCREENSIZE)
    back_surf.fill(BACKGROUND)
    back_surf.set_alpha(BACKALPHA)
    while True:
        CLOCK.tick(FPS)
        DISPSURFACE.blit(back_surf, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        loop()
        pg.display.update()
