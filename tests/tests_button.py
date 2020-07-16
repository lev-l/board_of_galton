from nose2.tools import *
from fibonachi.CLASSES import BUTTON

def test_spawn_new():
	button = BUTTON(0, 10, "add new")
	r = button.spawn_new(3, 15)
	r.fall()
	assert r.y == 6
	assert r.x == 195
