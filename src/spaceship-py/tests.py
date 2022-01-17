import sys
from spaceship import spaceship

def tests():
	def test(x, y):
		linenum = sys._getframe(1).f_lineno
		assert x == y, "Test at line {0} FAILED.".format(linenum)

	test(spaceship(1, 2), -1)
	test(spaceship(52, 42), 1)
	test(spaceship(15, 15), 0)
	test(spaceship(3.14, 3.1415), -1)
	test(spaceship("y", "x"), 1)
	test(spaceship("aa", "zz"), -1)
	test(spaceship("john", "john"), 0)
	test(spaceship([1, 2, 3], [1, 2, 3]), 0)
	test(spaceship([1, 2, 3], []), 1)
	test(spaceship([1, 2, 3], [1, 2, 1]), 1)
	test(spaceship([1, 2, 3], [1, 2, 4]), -1)
	print("All tests SUCCESS")

tests()