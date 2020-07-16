from random import choice

#globals
WIDTH = 400
HEIGHT = 300
CIRCLE_SIZE = 10
COLUMN_SIZE = 5
START_X = 195
START_Y = 5

class COLUMN(object):
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def return_coords(self):
		return (self.x, self.y)

class CIRCLE(COLUMN):
	
	def fall(self):
		self.y += 1
	
	def stop(self, height):
		if self.y + CIRCLE_SIZE > height:
			self.y -= 1
	
	def lie(self, x, y):
		if self.x == x:
			if self.y + CIRCLE_SIZE == y + 1:
				self.y -= 1
	
	def touch(self, x_y):
		if self.x == x_y[0]:
			if self.y + CIRCLE_SIZE == x_y[1]:
				new_x = choice([x_y[0] - CIRCLE_SIZE, x_y[0] + CIRCLE_SIZE])
				self.x = new_x

class BUTTON(object):
	
	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text
	
	def spawn_new(self, mouse_x, mouse_y):
		if mouse_y > self.y and self.y + 20 > mouse_y:
			if mouse_x > self.x and self.x + 50 > mouse_x:
				return CIRCLE(START_X, START_Y)
