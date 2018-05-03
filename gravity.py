# mouse gravity experiment

import pygame as pg, math, sys
from random import randint
from pygame.locals import *

pg.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
bg_color = (0,0,0)
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
balls = []
colors = [
		(200,200,50),
		(255,255,255),
		(100,240,0),
		(0,0,150),
		(50,140,200),
		(220, 40, 0),
		(230, 0, 25)
		]
color = (255,255,255)

class Ball(pg.sprite.Sprite):

	def __init__(self, x, y, vx = 0, vy = 0, r = 15):
		pg.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.ax = 0
		self.ay = 0
		self.r = r
		balls.append(self)

	def acceleration(self):
		pass

	def update(self):
		mousepos = pg.mouse.get_pos()
		distx = mousepos[0] - self.x
		disty = mousepos[1] - self.y

		if distx > 0:
			self.vx = (self.vx + 1) * 0.995
		elif distx < 0:
			self.vx = (self.vx - 1) * 0.995
		if disty > 0:
			self.vy = (self.vy + 1) * 0.995
		elif disty < 0:
			self.vy = (self.vy - 1) * 0.995

		self.x = int(self.x + self.vx)
		self.y = int(self.y + self.vy)
		pg.draw.circle(screen, color, (self.x,self.y), self.r)

def main():
	global bg_color, color
	clock = pg.time.Clock()
	for i in range(1, 20):
		ball = Ball(randint(10, SCREEN_WIDTH - 10), 10*i, 0, 0, 8)
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					color = colors[randint(0,len(colors) - 1)]
				elif event.button == 3:
					if bg_color == (0,0,0):
						bg_color = (230,230,230)
					else:
						bg_color = (0,0,0)
		screen.fill(bg_color)
		for ball in balls:
			ball.update()
		pg.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main()