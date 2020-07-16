from nose2.tools import *
from fibonachi.logic import ENGINE, START_Y, round, rounds

def test_spawn():
	e = ENGINE()
	e.spawn(round)
	print (rounds)

def test_move():
	e = ENGINE()
	e.move()
	assert round.y == START_Y + 1
