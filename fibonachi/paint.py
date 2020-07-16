from tkinter import *
from logic import *
import sys

win = Tk()
can = Canvas(win, width=WIDTH, height=HEIGHT)

def repaint():
	can.delete(ALL)
	can.create_rectangle(-1, -1, WIDTH + 1, HEIGHT + 1, fill="gray")
	
	x_y = col.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	
	x_y = col1.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col2.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	
	x_y = col3.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col4.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col5.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	
	x_y = col6.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col7.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col8.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col9.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	
	x_y = col10.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col11.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col12.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col13.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col14.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	
	x_y = col15.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col16.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col17.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col18.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col19.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	x_y = col20.return_coords()
	can.create_rectangle(x_y[0], x_y[1], x_y[0] + COLUMN_SIZE, x_y[1] + COLUMN_SIZE, fill="green")
	
	text = Label(can, text=button.text)
	text.place(x=button.x, y=button.y)
	
	for r in rounds:
		can.create_rectangle(r.x, r.y, r.x + CIRCLE_SIZE, r.y + CIRCLE_SIZE, fill="red")
	
	can.pack()
	threading.Timer(0.1, repaint).start()

start()
repaint()
win.bind("<Button-1>", en.spawn)
threading.Timer(20, sys.exit).start()
win.mainloop()
