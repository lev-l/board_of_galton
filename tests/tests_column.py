from nose2.tools import *
from fibonachi.CLASSES import COLUMN

def test_column():
	col = COLUMN(10, 20)
	assert col.return_coords() == (10, 20)
