import unittest

class SimpleTest(unittest.TestCase):

	def test_addition(self):
		a = 2
		b = 5
		self.assertTrue( (a + b) == 7 )

if __name__ == '__main__':
    unittest.main()