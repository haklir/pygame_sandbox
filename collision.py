# ball collision practice

import pygame as pg, sys, time, math
from pygame.locals import *
from random import randint

BALL_COUNT = 50
SPEED = 0.4
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FPS = 60

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

class Ball:

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

	def __init__(self, x, y, vx, vy, r=15):
		self.x = x
		self.y = y
		self.vy = vy
		self.vx = vx
		self.r = r
		self.color = self.colors[randint(0, len(self.colors) - 1)]
		self.balls.append(self)

	def move(self):

		if SPEED == 0:
			return

		def bumper_collision(x, y, vx, vy, r):
			pass
			
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

		self.x = int(self.x + SPEED*self.vx)
		self.y = int(self.y + SPEED*self.vy)

		if self.x >= SCREEN_WIDTH - self.r:
			self.x = SCREEN_WIDTH*2 - self.x - 2*self.r
			self.vx = -self.vx * 0.995
		elif self.x <= 0 + self.r:
			self.x = -self.x + 2*self.r
			self.vx = -self.vx * 0.995
		if self.y >= SCREEN_HEIGHT - self.r:
			self.y = SCREEN_HEIGHT*2 - self.y - 2*self.r
			self.vy = -self.vy * 0.995
		elif self.y <= 0 + self.r:
			self.y = -self.y + 2*self.r
			self.vy = -self.vy * 0.995

		# if math.sqrt((self.x - 600)**2 + (self.y - 300)**2) <= self.r + 60:
		# 	bumper_collision(self.x, self.y, self.vx, self.vy, self.r)


for i in range(BALL_COUNT):
	a = Ball(randint(10,SCREEN_WIDTH - 10), randint(10,SCREEN_HEIGHT), randint(-10, 10), randint(-10, 10) , randint(4,8))

if __name__ == '__main__':
	clock = pg.time.Clock()
	i = 1; j = 1; k = 1
	di = 1; dj = 0.8; dk = 0.5
	color_slide = True
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button  == 1:
					color_slide = not color_slide
				elif event.button == 3:
					pass
				elif event.button == 5 and SPEED >= 0.05:
					SPEED -= 0.05
				elif event.button == 4 and SPEED < 1:
					SPEED += 0.05
		screen.fill((int(i), int(j), int(k)))
		for ball in a.balls:
			Ball.move(ball)
			pg.draw.circle(screen, ball.color, (ball.x,ball.y), ball.r)
		pg.display.update()
		if color_slide:
			if i > 254 or i < 1:	
				di = -di
			if j > 254 or j < 1:
				dj = -dj
			if k > 254 or k < 1:
				dk = -dk
			i += di; j += dj; k += dk
		clock.tick(FPS)