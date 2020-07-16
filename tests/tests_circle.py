from nose2.tools import *
from fibonachi.CLASSES import CIRCLE, COLUMN

def test_fall():
	round = CIRCLE(10, 20)
	round.fall()
	assert round.y == 21

def test_stop():
	round = CIRCLE(20, 10)
	round.fall()
	round.stop(20)
	assert round.y == 10

def test_lie():
	round = CIRCLE(20, 20)
	round1 = CIRCLE(20, 9)
	round1.fall()
	round1.lie(round.x, round.y)
	assert round1.y == 10
	round1.fall()
	round1.lie(round.x, round.y)
	assert round1.y == 10

def test_touch():
	col = COLUMN(20, 20)
	round = CIRCLE(20, 10)
	round.touch(col.return_coords())
	assert round.x == 30 or round.x == 10
