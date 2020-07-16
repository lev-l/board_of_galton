try:
	from fibonachi.CLASSES import *
except ModuleNotFoundError:
	from CLASSES import *
finally:
	import threading

#objects
button = BUTTON(0, 0, "add circle")
round = CIRCLE(START_X, START_Y)

rounds = [round]
#standart objects
col = COLUMN(START_X, 20)

col1 = COLUMN(START_X - 10, 30)
col2 = COLUMN(START_X + 10, 30)

col3 = COLUMN(START_X - 20, 40)
col4 = COLUMN(START_X, 40)
col5 = COLUMN(START_X + 20, 40)

col6 = COLUMN(START_X - 30, 50)
col7 = COLUMN(START_X - 10, 50)
col8 = COLUMN(START_X + 10, 50)
col9 = COLUMN(START_X + 30, 50)

col10 = COLUMN(START_X - 40, 60)
col11 = COLUMN(START_X - 20, 60)
col12 = COLUMN(START_X, 60)
col13 = COLUMN(START_X + 20, 60) 
col14 = COLUMN(START_X + 40, 60)

col15 = COLUMN(START_X - 50, 70)
col16 = COLUMN(START_X - 30, 70)
col17 = COLUMN(START_X - 10, 70)
col18 = COLUMN(START_X + 10, 70)
col19 = COLUMN(START_X + 30, 70)
col20 = COLUMN(START_X + 50, 70)

columns = (col, col1, col2, col3, col4,
			col5, col6, col7, col8, col9,
			col10, col11, col12, col13,
			col14, col15, col16, col17, 
			col18, col19, col20)

class ENGINE(object):
	
	def spawn(self, e):
		mouseX = e.x
		mouseY = e.y
		print (e.x, e.y)
		new = button.spawn_new(mouseX, mouseY)
		print(new)
		if new:
			rounds.append(new)
	
	def lied(self, circle):
		global rounds
		
		for r in rounds:
			circle.lie(r.x, r.y)
	
	def touched(self, circle):
		global columns
		
		for column in columns:
			circle.touch(column.return_coords())
	
	def move(self):
		global rounds
		
		for r in rounds:
			r.fall()
			r.stop(HEIGHT)
			self.lied(r)
			self.touched(r)

en = ENGINE()
def start():
	en.move()
	threading.Timer(0.1, start).start()
